@echo off
REM Batch script to create a venv and install requirements (Windows)
REM Usage: run from project root: scripts\setup_env.bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo Setup complete. Activate with: .venv\Scripts\activate