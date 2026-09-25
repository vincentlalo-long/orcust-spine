# 🎼 orcust-spine

> **Automated 2D Animation & Spine Motion Pipeline for AI Companions.**  
> *Crafting mechanical skeletons and breathing fluid motion into digital souls.*

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Spine](https://img.shields.io/badge/Spine-3.7%20%7C%203.8-orange.svg)](http://esotericsoftware.com/)
[![Ecosystem](https://img.shields.io/badge/Ecosystem-Orcust%20Companion-purple.svg)](https://github.com/vincentlalo-long)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 Overview

**`orcust-spine`** is the motion and character animation engine within the **Orcust** desktop assistant ecosystem (paired directly with [`orcust-companion`](https://github.com/vincentlalo-long)).

While `orcust-companion` handles the cognitive core (LLM, STT, TTS, and desktop runtime daemon), `orcust-spine` solves the visual pipeline: **turning flat 2D character illustrations (e.g., Makise Kurisu) into fluid, interactive, 60 FPS animated avatars**.

```
                ┌────────────────────────────────────────┐
                │          Static 2D Character           │
                │        (e.g., Makise Kurisu)           │
                └──────────────────┬─────────────────────┘
                                   │
                                   ▼
        ┌────────────────────────────────────────────────────────┐
        │                      orcust-spine                      │
        │                                                        │
        │  [1. Reference Extractor] ──► Extracts game Spine data │
        │  [2. Layer Decomposition] ──► AI parts + inpainting    │
        │  [3. Motion Retargeting ] ──► Transfers Idle/Talk      │
        │  [4. Loop Exporter      ] ──► 60 FPS Transparent WebM  │
        └──────────────────────────┬─────────────────────────────┘
                                   │
                                   ▼
                ┌────────────────────────────────────────┐
                │            orcust-companion            │
                │     (Tauri / Linux Desktop Daemon)     │
                │  - Idle Breathing Loop                 │
                │  - Responsive Mouth Talk (TTS lipsync) │
                │  - Touch / Interaction Reaction        │
                └────────────────────────────────────────┘
```

---

## ✨ Key Features

- 🧩 **Spine Asset Extractor**: High-speed extraction and decryption of Spine binary skeletons (`.skel`), texture maps (`.atlas`), and high-res atlas textures (`.png`) from Unity AssetBundles.
- ✂️ **Semantic Layer Segmentation**: Automated separation of character artwork into independent anatomical layers (hair, eyes, face, torso, clothes) with background occlusion inpainting.
- 🦴 **Motion Retargeting**: Map keyframe trajectories (`IDLE`, `TOUCH`, `mouth_talk`) from reference game skeletons onto custom target characters.
- 🎬 **Companion-Ready WebM Exporter**: Output ultra-lightweight, hardware-accelerated VP9 transparent WebM loops (< 2% CPU overhead on desktop).

---

## 📁 Repository Structure

```text
orcust-spine/
├── .gitignore               # Strict ignore rules for game assets and model weights
├── README.md                # Project documentation
├── requirements.txt         # Core dependencies (UnityPy, Pillow, etc.)
├── config.example.yaml      # Configuration template for asset and output paths
│
├── modules/
│   ├── extractor/           # Asset extraction & crypto stream handlers
│   │   ├── decrypt.py       # Header decryption & crypto routines
│   │   └── spine_extract.py # Spine bundle parser (.skel, .atlas, .png)
│   │
│   ├── segmenter/           # 2D Layer decomposition & inpainting
│   │   └── layer_split.py   # Anime segmentation wrapper
│   │
│   ├── rigger/              # Skeleton generation & animation retargeting
│   │   └── retarget.py      # Transfer bone motions from template
│   │
│   └── viewer/              # Local preview server & video recorder
│       ├── server.py        # Lightweight local asset server
│       └── web/             # PixiJS + Spine 3.7/3.8 HTML5 runtime
│
├── extract.py               # CLI tool to extract reference Spine assets
└── pipeline.py              # End-to-end execution pipeline
```

---

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.11+**
- **NVIDIA GPU** with CUDA support (Recommended: RTX 3060/4060 or higher with 8GB VRAM)
- Optional for `.jar` tools: Java Runtime Environment 17+

### 2. Installation
```bash
# Clone repository
git clone https://github.com/vincentlalo-long/orcust-spine.git
cd orcust-spine

# Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Extracting Reference Motion
Extract high-resolution character Spine assets from game bundles:
```bash
# Extract character by name keyword
python extract.py --name "mina"

# Output will be located in:
# outputs/spine_mina/
# ├── UNIT_ILLUST_C_YOO_MI_NA.skel
# ├── UNIT_ILLUST_C_YOO_MI_NA.atlas
# └── UNIT_ILLUST_C_YOO_MI_NA.png
```

---

## 🎯 Target Pipeline for AI Companions

| State | Animation Target | Description |
| :--- | :--- | :--- |
| **Idle** | `idle.webm` | Subtle breathing, eye blinking, gentle hair sway (looping 3-4s). |
| **Speaking** | `talk.webm` | Natural mouth movement synchronized with TTS speech output. |
| **React** | `touch.webm` | Response triggered upon desktop cursor interaction / click. |

---

## ⚖️ Disclaimer

This repository is developed strictly for **educational, non-commercial, and open-source research purposes**.
- **No copyrighted game assets, binary textures, or audio clips are hosted or distributed in this repository.**
- All third-party game assets belong to their respective copyright holders. Users are solely responsible for supplying their own legally acquired assets.

---

## 📜 License

Distributed under the [MIT License](LICENSE).
Part of the **Orcust** project suite.