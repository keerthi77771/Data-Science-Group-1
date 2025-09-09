# Data-Science-Group-1

This repo contains the Stage-1 notebook and report.  
The dataset (`data/newdata.csv`) is **not committed** due to size/privacy.  
Use the provided script to fetch it locally.

---

## What's here

├─ scripts/
│ └─ data_download.py # downloads data/newdata.csv from Google Drive (default ID embedded)
├─ Stage 1 (1).ipynb
├─ Stage 1 (1).html
├─ Project stage I report (1).docx
└─ README.md

This downloads data/newdata.csv using the default Google Drive File ID already in the script.


The `data/` folder will be created automatically when the script runs.

---

## Getting the dataset

### Quick run (default Google Drive ID baked in)
```bash
python scripts/data_download.py


Please find the script below:
#!/usr/bin/env bash
# get_newdata.sh
# Clones the repo, installs dependencies, and pulls data/newdata.csv from Google Drive.
# macOS/Linux friendly. Requires: git, python3

set -euo pipefail

REPO_URL="https://github.com/keerthi77771/Data-Science-Group-1.git"
REPO_DIR="Data-Science-Group-1"

echo "=== 1) Clone or update repo ==="
if [ -d "$REPO_DIR/.git" ]; then
  echo "Repo already present. Pulling latest changes..."
  git -C "$REPO_DIR" pull --ff-only
else
  echo "Cloning $REPO_URL ..."
  git clone "$REPO_URL"
fi

echo "=== 2) Enter repo directory ==="
cd "$REPO_DIR"

echo "=== 3) Show repo status ==="
git status
git log -1 --oneline || true

echo "=== 4) Create and activate Python venv ==="
PYBIN="python3"
command -v python3 >/dev/null 2>&1 || PYBIN="python"

$PYBIN -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate

echo "=== 5) Upgrade pip and install dependencies (gdown) ==="
python -m pip install --upgrade pip
python -m pip install gdown

echo "=== 6) Download dataset to data/newdata.csv ==="
python scripts/data_download.py

echo "=== 7) Verify file exists ==="
ls -lh data/newdata.csv

echo "=== DONE ===
Repo:      $(pwd)
Dataset:   data/newdata.csv
You can now open the notebook:
  (.venv) jupyter notebook 'Stage 1 (1).ipynb'
"


