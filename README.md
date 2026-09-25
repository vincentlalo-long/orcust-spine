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
        │  [2. Layer Decomposition] ──► AI parts + inpainting    │
        │  [3. Motion Retargeting ] ──► Transfers Idle/Talk      │
        │  [4. Loop Exporter      ] ──► 60 FPS Transparent WebM  │
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

- 🧩 **Modular Spine Extractor**: An extensible extraction architecture designed for 2D game assets. The pipeline initially implements full decryption and extraction for *CounterSide* (Spine 3.7) as the primary reference database (providing 1,300+ character and skin motion templates), with support for additional titles planned.
- ✂️ **Semantic Layer Segmentation**: Automated separation of character artwork into independent anatomical layers (hair, eyes, face, torso, clothes) with background occlusion inpainting.
- 🦴 **Motion Retargeting**: Map keyframe trajectories (`IDLE`, `TOUCH`, `mouth_talk`) from reference game skeletons onto custom target characters.
- 🎬 **Companion-Ready WebM Exporter**: Output ultra-lightweight, hardware-accelerated VP9 transparent WebM loops (< 2% CPU overhead on desktop).

---

## 🚀 Quick Start (Reference Extraction: CounterSide)

### 1. Configuration
Copy `.env.example` to `.env` and set your CounterSide `StreamingAssets` path:
```bash
# Windows (PowerShell / CMD)
copy .env.example .env

# Linux / macOS
cp .env.example .env
```

Edit `.env`:
```env
CS_STREAMING_ASSETS_DIR=D:\Game\CounterSide\Game\CounterSide\Data\StreamingAssets
OUTPUT_DIR=outputs
```

### 2. Search & Extract Characters
Use the CLI to search character bundles or extract full Spine assets:
```bash
# List matching character bundles without extracting
python extract.py --name "c_yoo_mi_na" --list

# Extract character Spine assets (creates .skel, .atlas, .png)
python extract.py --name "illust_nkm_unit_c_yoo_mi_na.asset"
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