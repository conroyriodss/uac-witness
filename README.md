# UAC evaluation witness records

This repository publishes records of SHA-256 digests, byte counts, and seal-log state for the related [UAC NITRD evaluation workflow](https://github.com/conroyriodss/uac-nitrd). The [NITRD Categorization MCP Suite](https://github.com/conroyriodss/nitrd-categorization-mcp) provides the broader submission map.

**Repository role: a separate record of declared artifact states.** It is not an application, an answer-key distribution, or an independent certification of the evaluation.

## Records

|Record|Recorded event|
|-|-|
|[0001](records/0001-pre-amendment-baseline.json)|Baseline before the recorded seal-log amendment.|
|[0002](records/0002-post-amendment-lines-29-31.json)|State after the recorded amendment of seal-log lines 29–31.|
|[0003](records/0003-correction-pcc-history-rewrite.json)|Correction: the single sanctioned history rewrite of uac-nitrd (2026-11-04), which removed the non-public PCC column from the FY2025 fixture. Gives the superseded and corrected fixture hashes and the full old→new commit map (43 commits plus the moved `uac-nitrd-freeze-v1` tag). It has no `files` mapping or seal-log summary.|
|[0004](records/0004-task1-preregistration-freeze.json)|Freeze: the Task 1 pre-registration (`task1-prereg-v1-2026-11-04T18:00:50Z`), with its SHA-256 and commit, the FY2024 freeze-run ranking, the FY2026 forecast and the zero-count check that was in force at the freeze.|
|[0005](records/0005-task1-tier2-fy2024-reveal.json)|Reveal: the single opening of the FY2024 key and its has_any_category supplement by the Tier 2 scoring run, the order of events, and the hashes of the inputs, rankings and results.|
|[0006](records/0006-task1-fy2026-forecast-bias-prediction.json)|Secondary prediction, **not pre-registered** (2026-11-05). It is estimated from the exposed years FY2022-25 and predicts that the FY2026 count forecast (3,326) comes in low, with an error between -13% and -2%. It is scored against the category-329 count over the forecast's 56,508 snapshot appl_ids. It does not change record 0004.|
|[0007](records/0007-task1-tier1c-denominator-clarification.json)|Clarification, made after the freeze while FY2026 category-329 was still 0 (owner decision, 2026-11-05). It fixes an ambiguity the frozen pre-registration left open. Tier 1c is scored against the category-329 count over the 56,508 snapshot appl_ids in `forecast.csv.gz`. The full-universe count and the post-snapshot additions are reported but not scored. It quotes the ambiguous clauses and does not change record 0004.|
|[0008](records/0008-correction-0006-at-utc-and-zero-count-log-method.json)|Correction, with two items. (1) Record 0006 declared `at_utc` 22:05:00, but its commit landed at 22:02:45; it is corrected by a new record, so 0006's bytes are kept. (2) Disclosure: the FY2026 zero-count log on the UC volume is rewritten with its old bytes preserved, not truly appended, because the volume does not support append. The record gives prefix-hash checks for both rewrites.|
|[0009](records/0009-correction-0008-at-utc.json)|Correction: record 0008 declared `at_utc` 22:12:00, but its commit landed at 22:11:31, the same defect it was correcting. It is corrected by a new record, so 0008's bytes are kept.|

Each state record (0001, 0002) contains an event description and recorded UTC time; a `files` mapping of logical artifact names to byte counts and SHA-256 digests; a seal-log summary; and a witness identifier. Logical artifact paths refer to the source environment, not necessarily files in this repository.

## What a comparison establishes

Given the exact original artifact bytes and the applicable record, a reader can compare byte counts and hashes. Agreement supports that the supplied bytes match the recorded state. A later record can document an amendment while preserving the earlier statement.

These comparisons do not establish the truth of an artifact’s contents, that a prediction was generated independently of its labels, that every relevant event was recorded, or that access controls prevented all possible access. The witness repository has the same GitHub owner as the related project; it provides separation of records, not independent institutional custody.

The `at\_utc` field is a recorded assertion. Git commit dates alone are not independent proof of publication time. Assess ordering using retained GitHub/server records and the broader protocol evidence where available.

## Verification route

1. Choose the event and pin this repository to the commit containing the applicable record.
2. Identify the exact logical artifact name under `files`.
3. Obtain the corresponding bytes through the workflow’s authorized release or review process. Do not open a sealed answer key before its protocol-authorized reveal.
4. Compute the local file’s byte length and SHA-256; compare both with the record. Do not normalize line endings, parse/reserialize JSON, or otherwise transform the file first.
5. Record the witness commit, record filename, logical artifact name, and comparison result. Investigate a mismatch rather than replacing the earlier recorded digest.

Some referenced artifacts remain outside the public repositories. When the bytes are unavailable, their recorded hashes can be inspected but the underlying files cannot yet be independently matched. Distinguish that missing access from a successful verification.

## Record changes

Treat existing records as historical statements. Add a new numbered record for a later event or correction, identify the earlier record, and explain the change. Preserve the original JSON bytes. Documentation changes can use ordinary pull requests; record additions should explain their source event and evidence.

This convention is a maintenance policy. Its presence in a README does not establish that repository settings or automated checks enforce it.

## Questions and reuse

Use [issues](https://github.com/conroyriodss/uac-witness/issues) for questions about record interpretation or discrepancies, citing the witness commit and record filename. Do not post sealed keys or nonpublic source artifacts.

No project-wide LICENSE file is currently included. Determine the appropriate reuse terms separately from verification of the recorded digests.

