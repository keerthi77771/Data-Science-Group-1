# scripts/download_data.py
import argparse
from pathlib import Path
import urllib.request

def download_url(url: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {url} -> {out_path}")
    urllib.request.urlretrieve(url, out_path)
    print("Done.")

def download_gdrive(file_id: str, out_path: Path):
    try:
        import gdown  # install only if you use Google Drive
    except ImportError:
        raise SystemExit("Please install gdown first: pip install gdown")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading GDrive file id={file_id} -> {out_path}")
    gdown.download(id=file_id, output=str(out_path), quiet=False)
    print("Done.")

if __name__ == "__main__":
    DEFAULT_GDRIVE_ID = "1xbwo_aYWxF0Cw90QygnfT1lA-RzsNkS7"
    p = argparse.ArgumentParser(description="Fetch data/newdata.csv without committing large files.")
    p.add_argument("--out", default="data/newdata.csv")
    p.add_argument("--url", help="Direct download URL (HTTP/S3 pre-signed/etc.)")
    p.add_argument("--gdrive-id", help="Google Drive file ID (alternative to --url)")
    args = p.parse_args()

    out = Path(args.out)
    if args.url:
        download_url(args.url, out)
    elif args.gdrive_id:
        download_gdrive(args.gdrive_id, out)
    else:
        # fallback to your file
        download_gdrive(DEFAULT_GDRIVE_ID, out)
