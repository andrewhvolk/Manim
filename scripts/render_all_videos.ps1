param(
    [ValidateSet("l", "m", "h", "k")]
    [string]$Quality = "h",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "python was not found on PATH. Activate your .venv first."
}

$files = Get-ChildItem -Path "manim" -Filter "v*.py" | Sort-Object Name

foreach ($file in $files) {
    $classLine = Select-String -Path $file.FullName -Pattern '^class\s+([A-Za-z_][A-Za-z0-9_]*)\(Scene\):' | Select-Object -First 1

    if (-not $classLine) {
        Write-Error "Could not find a Scene class in $($file.FullName)"
    }

    $sceneClass = $classLine.Matches[0].Groups[1].Value
    $args = @("-m", "manim", "-q$Quality", $file.FullName, $sceneClass)

    Write-Host "Rendering $($file.FullName) :: $sceneClass"
    Write-Host "+ python $($args -join ' ')"

    if (-not $DryRun) {
        & python @args
    }
}

Write-Host "Done. Rendered outputs are in media/ (git-ignored)."
