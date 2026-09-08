---
name: assess-accessibility-articles
description: Systematically assess the reliability, accuracy, clarity, evidence, and practical safety of articles, guides, commentary, newsletters, and other publications about accessibility. Use when Codex must review a complete accessibility-related publication, verify its legal, normative, technical, or user-research claims against authoritative sources, produce comparable 0–4 scores and a descriptive verdict, analyze whether the intended audience can understand it, or run a frozen-method calibration series across multiple publications.
---

# Assess accessibility articles

Apply one fixed, evidence-led workflow to every publication. Evaluate the publication, not the author.

## Load the governing materials

Select and record the methodology version before reading the publication critically. Use version 0.1 unless the user or a frozen calibration prompt explicitly selects another version. Never combine rules from different versions.

For version 0.1:

- read [references/standard.md](references/standard.md) completely;
- use [references/wzor-raportu.md](references/wzor-raportu.md) and [references/karta-oceny.md](references/karta-oceny.md).

For version 0.2 draft:

- read the complete 0.1 standard as its retained base;
- read [references/standard-0.2-projekt.md](references/standard-0.2-projekt.md), then [references/kotwice-0.2.md](references/kotwice-0.2.md);
- use [references/wzor-raportu-0.2.md](references/wzor-raportu-0.2.md) and [references/karta-oceny-0.2.md](references/karta-oceny-0.2.md);
- validate data against [references/wynik-0.2.schema.json](references/wynik-0.2.schema.json) and [references/wyciag-kalibracyjny-0.2.schema.json](references/wyciag-kalibracyjny-0.2.schema.json);
- run `python3 scripts/validate_0_2.py result wynik.json` and, when applicable, `python3 scripts/validate_0_2.py extract wyciag-kalibracyjny.json`.

For version 0.3 draft:

- read the standalone [references/standard-0.3.md](references/standard-0.3.md) and [references/kotwice-0.3.md](references/kotwice-0.3.md) completely; do not load 0.1 or 0.2 as a base;
- use [references/wzor-raportu-0.3.md](references/wzor-raportu-0.3.md) and [references/karta-oceny-0.3.md](references/karta-oceny-0.3.md);
- validate data against [references/wynik-0.3.schema.json](references/wynik-0.3.schema.json) and [references/wyciag-kalibracyjny-0.3.schema.json](references/wyciag-kalibracyjny-0.3.schema.json);
- run `python3 scripts/validate_0_3.py result wynik.json` and, when applicable, `python3 scripts/validate_0_3.py extract wyciag-kalibracyjny.json`.

Treat the selected standard as authoritative if this file differs from it. The 0.3 materials are a public working draft, not a frozen release.

## Freeze the method and environment

Before the critical pass, record the selected methodology version and identifier. Also record the evaluator type, name or model, model snapshot, reasoning setting, tools, analysis date, and access to memory, project context, and private repositories. Use `not_available` instead of guessing.

Do not change criteria, anchors, verdict rules, or output vocabulary during an analysis or frozen calibration series. In a predefined series, fix the publication list and order first, keep cases separate, record suspected defects without applying them mid-series, and revise only after the series ends.

## Acquire and delimit the material

1. Obtain the complete available publication, including central tables, code, images, footnotes, attachments, and linked material on which the argument depends.
2. Verify the title, authorship or editorial signature, publisher, outlet, dates, language, type, purpose, audience, and completeness. Do not infer authorship from the domain alone.
3. Separate the main publication from advertisements, newsletters, event notices, and unrelated material.
4. Classify each inspected item using the selected standard's material roles. Record exact URLs, access dates, versions, and immutable identifiers when available.
5. If full material is unavailable, mark the assessment partial and do not infer missing content.
6. Do not reproduce a full copyrighted publication without a lawful basis and explicit request. Prefer metadata, short quotations, and faithful paraphrases.

## Perform two internal passes

### Pass 1: interpret

Before checking truth:

- prepare a neutral summary;
- identify the audience, assumed knowledge, purpose, promise, and main conclusion;
- distinguish information, instruction, legal commentary, opinion, experience, and promotion;
- state the strongest reasonable version of the main claims.

Do not let later findings rewrite this neutral summary.

### Pass 2: verify and assess

Build a claim map covering every statement material to the conclusion or likely reader action. For 0.3, split a statement whenever part of it could receive a different category, importance, result, or source set. Record confidence in the completeness of the claim map.

Verify claims against sources appropriate to their type, prioritizing:

1. legislation, official journals, and judgments;
2. standards and specifications from issuing bodies;
3. official explanations and implementation techniques;
4. product documentation for declared behavior;
5. peer-reviewed research and adequately documented user studies;
6. representative user organizations and strong expert literature.

Open and read the relevant source section. Do not use search snippets as evidence. Record access dates and versions. Separate historical accuracy at publication time from current applicability when law, standards, technology, or guidance changed later.

For each claim, distinguish requirements from guidance and preferences; errors from simplifications, omissions, interpretations, and unresolved evidence; tested behavior from universal claims; and individual experience from population evidence. Under 0.3, explain why the chosen result is more appropriate than the adjacent result category.

## Assess language for the actual audience

Establish the audience and language profile before assigning G, H, or L. Identify terms necessary to understand the core, their first use, whether they are explained or clear in context, and their effect on comprehension.

Keep the dimensions separate:

- G concerns correctness, precision, and consistency of terminology;
- H concerns whether the intended audience can follow the argument;
- L concerns whether the publication fulfils the promise of its format and outlet.

Do not penalize specialist vocabulary merely for being specialist. Apply the 0.3 score caps when unexplained core terminology blocks a substantial nonspecialist audience or defeats a declared popularizing purpose. State that this is an expert assessment unless user testing was performed.

## Group issues and determine the verdict

Do not turn every claim defect into a separate problem. Under 0.3, group defects only when they share one underlying cause, correction, and practical effect; otherwise keep them separate. Explain each grouping and propose a correction.

Assign severity and confidence separately. For every large or critical issue under 0.2 or 0.3, assign centrality and application risk. Under 0.3, explicitly perform both the centrality test and application-risk test required by the standard.

Score A–L from 0 to 4 or `nd` only where the selected version permits it. Compare each score with adjacent anchors. For 0, 1, or 4, identify the boundary-crossing evidence. Do not calculate a total or infer the verdict from an average or raw issue count.

Determine the descriptive verdict using the selected standard's decision sequence and counterfactual-correction test. State whether the publication is safe to recommend without qualification, only with named corrections or additional sources, or not for practical use.

## Produce and validate outputs

When persistent comparison is requested, produce:

- `metryka.yaml` — publication, method, environment, scope, and limitations;
- `analiza.md` — the complete human-readable report;
- `wynik.json` — the complete structured result;
- `wyciag-kalibracyjny.json` — the compact comparison record for 0.2 or 0.3 calibration work.

Use stable identifiers and the selected version's closed vocabulary. Run the matching validator before saving or returning structured files. A validator checks structure and internal consistency, not the truth of the assessment.

When the user designates an analysis repository, save each case under a unique dated directory. Do not place article copies, full case analyses, or private working material in a public methodology repository.

## Run independent calibration assessments

Two calibration assessments A and B must not know each other's result. If the environment can create isolated workers or contexts, the coordinating agent should run both assessments itself, preserve their isolation, validate the outputs, and then compare them. Do not require the user to copy prompts between empty chats when the environment can safely provide that isolation.

If isolated execution is unavailable, say so before starting and provide a reproducible handoff. Do not present two mutually informed passes as independent assessments.

## Report progress during long work

When ongoing updates are requested, report at least:

1. full text obtained and scope fixed;
2. interpretive pass complete;
3. claim map complete and verification underway;
4. scoring and verdict complete;
5. files validated and saved;
6. transition to the next case.

Keep updates concise and do not announce a conclusion before verification is complete.
