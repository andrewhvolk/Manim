# End-to-End Production Workflow for 28 Videos (Render -> Voiceover -> YouTube)

This guide provides a detailed, repeatable process for evaluating all 28 planned videos and preparing each one for upload to YouTube.

## 1) Scope and assumptions

- Video source scenes are `v01` through `v28`.
- Audience is undergraduate-level math students.
- Each video passes a staged quality process before upload.
- Voiceover is produced externally and merged during post-production.

## 1.5) Work you can do before rendering starts

Complete these setup tasks first so production is not blocked later:

1. Create the tracker CSV and prefill all 28 rows (`V01` to `V28`).
2. Prefill each row with:
   - `video_id`
   - `topic_title`
   - `scene_file`
   - `scene_class`
   - initial `target_runtime_sec`
3. Assign owners and target due dates for each batch.
4. Create reusable metadata templates:
   - title pattern
   - description skeleton
   - hashtag/tag set
5. Create a standard branded intro/outro asset set and file naming convention.
6. Create a thumbnail text pattern and visual style rules.
7. Prepare a shared voiceover recording checklist and audio export settings.

Starter file in this repository:

`assets/data/production/math130_test3_tracker.csv`

## 2) Master tracking sheet structure

Create one tracker file at:

`assets/data/production/math130_test3_tracker.csv`

Use one row per video (`V01` ... `V28`) and the following columns:

### Core metadata

- `video_id` (e.g., `V01`)
- `topic_title`
- `target_runtime_sec`
- `scene_file`
- `scene_class`
- `owner`
- `due_date`

### Production status columns

Use `not_started`, `in_progress`, `blocked`, or `done`.

- `script_outline`
- `preview_render`
- `math_qa`
- `visual_qa`
- `timing_lock`
- `voiceover_script`
- `voiceover_recorded`
- `voiceover_edited`
- `intro_outro_added`
- `title_card_added`
- `description_draft`
- `thumbnail_ready`
- `final_render`
- `final_qc`
- `youtube_metadata_ready`
- `upload_ready`
- `uploaded`

### QA notes columns

- `blocking_issue`
- `math_notes`
- `audio_notes`
- `visual_notes`
- `revision_round` (integer)
- `last_updated`

## 3) Batch cadence for all 28 videos

Process in five batches:

- Batch 1: `V01`–`V05`
- Batch 2: `V06`–`V11`
- Batch 3: `V12`–`V18`
- Batch 4: `V19`–`V24`
- Batch 5: `V25`–`V28`

Rule: do not advance to the next batch until at least 80% of current-batch videos are `final_qc=done`.

## 4) Step-by-step lifecycle for each video

## Step A: pre-production

1. Confirm learning objective, target runtime, and one worked example.
2. Draft a short narration script:
   - Hook (1 line)
   - Setup (definitions/givens)
   - Solve/explain (core steps)
   - Check/interpretation
   - Closing takeaway
3. Mark `script_outline=done` and `voiceover_script=in_progress`.

## Step B: technical preview render

1. Render preview (`-pql`).
2. Verify no Python/Manim errors.
3. Check layout readability on a laptop-sized screen.
4. Mark `preview_render=done` only when text and animations are legible.

## Step C: math + visual QA round

1. Math QA checklist:
   - notation correctness;
   - equation transformations valid;
   - labels and units correct.
2. Visual QA checklist:
   - no text overlap;
   - pacing is understandable;
   - color highlights are consistent.
3. Log issues in `math_notes` / `visual_notes`.
4. Increment `revision_round` if any issue requires code changes.

## Step D: timing lock

1. Re-render preview after fixes.
2. Confirm target runtime window (typically ±10 seconds).
3. Freeze major animation timing.
4. Mark `timing_lock=done`.

## Step E: voiceover production

1. Finalize narration script from timing-locked preview.
2. Record raw VO in a quiet environment.
3. Edit audio:
   - remove noise;
   - normalize loudness;
   - reduce harsh breaths/plosives.
4. Sync VO to scene timing and mark:
   - `voiceover_recorded=done`
   - `voiceover_edited=done`
5. Log retake lines in `audio_notes`.

## Step F: branding + titling pass

For every video, add:

1. **Branded intro** (short, consistent opening animation).
2. **Title card** with lesson name and numbering (`V##`).
3. **Branded outro** with CTA (subscribe / next lesson link placeholder).

Then mark:

- `intro_outro_added=done`
- `title_card_added=done`

## Step G: final render and QC

1. Render final-quality video (`-pqh`).
2. QC checklist before upload:
   - audio-video sync;
   - no clipping or cut-off text;
   - no math mistakes;
   - intro/outro present;
   - correct title card.
3. Mark `final_render=done` and then `final_qc=done`.

## Step H: YouTube packaging

1. Prepare upload title.
2. Prepare description with:
   - lesson objective;
   - key formulas;
   - timestamps;
   - short practice prompt;
   - links/playlists.
3. Add keywords/tags and playlist mapping.
4. Validate thumbnail and mark:
   - `description_draft=done`
   - `youtube_metadata_ready=done`
   - `upload_ready=done`

## 5) Iterative revision loop (required)

Use this loop until `final_qc=done`:

1. Review latest render with checklist.
2. Categorize issue as `math`, `visual`, `timing`, `audio`, or `branding`.
3. Apply one focused change set.
4. Re-render preview (or final if change is post-production only).
5. Re-check and update tracker notes.

Stop condition: two consecutive reviews with no blocking issues.

## 6) Suggested quality gates

A video cannot move forward unless these gates pass:

- Gate 1 (Technical): preview render succeeds.
- Gate 2 (Teaching): math + pacing reviewed by a second reader.
- Gate 3 (Audio): narration is clear and level.
- Gate 4 (Brand): intro, title card, and outro are consistent.
- Gate 5 (Publishing): metadata complete and thumbnail approved.

## 7) YouTube title template and description template

## Title template

`[Course/Topic] | V##: [Specific Concept] | Worked Example`

Example:

`Trigonometry Review | V14: Solve a Right Triangle | Worked Example`

## Description template

```text
In this lesson (V##), we cover: [concept].

What you'll learn:
- [objective 1]
- [objective 2]

Key formulas:
- [formula 1]
- [formula 2]

Timestamps:
00:00 Intro
00:15 Concept setup
01:05 Worked example
02:10 Final check

Practice:
Try this: [one short practice prompt]

Playlist:
[playlist URL]

#math #manim #[topic]
```

## 8) Weekly operating rhythm

Use a weekly cycle:

- Monday: script + preview targets.
- Tuesday: math/visual QA and revisions.
- Wednesday: timing lock and VO recording.
- Thursday: VO edit, branding, title cards.
- Friday: final renders + QC.
- Saturday: metadata + scheduled uploads.
- Sunday: retrospective and next-batch planning.

## 9) Definition of done (per video)

A video is complete only when all are true:

- `final_qc=done`
- `youtube_metadata_ready=done`
- `upload_ready=done`
- thumbnail approved
- no open blocking issue in tracker

## 10) Repository notes

- Keep source scenes in `scenes/`.
- Keep reusable assets in `assets/`.
- Keep generated media in `media/`.
- Keep process docs in `docs/`.
