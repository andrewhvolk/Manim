param(
    [string]$SceneFile = "scenes/lesson_001_intro.py",
    [string]$SceneClass = "Lesson001Intro"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not (Test-Path ".venv\Scripts\Activate.ps1")) {
    throw "The virtual environment was not found. Run scripts/setup_windows_safe.ps1 first."
}

& .\.venv\Scripts\Activate.ps1
python -m manim -pql $SceneFile $SceneClass
if ($LASTEXITCODE -ne 0) {
    throw "Preview render failed with exit code $LASTEXITCODE"
}
