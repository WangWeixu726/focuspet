# October 2026 Development Roadmap

> Default pace: approximately 60–90 minutes per day. If time becomes limited, preserve a complete P0 experience and reduce the amount of artwork or visual polish first.

## Stage 0: Make the Project Run (October 12–13)

- [x] Define the product scope and end-of-month acceptance criteria
- [x] Create the local Git repository structure
- [x] Create and connect the public GitHub repository
- [x] Prepare a Python 3.14 virtual environment
- [x] Install PySide6 and pytest
- [x] Build and run the first desktop window

Learning focus: the terminal, Python interpreters, virtual environments, packages, application entry points, and the first independent Git workflow.

## Stage 1: Bring the Pet to Life (October 14–17)

- [x] Create a transparent, frameless, always-on-top window
- [x] Display the first placeholder pet image
- [ ] Handle mouse press, move, and release events
- [ ] Add the picked-up state
- [ ] Swing according to dragging direction
- [ ] Add a basic idle animation

Learning focus: variables, coordinates, conditions, functions, events, timers, and debug output.

## Stage 2: Desktop Space and Platforms (October 18–21)

- [ ] Add falling after release
- [ ] Treat the bottom of the screen as the ground
- [ ] Add two custom platforms
- [ ] Detect landing
- [ ] Add free mode and platform mode
- [ ] Move toward a destination on the same platform

Learning focus: lists, dictionaries, loops, state machines, position and velocity updates, and collision detection.

## Stage 3: Focus and Progression (October 22–25)

- [ ] Start, pause, resume, and complete a Pomodoro session
- [ ] Connect focus state to pet behavior
- [ ] Add coins, experience, and levels
- [ ] Save and restore data with JSON
- [ ] Recover safely from damaged save data

Learning focus: time, data modeling, file input and output, exception handling, and module organization.

## Stage 4: Shop and Outfits (October 26–28)

- [ ] Add three purchasable items
- [ ] Validate purchases and deduct coins
- [ ] Add inventory and equipment
- [ ] Display equipped items or equipment state
- [ ] Test reward and shop logic

Learning focus: classes, separation of responsibilities, data validation, automated testing, and refactoring.

## Stage 5: Routes, Polish, and Acceptance (October 29–31)

- [ ] Add basic guided movement across platforms
- [ ] Add random idle interactions
- [ ] Complete the README and setup instructions
- [ ] Record a GIF or short video
- [ ] Release `v1.0`
- [ ] Complete the independent feature, explanation, debugging, and Git assessments

Learning focus: simple pathfinding, integration debugging, release practices, and project reflection.

## Scope Protection Rules

If progress falls behind, reduce scope in this order rather than sacrificing a complete experience:

1. Reduce the number of outfits and animation assets.
2. Simplify animation frames and the shop interface.
3. Postpone detection of other application windows.
4. Replace complex cross-platform jumping with predefined platform routes.
