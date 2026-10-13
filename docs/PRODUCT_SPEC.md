# FocusPet Product Specification and Acceptance Criteria

## 1. Project Goal

Build a working macOS desktop pet by October 31, 2026, and use the development process to gain practical Python skills. Success is measured by the ability to understand requirements, write code, diagnose problems, and add features independently—not by memorizing definitions.

## 2. Core Loop

```text
Start focusing → Pet keeps you company → Complete Pomodoro → Earn coins/XP
       ↑                                                       ↓
       └──────────── Dress up, feed, interact, and grow ────────┘
```

## 3. Pet Behavior

### 3.1 Core States

- `idle`: breathe, blink, or perform a random small action.
- `focus`: stay calm while a Pomodoro session is running.
- `picked_up`: display a suspended pose while held by the mouse.
- `swinging`: swing according to the speed and direction of dragging.
- `falling`: move downward after being released.
- `landing`: play a short landing response after touching a platform.
- `walking`: move toward a selected destination.
- `celebrating`: celebrate after a Pomodoro session is completed.
- `sleeping`: possibly fall asleep after a long period without interaction.

Only one primary state should be active at a time so that animations do not conflict. This behavior will gradually evolve into a state machine.

### 3.2 Dragging and Landing

1. Holding the pet changes its state to `picked_up`.
2. The pet follows the pointer and swings according to horizontal movement speed.
3. After the mouse button is released:
   - Free mode: the pet stays at the release position.
   - Platform mode: the pet enters `falling` and lands on the nearest valid platform below it.

### 3.3 Platforms

`v1.0` must support:

- The bottom of the screen as the default ground.
- At least two user-configurable virtual platforms.
- Detection of whether the pet is standing on a platform.
- Switching between platform mode and free mode.

Detecting the top edges of other application windows is an enhancement. Because it depends on operating-system permissions and access to window information, it is not required for the end-of-month acceptance test.

### 3.4 Guided Movement

- First version: select a destination on the same platform and let the pet walk toward it.
- Second version: if the target is on another platform, choose a route through connected platforms.
- Enhancement: add jumping or a more complete pathfinding system.

## 4. Focus and Progression

### 4.1 Pomodoro Timer

- The default focus duration is configurable, with short durations allowed during development.
- The timer supports starting, pausing, resuming, and abandoning a session.
- Rewards are granted only when a session is completed normally.
- The timer state and pet behavior must remain synchronized.

### 4.2 Rewards

- Completing a focus session grants coins and experience points.
- The pet levels up after reaching an experience threshold.
- Reward calculations are kept in one place so that balancing can be adjusted later.

### 4.3 Shop and Outfits

- The shop contains at least three items.
- Not purchased, owned, and equipped states are clearly distinguishable.
- An item cannot be purchased when the balance is too low.
- Equipment changes are visible on the pet or in its information panel.

### 4.4 Save Data

The save file contains at least the coin balance, experience, level, purchased items, current equipment, Pomodoro settings, and pet position. If the save file is damaged, the application should display an understandable message and safely create a new save.

## 5. Priorities

### Required (P0)

Transparent desktop pet, dragging and swinging, falling and platforms, basic guided movement, Pomodoro timer, rewards, shop, equipment, and save data.

### Targeted (P1)

Additional idle actions, random dialogue, sleeping, focus streak rewards, and focus-statistic visualizations.

### After the Monthly Milestone (P2)

Detecting other application windows, multi-display support, complex jumping routes, sound, a plugin system, and a packaged installer.

## 6. Final Acceptance

### Product Acceptance

- Follow the README from a clean environment and start the application.
- Demonstrate one complete focus, reward, purchase, and equip cycle.
- Demonstrate dragging, swinging, falling, landing, and guided movement.
- Close and reopen the application without losing key data.
- Cover core logic with automated tests.

### Learning Acceptance

- Build a small Python feature from an empty file without copying an answer.
- Explain in personal words how events, functions, objects, and state work together.
- Add one small feature independently.
- Locate and repair two intentionally introduced common errors.
- Create a Git commit and explain what problem the commit solves.
