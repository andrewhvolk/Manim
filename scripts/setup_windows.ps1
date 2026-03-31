Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Write-Host "==> Checking for winget..."
if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    throw "winget was not found. Install App Installer / winget first, then rerun."
}

Write-Host "==> Installing system dependencies with winget..."
# If a package ID fails on your machine, run winget search <name> and substitute the result.
winget install --id Python.Python.3.12 -e --accept-package-agreements --accept-source-agreements
winget install --id Gyan.FFmpeg -e --accept-package-agreements --accept-source-agreements
winget install --id MiKTeX.MiKTeX -e --accept-package-agreements --accept-source-agreements

Write-Host "==> Creating virtual environment..."
if (-not (Test-Path ".venv")) {
    py -3.12 -m venv .venv
}

Write-Host "==> Activating virtual environment..."
& .\.venv\Scripts\Activate.ps1

Write-Host "==> Upgrading pip..."
python -m pip install --upgrade pip

Write-Host "==> Installing repo requirements..."
python -m pip install -r requirements.txt

if (Test-Path "requirements-dev.txt") {
    python -m pip install -r requirements-dev.txt
}

Write-Host "==> Verifying installs..."
python --version
ffmpeg -version
python -m manim --version

Write-Host "==> Setup complete."
Write-Host "Run a test render with:"
Write-Host "python -m manim -pql scenes/lesson_001_intro.py Lesson001Intro"
