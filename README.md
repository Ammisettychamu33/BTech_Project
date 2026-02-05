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

## API — `/predict` (POST)

- **Endpoint**: `POST http://127.0.0.1:5000/predict`
- **Request body (JSON)**:
  ```json
  {
    "features": [ /* 900 numeric values */ ]
  }
  ```
  - The server expects exactly **900 numeric features** (the model reshapes this to `(1, 300, 3)`).

- **Response (JSON)**:
  ```json
  {
    "distance": 123.45,
    "magnitude": 4.5,
    "azimuth": 123.0,
    "depth": 10.0
  }
  ```
  - All four values are returned as floats.

- **Errors**:
  - `400 Bad Request` when the `features` array is missing or not length 900.
  - `500 Internal Server Error` on unexpected model/server errors.

- **Example (curl)**:
  ```bash
  curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [0,0,0, ..., 0]}"
  ```

- **Example (Python using requests)**:
  ```python
  import requests
  data = {"features": [0.0]*900}
  r = requests.post('http://127.0.0.1:5000/predict', json=data)
  print(r.json())
  ```

## Next steps
- Add a small **API usage** example in the front-end that calls `/predict` and displays results.
- Add a `.github/workflows/` CI file to run simple checks (lint/tests) on push.

---
Created and updated by GitHub Copilot (Raptor mini Preview).
