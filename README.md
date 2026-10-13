# FocusPet

A playful desktop companion that turns focused study sessions into rewards, growth, and interaction.

> Current status: a draggable placeholder pet is running in a transparent, frameless, always-on-top window. The goal is to release `v1.0` by October 31, 2026, and demonstrate the ability to build, explain, debug, and extend the project independently.

## Core Experience

1. Start a Pomodoro session and let the pet keep you company.
2. Earn coins and experience points after completing a focus session.
3. Spend rewards on clothes, food, and small items.
4. Pick the pet up with the mouse and watch it swing from side to side; release it to land on the ground or a platform.
5. Guide the pet to a destination, or switch to free mode and place it anywhere on the desktop.

## `v1.0` Acceptance Checklist

- [x] Transparent, frameless, always-on-top pet window
- [ ] Idle animations and click interactions
- [ ] Pick-up, dragging, swinging, falling, and landing
- [ ] A ground surface and at least two custom platforms
- [ ] Free mode and platform mode
- [ ] Guided movement to a selected destination
- [ ] Start, pause, resume, and complete a Pomodoro session
- [ ] Coin and experience rewards for completed sessions
- [ ] A shop, inventory, and at least three equippable items
- [ ] Local save data that survives an application restart
- [ ] Basic automated tests, setup instructions, and a demo

## Technology

- Python 3.14
- PySide6 for the desktop window, mouse events, timers, and animations
- JSON for the first save-data format
- pytest for automated tests

PySide6 was selected because FocusPet needs a transparent frameless window, always-on-top behavior, mouse interaction, and timers. The first stages use simple placeholder visuals so that artwork does not overshadow learning Python.

## Getting Started

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

The virtual environment keeps this project's packages separate from the system Python installation and other projects.

## Learning Approach

This repository records both the product and the learning process. Each feature follows the same cycle: define the need, break down the problem, implement it, debug it, create a small commit, and write a short reflection.

- [Product specification and acceptance criteria](docs/PRODUCT_SPEC.md)
- [Development roadmap](docs/ROADMAP.md)
- [Pair-learning workflow](docs/LEARNING_WORKFLOW.md)
- [Development log](devlog/)

## Current Next Step

Add a picked-up state with visible feedback while the pet is being held.
