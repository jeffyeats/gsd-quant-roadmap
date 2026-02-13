#!/usr/bin/env python3
"""
Builds the daily reminder message and sends it via email-to-SMS gateway.
Usage:
    python send_reminder.py            # Send SMS
    python send_reminder.py --dry-run  # Print message, don't send
"""

import argparse
import os
import smtplib
import sys
from datetime import date, timedelta
from email.mime.text import MIMEText

from dotenv import load_dotenv

# Allow imports from src/
sys.path.insert(0, os.path.dirname(__file__))

from progress import get_stats, is_completed, load_progress
from roadmap import PHASES, ROADMAP, get_active_milestones, get_current_phase

MAX_SMS_LENGTH = 1600

MOTIVATIONAL_CLOSERS = [
    "The 3.1 doesn't define you. The work does.",
    "One day closer to quant. Go.",
    "Discipline > motivation. Every single day.",
    "You're building something most people won't even attempt.",
    "The gap between you and them is closing. Keep going.",
    "Future you is counting on today's work.",
    "Quant desks don't care about excuses. Put in the reps.",
    "Small daily gains compound. You know this.",
    "Nobody's coming to save you. That's your superpower.",
    "The math doesn't lie. Neither does the effort.",
    "Brown Advisory is step one. Georgia Tech is step two. Move.",
    "Every problem you solve today is one less standing in your way.",
    "Consistency beats talent when talent doesn't show up.",
    "The people who get in did the work. Be one of them.",
    "Read the page. Solve the problem. Ship the code. Repeat.",
    "You chose the hard path. Now walk it.",
    "Your competition is studying right now. Are you?",
    "Make today undeniable.",
    "Stack the days. That's all this is.",
    "The only shortcut is not stopping.",
    "169 Quant. Georgia Tech. It's all within reach if you grind.",
    "You're not behind. You're building from a different angle.",
    "This semester's A's are your application's foundation.",
    "Do the work nobody sees so you can do the work everybody wants.",
    "Math is the language. Learn to speak it fluently.",
    "One derivation at a time. One program at a time.",
    "You're not preparing for a job. You're building a career.",
    "The hard part isn't knowing what to do. It's doing it daily.",
    "Prove it with code. Prove it with math. Prove it with results.",
    "Clock in. No days off from the mission.",
    "Your brother's at the Naval Academy grinding. Match that energy.",
]


def get_closer(today: date) -> str:
    """Rotate motivational closers by day of year."""
    index = today.timetuple().tm_yday % len(MOTIVATIONAL_CLOSERS)
    return MOTIVATIONAL_CLOSERS[index]


def get_overdue(today: date, progress: dict) -> list[dict]:
    """Milestones past their end date that aren't completed."""
    overdue = []
    for m in ROADMAP:
        if is_completed(progress, m["id"]):
            continue
        end = m.get("deadline", m["end"])
        if end < today:
            overdue.append(m)
    return overdue


def get_upcoming_deadlines(today: date, progress: dict, days: int = 7) -> list[dict]:
    """Milestones with deadlines in the next N days that aren't completed."""
    upcoming = []
    window = today + timedelta(days=days)
    for m in ROADMAP:
        if is_completed(progress, m["id"]):
            continue
        deadline = m.get("deadline")
        end = m["end"]
        check_date = deadline if deadline else end
        if today <= check_date <= window:
            upcoming.append((m, check_date))
    return [(m, d) for m, d in sorted(upcoming, key=lambda x: x[1])]


def get_top_focus(today: date, progress: dict, count: int = 3) -> list[str]:
    """Get today's top focus tasks from active milestones with daily actions."""
    active = get_active_milestones(today)
    tasks = []
    for m in active:
        if is_completed(progress, m["id"]):
            continue
        if m.get("daily_action"):
            tasks.append(m["daily_action"])
    return tasks[:count]


def get_weekly_summary(today: date, progress: dict) -> str | None:
    """Monday-only: what was completed last week + this week's priorities."""
    if today.weekday() != 0:  # 0 = Monday
        return None

    week_ago = today - timedelta(days=7)
    lines = []

    # Completions last week
    completed_last_week = []
    for m in ROADMAP:
        entry = progress.get(m["id"], {})
        cd = entry.get("completed_date")
        if cd and week_ago.isoformat() <= cd <= today.isoformat():
            completed_last_week.append(m["title"])

    if completed_last_week:
        lines.append("LAST WEEK:")
        for t in completed_last_week:
            lines.append(f"  + {t}")
    else:
        lines.append("LAST WEEK: No items completed")

    # This week's active priorities
    active = get_active_milestones(today)
    active_incomplete = [m for m in active if not is_completed(progress, m["id"])]
    if active_incomplete:
        lines.append("THIS WEEK:")
        for m in active_incomplete[:5]:
            lines.append(f"  > {m['title']}")

    return "\n".join(lines)


def build_message(today: date) -> str:
    """Build the full SMS message for today."""
    progress = load_progress()
    parts = []

    # Header
    day_name = today.strftime("%A")
    date_str = today.strftime("%m/%d")
    phase_key = get_current_phase(today)
    phase_label = PHASES[phase_key]["label"] if phase_key else "Off-schedule"
    parts.append(f"{day_name} {date_str} | {phase_label}")

    # Weekly summary (Monday only)
    weekly = get_weekly_summary(today, progress)
    if weekly:
        parts.append("")
        parts.append(weekly)

    # Top 3 focus tasks
    focus = get_top_focus(today, progress)
    if focus:
        parts.append("")
        parts.append("TODAY:")
        for i, task in enumerate(focus, 1):
            parts.append(f"  {i}. {task}")

    # Overdue
    overdue = get_overdue(today, progress)
    if overdue:
        parts.append("")
        parts.append(f"OVERDUE ({len(overdue)}):")
        for m in overdue[:3]:
            parts.append(f"  ! {m['title']}")
        if len(overdue) > 3:
            parts.append(f"  ...+{len(overdue) - 3} more")

    # Upcoming deadlines
    upcoming = get_upcoming_deadlines(today, progress)
    if upcoming:
        parts.append("")
        parts.append("UPCOMING:")
        for m, d in upcoming[:3]:
            days_left = (d - today).days
            parts.append(f"  {m['title']} ({days_left}d)")

    # Progress
    completed, total = get_stats(progress)
    pct = int((completed / total) * 100) if total > 0 else 0
    parts.append("")
    parts.append(f"PROGRESS: {completed}/{total} milestones ({pct}%)")

    # Motivational closer
    parts.append("")
    parts.append(get_closer(today))

    message = "\n".join(parts)

    # Truncate if needed
    if len(message) > MAX_SMS_LENGTH:
        message = message[: MAX_SMS_LENGTH - 3] + "..."

    return message


def send_sms(message: str) -> None:
    """Send message via Gmail SMTP to AT&T email-to-SMS gateway."""
    gmail_user = os.environ["GMAIL_ADDRESS"]
    gmail_app_password = os.environ["GMAIL_APP_PASSWORD"]
    phone_number = os.environ["MY_PHONE_NUMBER"]

    # AT&T SMS gateway
    sms_gateway = f"{phone_number}@txt.att.net"

    msg = MIMEText(message)
    msg["From"] = gmail_user
    msg["To"] = sms_gateway

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_app_password)
        server.sendmail(gmail_user, sms_gateway, msg.as_string())

    print(f"SMS sent to {phone_number} via AT&T gateway")


def main():
    parser = argparse.ArgumentParser(description="Daily quant roadmap SMS reminder")
    parser.add_argument("--dry-run", action="store_true", help="Print message without sending")
    parser.add_argument("--date", type=str, help="Override date (YYYY-MM-DD) for testing")
    args = parser.parse_args()

    load_dotenv()

    if args.date:
        from datetime import datetime
        today = datetime.strptime(args.date, "%Y-%m-%d").date()
    else:
        today = date.today()

    message = build_message(today)

    if args.dry_run:
        print("=" * 50)
        print(message)
        print("=" * 50)
        print(f"\nCharacters: {len(message)}/{MAX_SMS_LENGTH}")
    else:
        send_sms(message)


if __name__ == "__main__":
    main()
