# Setup

This repository targets Manim Community in an isolated Python environment.

## Preferred setup with `uv`

### macOS/Linux

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Windows PowerShell

```powershell
uv venv
.\.venv\Scripts\Activate.ps1
uv pip install -r requirements.txt
```

## Fallback setup with `venv` + `pip`

### macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Machine-level dependencies

Manim also depends on local system packages such as FFmpeg. Full LaTeX rendering may require a TeX distribution.
