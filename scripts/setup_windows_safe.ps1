Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Invoke-NativeStep {
    param(
        [string]$Description,
        [scriptblock]$Command
    )

    Write-Host "==> $Description"
    & $Command
    if ($LASTEXITCODE -ne 0) {
        throw "$Description failed with exit code $LASTEXITCODE"
    }
}

Write-Host "==> Checking for winget..."
if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    throw "winget was not found. Install App Installer / winget first, then rerun."
}

Invoke-NativeStep "Installing Python 3.12 with winget" {
    winget install --id Python.Python.3.12 -e --accept-package-agreements --accept-source-agreements
}

Invoke-NativeStep "Installing FFmpeg with winget" {
    winget install --id Gyan.FFmpeg -e --accept-package-agreements --accept-source-agreements
}

Invoke-NativeStep "Installing MiKTeX with winget" {
    winget install --id MiKTeX.MiKTeX -e --accept-package-agreements --accept-source-agreements
}

Write-Host "==> Creating virtual environment..."
if (-not (Test-Path ".venv")) {
    try {
        & py -3.12 -m venv .venv
    }
    catch {
        & py -3 -m venv .venv
    }
    if ($LASTEXITCODE -ne 0) {
        throw "Virtual environment creation failed."
    }
}

Write-Host "==> Activating virtual environment..."
& .\.venv\Scripts\Activate.ps1

$env:PIP_NO_CACHE_DIR = "1"
$env:PIP_CACHE_DIR = "$PWD\.pip-cache"

Invoke-NativeStep "Upgrading pip, setuptools, and wheel" {
    python -m pip install --upgrade pip setuptools wheel --no-cache-dir
}

Invoke-NativeStep "Installing repository requirements" {
    python -m pip install --no-cache-dir -r requirements.txt
}

if (Test-Path "requirements-dev.txt") {
    Invoke-NativeStep "Installing development requirements" {
        python -m pip install --no-cache-dir -r requirements-dev.txt
    }
}

Invoke-NativeStep "Verifying Manim installation" {
    python -m manim --version
}

Write-Host "==> Setup complete."
Write-Host "Activate with: .\.venv\Scripts\Activate.ps1"
Write-Host "Preview render: .\scripts\render_preview_safe.ps1"
Write-Host "Final render: .\scripts\render_final_safe.ps1"
