# 🎼 orcust-spine

> **Automated 2D Animation & Spine Motion Pipeline for AI Companions.**  
> *Crafting mechanical skeletons and breathing fluid motion into digital souls.*

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Spine](https://img.shields.io/badge/Spine-3.7%20%7C%203.8-orange.svg)](http://esotericsoftware.com/)
[![Ecosystem](https://img.shields.io/badge/Ecosystem-orcust--companiond-purple.svg)](https://github.com/vincentlalo-long/orcust-companiond)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 Overview

**`orcust-spine`** is the motion and character animation engine within the **Orcust** desktop assistant ecosystem, designed to work in tandem with [`orcust-companiond`](https://github.com/vincentlalo-long/orcust-companiond).

While `orcust-companiond` serves as the cognitive core and runtime daemon (LLM, STT, TTS, and desktop UI), `orcust-spine` focuses on the visual and motion pipeline: **turning flat 2D character illustrations into fluid, interactive, 60 FPS animated avatars**.

```
                ┌────────────────────────────────────────┐
                │          Static 2D Character           │
                │             (Single Image)             │
                └──────────────────┬─────────────────────┘
                                   │
                                   ▼
        ┌────────────────────────────────────────────────────────┐
        │                      orcust-spine                      │
        │                                                        │
        │  [1. Reference Extractor] ──► Extracts game Spine data │
        │  [2. Portrait & Face Sync]──► Official 256x256 cards   │
        │  [3. Headless Renderer  ] ──► Full-body 2K RGBA PNGs   │
        │  [4. Layer Decomposition] ──► AI parts + inpainting    │
        │  [5. Motion Retargeting ] ──► Transfers Idle/Talk      │
        │  [6. Loop Exporter      ] ──► 60 FPS Transparent WebM  │
        └──────────────────────────┬─────────────────────────────┘
                                   │
                                   ▼
                ┌────────────────────────────────────────┐
                │           orcust-companiond            │
                │     (Tauri / Linux Desktop Daemon)     │
                │  - Idle Breathing Loop                 │
                │  - Responsive Mouth Talk (TTS lipsync) │
                │  - Touch / Interaction Reaction        │
                └────────────────────────────────────────┘
```

---

## ✨ Key Features

- 🧩 **Modular Spine Extractor**: An extensible extraction architecture designed for 2D game assets. The pipeline implements full decryption and extraction for *CounterSide* (Spine 3.7) as the primary reference database (providing 1,300+ character and skin motion templates).
- 🎴 **Direct Portrait Extractor**: Bulk extraction of official character face cards directly from game asset bundles, automatically mapped and synchronized into individual character directories.
- 🎨 **Headless Full-Body Renderer**: Pure CLI headless renderer (powered by Edge/Chrome and PixiJS) that converts Spine 3.7 skeleton data into high-resolution, transparent (RGBA), auto-cropped full-body standing illustrations without requiring any web server or UI.
- ✂️ **Semantic Layer Segmentation**: Automated separation of character artwork into independent anatomical layers (hair, eyes, face, torso, clothes) with background occlusion inpainting.
- 🦴 **Motion Retargeting**: Map keyframe trajectories (`IDLE`, `TOUCH`, `mouth_talk`) from reference game skeletons onto custom target characters.
- 🎬 **Companion-Ready WebM Exporter**: Output ultra-lightweight, hardware-accelerated VP9 transparent WebM loops (< 2% CPU overhead on desktop).

---

## 🚀 Quick Start

### 1. Installation & Environment

Prerequisites:
- **Python 3.10+** (recommended: 3.11)
- **Microsoft Edge** or **Google Chrome** (used for headless WebGL Spine rendering)

Install Python dependencies:
```bash
pip install -r requirements.txt
```

### 2. Configuration
Copy `.env.example` to `.env` and specify your CounterSide game asset directory:
```bash
# Windows (PowerShell)
copy .env.example .env

# Linux / macOS
cp .env.example .env
```

Edit `.env`:
```env
CS_STREAMING_ASSETS_DIR=D:\Game\CounterSide\Game\CounterSide\Data\StreamingAssets
OUTPUT_DIR=outputs
```

---

## 🛠️ CLI Tools & Workflow

### Step 1: Extract Spine Assets (`extract.py`)
Extract `.skel`, `.atlas`, and texture `.png` files from encrypted game bundles:
```bash
# Search and list matching character bundles without extracting
python extract.py --name "c_yoo_mi_na" --list

# Extract character Spine assets
python extract.py --name "illust_nkm_unit_c_yoo_mi_na.asset"
```

### Step 2: Extract & Sync Character Portraits (`extract_portraits.py`)
Extract official 256x256 face cards directly from game bundles and automatically synchronize them to character folders:
```bash
# Extract all character portraits and auto-sync to outputs/<char_id>/portrait.png
python extract_portraits.py --sync
```
*Outputs are saved to `outputs/portraits/` and mirrored to each character's folder as `portrait.png`.*

### Step 3: Render Full-Body Standing Art (`render_fullbody.py`)
Render full-body illustrations from Spine data into transparent RGBA PNGs (with auto-pose detection, dynamic centering, and automatic alpha margin trimming):
```bash
# Render specific characters by name keyword
python render_fullbody.py -n hilde
python render_fullbody.py -n yoo_mi_na

# Render all extracted characters in outputs/
python render_fullbody.py --all

# Force re-rendering existing images
python render_fullbody.py -n hilde --force
```

---

## 📁 Output Structure

Each character directory in `outputs/` contains complete, self-contained reference assets:

```
outputs/
├── nkm_unit_c_hilde/
│   ├── UNIT_ILLUST_C_HILDE.skel   # Spine 3.7 binary skeleton data
│   ├── UNIT_ILLUST_C_HILDE.atlas  # Spine texture atlas definition
│   ├── UNIT_ILLUST_C_HILDE.png    # Spine sprite atlas texture
│   ├── portrait.png               # Official 256x256 character face card
│   └── full_body.png              # Rendered transparent full-body art (~1200x2100)
└── portraits/                     # Central repository of all 1,400+ face cards
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
- All third-party game assets belong to their respective copyright holders (Studiobside Co., Ltd. / Nexon). Users are solely responsible for supplying their own legally acquired assets.

---

## 📜 License

Distributed under the [MIT License](LICENSE).  
Part of the **Orcust** project suite, paired with [`orcust-companiond`](https://github.com/vincentlalo-long/orcust-companiond).