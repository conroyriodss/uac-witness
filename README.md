# UAC evaluation witness records

This repository publishes records of SHA-256 digests, byte counts, and seal-log state for the related [UAC NITRD evaluation workflow](https://github.com/conroyriodss/uac-nitrd). The [NITRD Categorization MCP Suite](https://github.com/conroyriodss/nitrd-categorization-mcp) provides the broader submission map.

**Repository role: a separate record of declared artifact states.** It is not an application, an answer-key distribution, or an independent certification of the evaluation.

## Records

|Record|Recorded event|
|-|-|
|[0001](records/0001-pre-amendment-baseline.json)|Baseline before the recorded seal-log amendment.|
|[0002](records/0002-post-amendment-lines-29-31.json)|State after the recorded amendment of seal-log lines 29–31.|

Each JSON record contains an event description and recorded UTC time; a `files` mapping of logical artifact names to byte counts and SHA-256 digests; a seal-log summary; and a witness identifier. Logical artifact paths refer to the source environment, not necessarily files in this repository.

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

