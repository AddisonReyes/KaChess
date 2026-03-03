from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
IGNORED_DIR_NAMES = {".git", "venv", "__pycache__", ".mypy_cache", ".pytest_cache"}


def run_game_once() -> None:
    import game

    game.main.game()


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


def restart_child_process(child: subprocess.Popen[bytes]) -> subprocess.Popen[bytes]:
    if child.poll() is None:
        child.terminate()
        try:
            child.wait(timeout=2)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait()

    return subprocess.Popen([sys.executable, str(PROJECT_ROOT / "run.py"), "--child"])


def run_with_hotreload(interval: float) -> None:
    child = subprocess.Popen([sys.executable, str(PROJECT_ROOT / "run.py"), "--child"])
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
                child = restart_child_process(child)
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
    parser.add_argument("--child", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.child:
        run_game_once()
    elif args.hotreload:
        run_with_hotreload(interval=args.interval)
    else:
        run_game_once()
