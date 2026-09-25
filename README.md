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

- 🧩 **Spine Asset Extractor**: Extract and decrypt Spine binary skeletons (`.skel`), texture maps (`.atlas`), and high-res atlas textures (`.png`) from Unity AssetBundles (supports Spine 3.7/3.8 titles such as *CounterSide*).
- ✂️ **Semantic Layer Segmentation**: Automated separation of character artwork into independent anatomical layers (hair, eyes, face, torso, clothes) with background occlusion inpainting.
- 🦴 **Motion Retargeting**: Map keyframe trajectories (`IDLE`, `TOUCH`, `mouth_talk`) from reference game skeletons onto custom target characters.
- 🎬 **Companion-Ready WebM Exporter**: Output ultra-lightweight, hardware-accelerated VP9 transparent WebM loops (< 2% CPU overhead on desktop).

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
Part of the **Orcust** project suite, paired with [`orcust-companiond`](https://github.com/vincentlalo-long/orcust-companiond).