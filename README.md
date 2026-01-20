# Distributed Neural Image Compression with Overfitted Models  
### Master’s Thesis – Abdulrahman Almajdalawi (2025)

This repository contains the code developed for my Master’s thesis:

**“Distributed Image Compression Using Overfitted Neural Network Models.”**

This project builds on the **C3 neural compression framework** and extends it to study **distributed / side-information–based image compression**, inspired by information-theoretic principles such as **Slepian–Wolf and Wyner–Ziv coding**. The core idea is to exploit **stereo image pairs available only at the decoder** to reduce the bitrate required to encode an image.

---

## Thesis Information

- **Title:** Distributed Image Compression Using Overfitted Neural Network Models  
- **Author:** Abdulrahman Almajdalawi  
- **Degree:** MSc in Applied Computer Science  
- **Institution:** Vrije Universiteit Brussel  
- **Year:** 2025  

The full thesis manuscript is included in this repository.

---

## Project Overview

Most neural image compression systems rely on large models trained on massive datasets to generalize across images. In contrast, **overfitted neural compression models** (such as COOL-CHIC and C3) learn a **compact neural representation per image**, achieving strong rate–distortion performance with low decoding complexity.

In this thesis, I extend the **C3 neural compression framework** to explore a new research direction:

> Can side information available only at the decoder (e.g., stereo image pairs) be exploited to reduce the bitrate of overfitted neural image compression?

The work focuses on designing and evaluating architectures that integrate **stereo side information** into the decoding process while keeping the encoding independent.

---

## Technical Highlights

- Extension of a research-grade neural compression framework (C3 / COOL-CHIC)  
- Design and implementation of custom decoder-side architectures  
- Integration of distributed source coding concepts into neural compression  
- Large-scale experiments on the KITTI 2012 stereo dataset  
- Quantitative evaluation using:
  - PSNR  
  - MS-SSIM  
  - LPIPS  
  - Bit-per-pixel (bpp)  
- Automated experiment pipelines and result logging

---

## Baseline Framework

This project is built on top of:

**C3: High-performance and low-complexity neural compression from a single image or video**  
Hyunjik Kim, Matthias Bauer, Lucas Theis, Jonathan Richard Schwarz, Emilien Dupont  
arXiv 2023 – https://arxiv.org/abs/2312.02753  
Project page – https://c3-neural-compression.github.io/

C3 itself builds on **COOL-CHIC** (Ladune et al.).

The original C3 work demonstrates that overfitted neural models can achieve state-of-the-art rate–distortion performance with significantly reduced decoding complexity. This thesis extends that work toward **distributed neural image compression**.


