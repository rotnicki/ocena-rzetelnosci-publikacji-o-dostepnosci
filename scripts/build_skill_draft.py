#!/usr/bin/env python3
"""Build a reproducible, self-contained Agent Skill archive from the 0.3 branch."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tempfile
import zipfile
from pathlib import Path


PACKAGE_NAME = "assess-accessibility-articles"
VERSION = "0.3.0-draft"


def check_relative_links(skill_dir: Path) -> None:
    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", skill_text)
    missing = [link for link in links if "://" not in link and not (skill_dir / link).exists()]
    if missing:
        raise RuntimeError(f"Missing files referenced by SKILL.md: {missing}")


def write_deterministic_zip(source_dir: Path, destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source_dir.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            relative = Path(PACKAGE_NAME) / path.relative_to(source_dir)
            info = zipfile.ZipInfo(str(relative), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())


def build(repo: Path, output_dir: Path) -> tuple[Path, str]:
    with tempfile.TemporaryDirectory(prefix="skill-0.3-draft-") as temp_name:
        skill_dir = Path(temp_name) / PACKAGE_NAME
        shutil.copytree(repo / "skill", skill_dir, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

        skill_path = skill_dir / "SKILL.md"
        skill_text = skill_path.read_text(encoding="utf-8")
        marker = "Select and record the methodology version before reading the publication critically."
        replacement = (
            "This working-draft package is fixed to methodology 0.3. "
            "Select and record the methodology version before reading the publication critically."
        )
        if marker not in skill_text:
            raise RuntimeError("Expected version-selection marker not found in SKILL.md")
        skill_text = skill_text.replace(marker, replacement, 1)
        skill_text = skill_text.replace(
            "Use version 0.1 unless the user or a frozen calibration prompt explicitly selects another version. ",
            "Use the included 0.3 draft; the older files are retained only for repository compatibility. ",
            1,
        )
        skill_path.write_text(skill_text, encoding="utf-8")

        shutil.copy2(repo / "LICENSE.md", skill_dir / "LICENSE.md")
        (skill_dir / "licenses").mkdir(exist_ok=True)
        shutil.copy2(repo / "licenses" / "MIT.txt", skill_dir / "licenses" / "MIT.txt")
        manifest = {
            "name": PACKAGE_NAME,
            "version": VERSION,
            "status": "working-draft-not-a-release",
            "methodology_version": "0.3-draft",
            "licenses": {
                "text_and_methodology": "CC-BY-4.0",
                "code_and_technical_files": "MIT",
            },
            "notice": "For review and testing only. Rules may change before v0.3.0.",
        }
        (skill_dir / "DRAFT-MANIFEST.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        check_relative_links(skill_dir)

        output_dir.mkdir(parents=True, exist_ok=True)
        destination = output_dir / f"{PACKAGE_NAME}-v{VERSION}.zip"
        write_deterministic_zip(skill_dir, destination)

    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    destination.with_suffix(destination.suffix + ".sha256").write_text(
        f"{digest}  {destination.name}\n", encoding="utf-8"
    )
    return destination, digest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("dist"))
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent.parent
    destination, digest = build(repo, args.output)
    print(f"{destination}: {digest}")


if __name__ == "__main__":
    main()
