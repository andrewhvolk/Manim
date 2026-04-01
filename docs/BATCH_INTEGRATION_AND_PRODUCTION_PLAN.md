# Batch Integration and Production Plan (Manim + Voiceover)

This plan reviews the current `manim/` batch and proposes a practical way to integrate it into the repository's teaching workflow.

## 1) What is already in your batch

The `manim/` folder already contains a complete 28-video sequence (`v01` through `v28`) plus shared style helpers and planning docs:

- 28 scene files: `manim/v01_...py` through `manim/v28_...py`
- shared visual and scene-construction helpers in `manim/style/`
- production and QA tracking docs in `manim/VIDEO_MASTER_PLAN_28.md`, `manim/MANIM_PROGRESS_ORCHESTRATOR.md`, and `manim/MATH_QA_REPORT.md`

This is a strong starting point because your math QA is already documented and the scene architecture is consistent.

## 2) Recommended repository organization

Keep your current files for safety, then migrate in a structured way.

### Target layout for this batch

```text
scenes/
  math130_test3/
    v01_coterminal_deg.py
    ...
    v28_capstone_review.py
    style/
      components.py
      scene_factory.py

assets/
  audio/
    math130_test3/
      raw/
      edited/
      final/
  data/
    production/
      math130_test3_tracker.csv
  images/
    math130_test3/

docs/
  production/
    math130_test3/
      run_order.md
      voiceover_script.md
      pickup_lines.md
```

### Why this organization

- Keeps course-specific content isolated (`math130_test3`) so you can add future courses cleanly.
- Separates source scenes from production assets and narration deliverables.
- Makes it easy to track completion state outside generated `media/` outputs.

## 3) Integration sequence (safe and incremental)

1. **Freeze current batch as source of truth**
   - Keep `manim/` unchanged until first migrated render passes.
2. **Create destination course folder in `scenes/`**
   - Add `scenes/math130_test3/` and move/copy files in small groups (first 3 videos).
3. **Fix imports after move**
   - Ensure `from style...` paths still resolve (either local package style or relative import strategy).
4. **Render pilot set**
   - Render V01–V03 in preview and final quality.
5. **Validate media + narration timing**
   - Confirm pacing target before migrating the rest.
6. **Migrate remaining scenes in topic blocks**
   - Angles/trig basics (V01–V13), applications (V14–V19), vectors (V20–V28).

## 4) Render progression strategy

Use a staged pipeline so you avoid doing full exports too early.

### Stage A: Technical validation
- Render all videos at preview quality (`-pql`) for syntax/layout checks.
- Goal: zero render errors and no clipped text.

### Stage B: Timing lock
- Re-render previews after pacing edits.
- Lock each video's approximate duration target.

### Stage C: Final export
- Export only approved videos at final quality (`-pqh`) in batches of 3–5.
- Keep export naming consistent with your standard (e.g., `V##_topic_1080p.mp4`).

## 5) Voiceover workflow (after timing lock)

Do voiceover after preview timing is stable, before bulk final exports.

### Per-video VO checklist
1. Draft script from scene text (Goal -> Setup -> Solve -> Check).
2. Time script to preview video and trim to fit natural pauses.
3. Record raw take.
4. Edit (noise reduction, leveling, de-breath if needed).
5. Align VO to visuals.
6. Note pickup lines in a running list (`pickup_lines.md`).
7. Re-export final video once VO and scene timing both pass.

### Recommended batch cadence
- **Batch 1:** V01–V05
- **Batch 2:** V06–V11
- **Batch 3:** V12–V18
- **Batch 4:** V19–V24
- **Batch 5:** V25–V28

This mirrors your existing orchestrator cadence and minimizes context switching.

## 6) Practical production controls

For each video, track these statuses in one CSV or sheet:

- `scene_preview_pass`
- `math_qa_pass`
- `visual_qa_pass`
- `script_locked`
- `vo_recorded`
- `vo_edited`
- `final_export`
- `final_qc`

Use one owner and one due date per status to keep momentum.

## 7) Immediate next steps

1. Create `scenes/math130_test3/` and copy V01–V03 + `style/` there.
2. Run preview render for V01–V03.
3. Adjust text spacing/animation timing only.
4. Draft and record VO for V01 first.
5. Approve one full end-to-end video (scene + VO + final export) as the production template.
6. Scale to the remaining videos in batches.

## 8) Assumptions and dependencies

- Assumes local Manim dependencies (FFmpeg and LaTeX toolchain) are available.
- Assumes narration is recorded outside Manim and merged during post-production.
- Assumes `media/` remains generated output and not the main progress tracker.
