#!/usr/bin/env python3
"""Build reproducible, version-specific Agent Skill release archives."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path


RELEASES = {
    "0.1.0": {
        "source_commit": "af83066983e832cd7f61b7c2bd99482a07731afc",
        "methodology": "0.1",
        "replacement": (
            "Before assessing a publication, read",
            "This version-specific package is fixed to methodology 0.1. Before assessing a publication, read",
        ),
    },
    "0.2.0": {
        "source_commit": "c3280da26d2bf0a5a44dfcddc9105180bf3d4267",
        "methodology": "0.2",
        "replacement": (
            "Select and record the methodology version before reading the publication critically. Use version 0.1 unless the user or a frozen calibration prompt explicitly selects another version.",
            "This version-specific package is fixed to methodology 0.2. Treat the included 0.1 materials only as the retained base required by 0.2; do not select 0.1 as the active version.",
        ),
    },
    "0.3.0": {
        "source_commit": "714a5979e52f889671ba52f376824990549da013",
        "methodology": "0.3",
        "replacement": (
            "Select and record the methodology version before reading the publication critically. Use version 0.3 unless the user or a frozen calibration prompt explicitly selects another version.",
            "This version-specific package is fixed to methodology 0.3. Do not select or combine rules from another version.",
        ),
    },
}

PACKAGE_NAME = "assess-accessibility-articles"


def run(*args: str, cwd: Path) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def check_relative_links(skill_dir: Path) -> None:
    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", skill_text)
    missing = [link for link in links if "://" not in link and not (skill_dir / link).exists()]
    if missing:
        raise RuntimeError(f"Missing files referenced by SKILL.md: {missing}")


def write_deterministic_zip(source_dir: Path, destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source_dir.rglob("*")):
            if not path.is_file():
                continue
            relative = Path(PACKAGE_NAME) / path.relative_to(source_dir)
            info = zipfile.ZipInfo(str(relative), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())


def build(repo: Path, output_dir: Path, version: str) -> tuple[Path, str]:
    release = RELEASES[version]
    with tempfile.TemporaryDirectory(prefix=f"skill-{version}-") as temp_name:
        temp = Path(temp_name)
        archive_path = temp / "source.tar"
        with archive_path.open("wb") as archive:
            subprocess.run(
                ["git", "archive", release["source_commit"], "skill"],
                cwd=repo,
                check=True,
                stdout=archive,
            )
        run("tar", "-xf", str(archive_path), "-C", str(temp), cwd=repo)

        skill_dir = temp / "skill"
        skill_path = skill_dir / "SKILL.md"
        skill_text = skill_path.read_text(encoding="utf-8")
        old, new = release["replacement"]
        if old not in skill_text:
            raise RuntimeError(f"Expected version marker not found for {version}")
        skill_path.write_text(skill_text.replace(old, new, 1), encoding="utf-8")

        metadata_path = skill_dir / "agents" / "openai.yaml"
        metadata = metadata_path.read_text(encoding="utf-8")
        metadata = "\n".join(
            line for line in metadata.splitlines() if "icon_small:" not in line and "icon_large:" not in line
        ) + "\n"
        metadata_path.write_text(metadata, encoding="utf-8")

        shutil.copy2(repo / "LICENSE.md", skill_dir / "LICENSE.md")
        (skill_dir / "licenses").mkdir(exist_ok=True)
        shutil.copy2(repo / "licenses" / "MIT.txt", skill_dir / "licenses" / "MIT.txt")

        manifest = {
            "name": PACKAGE_NAME,
            "version": version,
            "status": "experimental-frozen",
            "methodology_version": release["methodology"],
            "source_commit": release["source_commit"],
            "licenses": {
                "text_and_methodology": "CC-BY-4.0",
                "code_and_technical_files": "MIT",
            },
            "packaging_adjustments": [
                "The active methodology version is explicit in SKILL.md.",
                "References to icon files absent from the historical source were removed.",
                "License files and this release manifest were added.",
            ],
        }
        (skill_dir / "RELEASE-MANIFEST.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

        check_relative_links(skill_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        destination = output_dir / f"{PACKAGE_NAME}-v{version}.zip"
        write_deterministic_zip(skill_dir, destination)

    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    checksum_path = destination.with_suffix(destination.suffix + ".sha256")
    checksum_path.write_text(f"{digest}  {destination.name}\n", encoding="utf-8")
    return destination, digest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("versions", nargs="*", choices=sorted(RELEASES))
    parser.add_argument("--output", type=Path, default=Path("dist"))
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    versions = args.versions or sorted(RELEASES)
    for version in versions:
        destination, digest = build(repo, args.output, version)
        print(f"{destination}: {digest}")


if __name__ == "__main__":
    main()
