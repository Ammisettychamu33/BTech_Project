# PowerShell script to create and activate a virtual environment and install requirements
# Usage: Open PowerShell in the project root and run: .\scripts\setup_env.ps1

# Create virtual environment
python -m venv .venv

# Activate (PowerShell)
if (Test-Path ".\.venv\Scripts\Activate.ps1") {
    Write-Host "Activating .venv (PowerShell)"
    & ".\.venv\Scripts\Activate.ps1"
} else {
    Write-Host "Activation script not found. Activate manually: .\.venv\Scripts\Activate.ps1"
}

# Upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Setup complete. Activate your venv with: .\.venv\Scripts\Activate.ps1"