# 🎮 Connect 4 — From Logic to AI  
*By Jeroen Penders*

A fully playable **Connect 4** built in Python — evolving from a simple two-player console game into an AI-driven opponent using **minimax** with **alpha-beta pruning**.  
This project represents my personal journey from beginner-level programming to algorithmic problem solving and optimization.

---

## 🚀 Overview

- **Version 1.0 → Two-Player Game**  
  A pure-Python console implementation. Players take turns dropping pieces; win detection covers horizontal, vertical, and both diagonal directions.

- **Version 1.2 → AI Opponent with Minimax + Alpha-Beta Pruning**  
  Introduced an AI that evaluates future board states using a heuristic scoring system.  
  Alpha-beta pruning was added later to reduce CPU load — the initial minimax ran every possible branch, causing the CPU to hit 100 % while the AI “thought” for several seconds.

---

## 💡 Motivation

I started this as a learning exercise — to understand data structures, loops, and logical conditions — while building something fun and visual.  
After finishing the two-player version, curiosity drove me to ask: *“Can I make the computer think?”*  
That question led me into search trees, heuristics, recursion, and finally optimization.

---

## ✨ Highlights

| Version | Key Features |
|----------|--------------|
| **1.0** | • Two-player local mode<br>• Random starting player<br>• Full win detection (horizontal, vertical, diagonal)<br>• Text-based board drawing |
| **1.2** | • One-player vs AI mode<br>• Minimax algorithm for decision-making<br>• Alpha-Beta pruning for performance<br>• Adjustable difficulty (search depth)<br>• Heuristic scoring for board strength |

---

## 🧠 Technical Journey

### **v 1.0 – Foundations**
- Built a 6×7 board as nested lists.  
- Learned to manage two-dimensional data and control loops.  
- Implemented functions for move validation, gravity simulation, and win checking.  
- Experienced that incredible *“it finally works!”* moment seeing the full game loop run.

### **v 1.2 – Artificial Intelligence**
- Replaced manual turn logic with the **Minimax algorithm**, allowing the AI to evaluate possible moves several layers deep.  
- Designed a **heuristic evaluation function** that scored board states based on:
  - Central column control  
  - 2-, 3-, and 4-in-a-row opportunities  
  - Blocking opponent threats  
- Introduced **Alpha-Beta Pruning**, after discovering the CPU pegged at 100 % during deeper searches.  
  This optimization cut computation time drastically while producing identical move quality.  
- Added configurable difficulty by adjusting recursion depth.


