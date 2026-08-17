---
name: assess-accessibility-articles
description: Systematically assess the reliability, accuracy, clarity, evidence, and practical safety of articles, guides, commentary, newsletters, and other publications about accessibility. Use when Codex must review a complete accessibility-related publication, verify its legal, normative, technical, or user-research claims against authoritative sources, produce comparable 0–4 scores and a descriptive verdict, analyze whether the intended audience can understand it, or run a frozen-method calibration series across multiple publications.
---

# Assess accessibility articles

Apply one fixed, evidence-led workflow to every publication. Evaluate the publication, not the author.

## Load the governing materials

Select and record the methodology version before reading the publication critically. Use version 0.1 unless the user or a frozen calibration prompt explicitly selects another version.

For version 0.1:

- read [references/standard.md](references/standard.md) completely;
- use [references/wzor-raportu.md](references/wzor-raportu.md) for the full report;
- use [references/karta-oceny.md](references/karta-oceny.md) for the score profile.

For the 0.2 draft:

- first read the complete 0.1 standard as the retained base;
- then read [references/standard-0.2-projekt.md](references/standard-0.2-projekt.md) and treat it as controlling where the versions differ;
- read [references/kotwice-0.2.md](references/kotwice-0.2.md) completely before scoring;
- use [references/wzor-raportu-0.2.md](references/wzor-raportu-0.2.md) and [references/karta-oceny-0.2.md](references/karta-oceny-0.2.md);
- validate structured outputs against [references/wynik-0.2.schema.json](references/wynik-0.2.schema.json) and, for calibration work, [references/wyciag-kalibracyjny-0.2.schema.json](references/wyciag-kalibracyjny-0.2.schema.json).
- run `python3 scripts/validate_0_2.py result wynik.json` and, when applicable, `python3 scripts/validate_0_2.py extract wyciag-kalibracyjny.json` before saving or returning files.

Never silently substitute one version for another. Treat the detailed standard and its version-specific overlay as authoritative if this file differs from them.

## Freeze the method

Record the methodology version and, when available, its source commit before reading the publication critically. Do not change criteria, anchors, weights, verdict rules, or output vocabulary during an analysis or a calibration series.

Also record the evaluator environment as far as it is knowable: evaluator type, model or reviewer name, model snapshot or version, reasoning setting, available tools, analysis date, and whether memory, project context, or private repositories were available. Write `not_available` instead of guessing.

When evaluating a predefined calibration set:

1. Fix the article list and order before scoring.
2. Complete each article as a separate case.
3. Do not use one article's score to raise or lower another article's score.
4. Record suspected methodology defects separately without applying them to later cases.
5. Compare cases and propose revisions only after the entire set is complete.

## Acquire and delimit the material

1. Open the supplied publication and obtain its complete available content, including relevant tables, code, images, footnotes, attachments, and linked material that forms part of the argument.
2. Record title, author, URL, dates, language, publication type, outlet, declared audience, purpose, and completeness.
3. Inspect the outlet's about page or equivalent only to establish audience, purpose, and editorial context.
4. Separate the main article from newsletters, advertisements, event notices, and unrelated roundups. State which sections affect the main score.
5. Classify each inspected item as main content, central external material, additional material, or excluded material.
6. For every central external material, record its exact URL, access date, and an immutable identifier such as a commit, release, document version, or archived snapshot when available. If no immutable identifier exists, state that explicitly.
7. If the full material is unavailable, mark the assessment partial and do not infer missing content.
8. Do not store or reproduce a full copyrighted article unless the user has a lawful basis and explicitly requests storage. Prefer a URL, metadata, short quotations, and faithful paraphrases.

## Perform two independent passes

### Pass 1: interpret

Before checking truth:

- prepare a neutral summary;
- identify the intended audience and assumed knowledge;
- state the author's purpose and main conclusion;
- distinguish information, instruction, legal commentary, opinion, personal experience, and promotion;
- list the strongest reasonable version of the main claims.

Do not let later discoveries rewrite the neutral summary.

### Pass 2: verify and assess

Build a claim map covering every statement material to the conclusion or likely reader action. Assign each claim the categories and fields required by the standard.

Verify claims using sources appropriate to the claim:

1. current legislation, official journals, and judgments;
2. standards and specifications from their issuing bodies;
3. official explanations and implementation techniques;
4. product documentation for declared behavior;
5. peer-reviewed studies and adequately documented user research;
6. representative user organizations and strong expert literature.

Open and read the supporting section. Do not treat search snippets as evidence. For technical, legal, financial, medical, standards, or current claims, browse current primary sources by default. Record the access date and relevant version.

For each claim, distinguish:

- a binding requirement from guidance, a sufficient technique, or a preference;
- a factual error from simplification, omission, ambiguity, interpretation, opinion, and unresolved evidence;
- normative wording from implementation advice;
- tested behavior in one environment from universal behavior;
- an individual account from evidence about a population.

## Assess language and audience comprehension

Analyze comprehension separately from factual correctness. Examine:

- unexplained terminology and assumed domain knowledge;
- sentence and paragraph structure;
- argument order and transitions;
- headings, lists, examples, metaphors, irony, and digressions;
- ambiguity between related technical concepts;
- whether code and examples are syntactically valid and safe to copy;
- whether each declared audience subgroup can follow the reasoning and act safely.

Give one main score relative to the outlet's declared audience. Also state briefly when comprehension differs materially between subgroups, such as developers, coordinators, auditors, and users of assistive technologies.

## Score without averaging away the profile

Score all twelve dimensions from 0 to 4 using the anchors in the standard. Justify each score with article-specific evidence. Do not calculate or present a weighted total unless weights were fixed before seeing the article.

When using the 0.2 draft, use `nd` only under its strict applicability rule and justify every `nd`. Before finalizing each numeric score, compare the evidence with both adjacent anchors. For every score of 0, 1, or 4, name the evidence that crosses the relevant boundary. Do not normalize scores merely to make a series look consistent.

Assign problem severity and confidence separately. Under the 0.2 draft, also assign centrality and application risk to every large or critical problem. Determine the verdict with the version-specific decision sequence and counterfactual-correction test; do not infer it from a sum, average, or raw problem count. Explain whether the material can be recommended:

- without qualification;
- only with named corrections or supplementary sources;
- not for practical use.

## Produce and store outputs

Produce three case files when persistent comparison is requested:

- `metryka.yaml` — publication, method, scope, and limitations;
- `analiza.md` — the full human-readable report in the required order;
- `wynik.json` — scores, claim results, severities, verdict, confidence, sources, and limitations.

Use stable identifiers and closed vocabulary consistently. Validate JSON and YAML before saving.

For a 0.2 calibration case, always produce both:

- the complete report;
- a compact calibration extract conforming to the 0.2 calibration schema.

When the result is delivered only in chat, put the compact extract in one complete JSON code block so it can be copied without reconstructing the full report. Do not require repository access and do not write to a repository unless the user explicitly authorizes it.

If the user has designated a private analysis repository, save each case under a unique dated directory there. Do not place article copies or sensitive working material in a public methodology repository. Save general methodology observations separately from the case report.

## Report progress during long work

When the user requests ongoing updates, report at least these milestones:

1. full text obtained and scope fixed;
2. interpretive pass complete;
3. claim map complete and source verification underway;
4. scoring and verdict complete;
5. files validated and saved;
6. transition to the next case.

Keep updates concise and do not announce a conclusion before the evidence pass is complete.
