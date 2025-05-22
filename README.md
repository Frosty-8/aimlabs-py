# Circle Clicker Game

A minimalistic Pygame‑based game where you click a moving red circle to rack up points—and lose them when you miss.

## Table of Contents

* [Description](#description)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Code](#code)

  * [app.py](#apppy)
  * [Makefile](#makefile)
  * [requirements.txt](#requirementstxt)
* [Contributing](#contributing)
* [License](#license)
* [Notes](#notes)

---

## Description

The **Circle Clicker Game** opens a 1280 × 720 light‑blue window with a red circle in the centre. Each **left‑click on the circle** increments your score by one and teleports the circle to a new random position. Clicking **anywhere else** decrements the score by one. Your current score is always visible in the top‑left corner.

---

## Requirements

* **Python ≥ 3.6**
* **Pygame** (listed in `requirements.txt`)
* **Windows** (for the provided Makefile). See the *Notes* section for Unix instructions.
* **Make** (e.g., `mingw32-make` on Windows)

---

## Installation

### 1 ‑ Clone or download the project

```bash
# Example (HTTPS)
git clone https://github.com/your‑name/CircleClickerGame.git
cd CircleClickerGame
```

### 2 ‑ Set up the virtual environment and install dependencies

```bash
make install
```

This creates a `venv` folder and installs Pygame from `requirements.txt`.

### 3 ‑ Fix the PowerShell execution policy (Windows only)

If you see *“running scripts is disabled”*:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Answer **Y** when prompted.

---

## Usage

### Run the game

```bash
make run
```

`make` activates the virtual environment and launches `app.py`.

### How to play

1. **Click the red circle** → score +1, circle moves.
2. **Click elsewhere** → score –1.
3. Close the window to quit.

### Clean up

Remove the virtual environment and cached files:

```bash
make clean
```

---

## Project Structure

```text
CircleClickerGame/
├── app.py              # Main game script (Pygame logic)
├── Makefile            # Automation for setup and running
├── requirements.txt    # Python dependencies
├── venv/               # Virtual environment (created by `make install`)
└── README.md           # Project documentation
```

---

## Code

### app.py

```python
import pygame, sys, math, random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
circle_pos = (1280 / 2, 720 / 2)
font = pygame.font.Font(None, 30)
score = 0

def check_circle_condition() -> bool:
    mouse_pos = pygame.mouse.get_pos()
    return math.hypot(mouse_pos[0] - circle_pos[0], mouse_pos[1] - circle_pos[1]) <= 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if check_circle_condition():
                score += 1
                circle_pos = (random.randint(0, 1280), random.randint(0, 720))
            else:
                score -= 1

    screen.fill("lightblue")
    pygame.draw.circle(screen, "red", circle_pos, 50)
    score_surf = font.render(f"Score: {score}", True, "black")
    screen.blit(score_surf, (50, 50))
    pygame.display.update()
```

### Makefile

```makefile
# Variables
PYTHON = python
PIP = pip
VENV = venv
MAIN_SCRIPT = app.py

.PHONY: all install run clean

all: install run

install:
	$(PYTHON) -m venv $(VENV)
	$(VENV)\Scripts\pip install --upgrade pip
	$(VENV)\Scripts\pip install -r requirements.txt

install-lib:
	$(VENV)\Scripts\pip install -r requirements.txt

run:
	powershell -Command "& { . $(VENV)\Scripts\Activate.ps1; python $(MAIN_SCRIPT) }"

clean:
	if exist $(VENV) rmdir /s /q $(VENV)
	if exist __pycache__ rmdir /s /q __pycache__
	del /s /q *.pyc *.pyo 2>nul
```

### requirements.txt

```text
pygame
```

---

## Contributing

1. **Fork** the repository.
2. **Create** a feature or fix branch.
3. **Commit** your changes with clear messages.
4. **Test** thoroughly.
5. **Open** a pull request describing your changes.

Follow the existing coding style and comment where appropriate.

---

## License

This project is licensed under the **MIT License**. See `LICENSE` for full text.

---

## Notes

* **Non‑Windows systems**: Replace the `run` and `clean` targets in the Makefile with Unix‑friendly commands (e.g., `source venv/bin/activate`, `rm -rf`).
* **Negative scores** are allowed; to prevent them, add a check before decrementing in `app.py`.
* The Makefile supports a future `.env` file for environment variables, though none are used currently.
