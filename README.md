# BTech_Project

Seismic event prediction front-end and model server.

## Quick start (Windows) ✅

1. Clone the repo (already done for you):
   ```powershell
   git clone https://github.com/Ammisettychamu33/BTech_Project.git
   cd BTech_Project
   ```

2. Create and activate a virtual environment and install dependencies:
   - Option A (PowerShell script):
     ```powershell
     .\scripts\setup_env.ps1
     ```
   - Option B (manually):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     python -m pip install --upgrade pip
     pip install -r requirements.txt
     ```

3. Run the Flask server:
   ```powershell
   python app.py
   ```
   The API will be available at http://127.0.0.1:5000/predict

## Notes
- The project includes `eq_model.h5` (model file). It is small (~0.75 MB) and included in the repo.
- Avoid committing virtual environments: `.venv/` and `backend/venv/` are in `.gitignore`.
- If you run into large-file errors when pushing to GitHub, consider using Git LFS for very large models or removing vendor binaries.

## Next steps
- Add a `README` section documenting the API (input/output schema). I can add that if you want.
- I can also add a `.github/workflows/` CI file to run tests / linting.

---
Created and updated by GitHub Copilot (Raptor mini Preview).
