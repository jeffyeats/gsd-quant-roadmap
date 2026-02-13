# gsd-quant-roadmap

Daily SMS accountability system for a quant finance transition. Sends a 7:30 AM ET text with today's focus tasks, overdue items, upcoming deadlines, and progress stats.

## Setup

### 1. Twilio
- Create a [Twilio account](https://www.twilio.com/)
- Get a phone number with SMS capability
- Note your Account SID and Auth Token

### 2. Local Testing
```bash
cp .env.example .env
# Fill in your Twilio creds and phone number
pip install -r requirements.txt
python src/send_reminder.py --dry-run
```

### 3. GitHub Actions (automated daily SMS)
Add these as repo secrets in Settings → Secrets and variables → Actions:
- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `TWILIO_FROM_NUMBER`
- `MY_PHONE_NUMBER`

The workflow runs daily at 11:30 UTC (7:30 AM ET during EDT).

## Tracking Progress
Edit `data/progress.json` to mark items complete. Set any task's `completed` field to `true` and optionally add a `completed_date`.

## Message Format
- **Daily**: Top 3 focus tasks, overdue items, upcoming deadlines (7 days), overall progress
- **Monday**: Weekly summary — last week's completions, this week's priorities
- Motivational closer rotates daily
