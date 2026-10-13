# Pair-Learning and GitHub Workflow

## How Each Session Works

Each session advances one small, verifiable goal:

1. The mentor explains what should be visible when the step is complete.
2. Only the concepts and examples needed for that step are introduced.
3. The learner writes and runs the core code.
4. The learner shares the result or error, and both sides investigate it together.
5. After the feature works, the code is cleaned up, committed, and followed by a short reflection.

Complete solutions are not provided at the beginning by default. When help is needed, hints progress through three levels:

- Level 1: identify the problem area and suggest what to inspect.
- Level 2: provide pseudocode or the key API.
- Level 3: provide the smallest working correction and explain it line by line.

## Commit Standards

- Each commit should complete one clearly describable change.
- Run the relevant code at least once before committing.
- Use a short English commit message, such as `feat: support dragging the pet`.
- Do not commit virtual environments, caches, operating-system files, or personal save data.
- Create a version tag after completing each major stage.

Suggested commit types:

- `feat`: a new feature
- `fix`: a bug fix
- `refactor`: a code improvement that does not change behavior
- `test`: automated tests
- `docs`: documentation or learning-log changes
- `chore`: environment or tooling maintenance

## Development Log Template

At the end of a session, add a short entry under `devlog/`:

```markdown
## What I Completed

- (Fill this in.)

## Problems and Solutions

- (Fill this in.)

## Concepts I Can Explain Now

- (Fill this in.)

## Next Step

- (Fill this in.)
```

## GitHub Presentation Goal

A visitor should be able to understand what the project does, how to run it, how its key features evolved, what problems appeared during development, and what the learner genuinely mastered. The log should be honest and concise rather than a daily essay.
