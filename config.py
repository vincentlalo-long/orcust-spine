from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


# Load .env variables into os.environ
def load_env(env_file: Path | None = None) -> None:
    target = env_file or (BASE_DIR / ".env")
    if not target.is_file():
        return

    for line in target.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        key, val = key.strip(), val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


load_env()

STREAMING_DIR_STR = os.getenv("CS_STREAMING_ASSETS_DIR", "")
OUTPUT_DIR_STR = os.getenv("OUTPUT_DIR", "outputs")

DEFAULT_OUTPUT_DIR = (
    Path(OUTPUT_DIR_STR) if Path(OUTPUT_DIR_STR).is_absolute() else BASE_DIR / OUTPUT_DIR_STR
)


# Get StreamingAssets path from .env or fallback
def get_default_streaming_dir() -> Path:
    if STREAMING_DIR_STR:
        return Path(STREAMING_DIR_STR)
    return Path(r"D:\Game\CounterSide\Game\CounterSide\Data\StreamingAssets")
