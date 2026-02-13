"""
Read/write progress.json — tracks completion state for each milestone.
"""

import json
from datetime import date, datetime
from pathlib import Path

from roadmap import ROADMAP

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
PROGRESS_FILE = DATA_DIR / "progress.json"


def _default_progress() -> dict:
    """Generate default progress entries for all milestones."""
    return {
        m["id"]: {"completed": False, "completed_date": None}
        for m in ROADMAP
    }


def load_progress() -> dict:
    """Load progress from file, creating it with defaults if missing."""
    if not PROGRESS_FILE.exists():
        progress = _default_progress()
        save_progress(progress)
        return progress

    with open(PROGRESS_FILE) as f:
        saved = json.load(f)

    # Merge with defaults so new milestones get added automatically
    defaults = _default_progress()
    for key, val in defaults.items():
        if key not in saved:
            saved[key] = val

    return saved


def save_progress(progress: dict) -> None:
    """Write progress to file."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)
        f.write("\n")


def mark_complete(milestone_id: str) -> None:
    """Mark a milestone as completed with today's date."""
    progress = load_progress()
    if milestone_id in progress:
        progress[milestone_id]["completed"] = True
        progress[milestone_id]["completed_date"] = date.today().isoformat()
        save_progress(progress)


def is_completed(progress: dict, milestone_id: str) -> bool:
    return progress.get(milestone_id, {}).get("completed", False)


def get_completed_date(progress: dict, milestone_id: str) -> date | None:
    d = progress.get(milestone_id, {}).get("completed_date")
    if d:
        return datetime.strptime(d, "%Y-%m-%d").date()
    return None


def get_stats(progress: dict) -> tuple[int, int]:
    """Return (completed_count, total_count)."""
    total = len(ROADMAP)
    completed = sum(1 for m in ROADMAP if is_completed(progress, m["id"]))
    return completed, total
