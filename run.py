from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
IGNORED_DIR_NAMES = {".git", "venv", "__pycache__", ".mypy_cache", ".pytest_cache"}


def run_game_once(second_screen: bool) -> None:
    import game

    game.main.game(second_screen=second_screen)


def iter_watched_files(root: Path):
    for path in root.rglob("*.py"):
        if any(part in IGNORED_DIR_NAMES for part in path.parts):
            continue
        yield path


def build_file_snapshot(root: Path) -> dict[str, int]:
    snapshot: dict[str, int] = {}

    for file_path in iter_watched_files(root):
        try:
            snapshot[str(file_path)] = file_path.stat().st_mtime_ns
        except OSError:
            continue

    return snapshot


def restart_child_process(
    child: subprocess.Popen[bytes], second_screen: bool
) -> subprocess.Popen[bytes]:
    if child.poll() is None:
        child.terminate()
        try:
            child.wait(timeout=2)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait()

    command = [sys.executable, str(PROJECT_ROOT / "run.py"), "--child"]
    if second_screen:
        command.append("--second-screen")

    return subprocess.Popen(command)


def run_with_hotreload(interval: float, second_screen: bool) -> None:
    command = [sys.executable, str(PROJECT_ROOT / "run.py"), "--child"]
    if second_screen:
        command.append("--second-screen")

    child = subprocess.Popen(command)
    previous_snapshot = build_file_snapshot(PROJECT_ROOT)

    try:
        while True:
            time.sleep(interval)

            if child.poll() is not None:
                break

            current_snapshot = build_file_snapshot(PROJECT_ROOT)
            if current_snapshot != previous_snapshot:
                print("Detected source changes. Reloading game...")
                previous_snapshot = current_snapshot
                child = restart_child_process(child, second_screen=second_screen)

    except KeyboardInterrupt:
        pass
    finally:
        if child.poll() is None:
            child.terminate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hotreload",
        action="store_true",
        help="Restart the game when Python files change",
    )
    parser.add_argument(
        "--interval", type=float, default=0.5, help="Watch interval in seconds"
    )
    parser.add_argument(
        "--second-screen",
        action="store_true",
        help="Start the game window on monitor 2 when available",
    )
    parser.add_argument("--child", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.child:
        run_game_once(second_screen=args.second_screen)
    elif args.hotreload:
        run_with_hotreload(interval=args.interval, second_screen=args.second_screen)
    else:
        run_game_once(second_screen=args.second_screen)
