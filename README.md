# PyChess

[![Python](https://img.shields.io/badge/python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pygame-CE](https://img.shields.io/badge/pygame--ce-2.5.6-45B7D1)](https://pyga.me/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A lightweight chessboard project built with Python and Pygame.

## Features

- Renders an 8x8 chessboard using Pygame
- Includes a development hot reload mode
- Supports opening the window on monitor 2 for dual-screen setups

## Requirements

- Python 3.12+
- `pygame-ce==2.5.6` (installed from `requirements.txt`)

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the game

- Normal run: `python run.py`
- Hot reload mode: `python run.py --hotreload`
- Hot reload + monitor 2: `python run.py --hotreload --second-screen`

In hot reload mode, the launcher watches Python files and automatically restarts the game whenever source files change.

## Development flags

- `--hotreload`: Restart the game process after Python source changes
- `--interval <seconds>`: Polling interval for file watching (default: `0.5`)
- `--second-screen`: Start on display 2 when available

## Project structure

- `run.py`: Launcher and hot reload entrypoint
- `game/main.py`: Pygame window setup and game loop
- `game/chess_board.py`: Chessboard and square rendering classes

## License

Distributed under the MIT License. See `LICENSE` for details.
