"""
Full roadmap data: phases, milestones, daily actions, and deadlines.
"""

from datetime import date

# Each milestone has an id, description, phase, start/end dates, daily_action (what to do each day),
# and optional deadline for one-off items.

ROADMAP = [
    # ── Phase 1: Now → May 2026 (Final Semester) ──
    {
        "id": "calc3",
        "phase": "spring-2026",
        "title": "Earn an A in Calculus 3",
        "daily_action": "3-5 Calc 3 practice problems (30 min)",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 8),
    },
    {
        "id": "linalg",
        "phase": "spring-2026",
        "title": "Earn an A in Linear Algebra",
        "daily_action": "3-5 Linear Algebra practice problems (30 min)",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 8),
    },
    {
        "id": "econ4960r",
        "phase": "spring-2026",
        "title": "ECON 4960R research project (quant-focused)",
        "daily_action": "45 min on research data/analysis/writing",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 8),
    },
    {
        "id": "clm_book",
        "phase": "spring-2026",
        "title": "CLM: Econometrics of Financial Markets",
        "daily_action": "5-10 pages CLM + derivations (30 min)",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 31),
    },
    {
        "id": "python_numpy_pandas",
        "phase": "spring-2026",
        "title": "Python NumPy & Pandas mastery",
        "daily_action": "One financial data exercise in NumPy/Pandas (30 min)",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 31),
    },
    {
        "id": "rust_book",
        "phase": "spring-2026",
        "title": "The Rust Programming Language (chapters 7-20)",
        "daily_action": "Read one section of the Rust book + code examples (30 min)",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 31),
    },
    {
        "id": "gre_prep_spring",
        "phase": "spring-2026",
        "title": "Start GRE prep",
        "daily_action": "30 min GRE quant problems or verbal review",
        "start": date(2026, 2, 1),
        "end": date(2026, 5, 31),
    },
    # ── Phase 2: June–August 2026 (Summer → Start at Brown Advisory) ──
    {
        "id": "diff_eq",
        "phase": "summer-2026",
        "title": "Differential Equations (MIT OCW 18.03)",
        "daily_action": "1 hr DiffEq lecture + problems",
        "start": date(2026, 6, 1),
        "end": date(2026, 8, 31),
    },
    {
        "id": "probability_ross",
        "phase": "summer-2026",
        "title": "Sheldon Ross: A First Course in Probability",
        "daily_action": "10-15 pages Ross + examples (45 min)",
        "start": date(2026, 6, 1),
        "end": date(2026, 8, 31),
    },
    {
        "id": "advanced_sql",
        "phase": "summer-2026",
        "title": "Advanced SQL — window functions, CTEs",
        "daily_action": "One LeetCode SQL problem (20 min)",
        "start": date(2026, 6, 1),
        "end": date(2026, 8, 31),
    },
    {
        "id": "scipy_statsmodels",
        "phase": "summer-2026",
        "title": "SciPy & statsmodels — regressions, GARCH, time series",
        "daily_action": "Implement one model in SciPy/statsmodels (30 min)",
        "start": date(2026, 6, 1),
        "end": date(2026, 8, 31),
    },
    {
        "id": "take_gre",
        "phase": "summer-2026",
        "title": "Take the GRE — target 169+ Quant",
        "daily_action": None,
        "deadline": date(2026, 8, 15),
        "start": date(2026, 6, 1),
        "end": date(2026, 8, 15),
    },
    {
        "id": "brown_start",
        "phase": "summer-2026",
        "title": "Start at Brown Advisory — crush first 90 days",
        "daily_action": "Show up, learn fast, build relationships",
        "start": date(2026, 7, 1),
        "end": date(2026, 9, 30),
    },
    {
        "id": "git_mastery",
        "phase": "summer-2026",
        "title": "Git & GitHub workflows mastery",
        "daily_action": "Practice Git workflows (branching, PRs, rebasing)",
        "start": date(2026, 6, 1),
        "end": date(2026, 7, 31),
    },
    # ── Phase 3: Sept–Dec 2026 (Building at Brown Advisory) ──
    {
        "id": "real_analysis",
        "phase": "fall-2026",
        "title": "Intro Real Analysis: Abbott's Understanding Analysis",
        "daily_action": "One section Abbott + proofs (45 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "shreve_vol1",
        "phase": "fall-2026",
        "title": "Shreve Vol I: Stochastic Calculus (discrete-time)",
        "daily_action": "Read + work through Shreve Vol I (45 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "hull_derivatives",
        "phase": "fall-2026",
        "title": "Hull: Options, Futures, and Other Derivatives",
        "daily_action": "One section Hull + problems (30 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "portfolio_theory",
        "phase": "fall-2026",
        "title": "Portfolio theory: Markowitz, Black-Litterman, factor investing",
        "daily_action": "Study portfolio theory concepts + implementation (30 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "cpp_oop",
        "phase": "fall-2026",
        "title": "C++ OOP — classes, templates, STL",
        "daily_action": "One C++ lesson (30 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "sklearn_ml",
        "phase": "fall-2026",
        "title": "Scikit-learn ML basics",
        "daily_action": "ML exercise: regression, classification, cross-validation (30 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "rec_letters",
        "phase": "fall-2026",
        "title": "Lock in rec letters: Prof Lastrapes + Brown Advisory CEO",
        "daily_action": None,
        "deadline": date(2026, 12, 15),
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 15),
    },
    {
        "id": "quant_projects",
        "phase": "fall-2026",
        "title": "Build quant projects (optimizer, Fama-French, momentum backtest)",
        "daily_action": "Work on quant project code (45 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "work_analytics",
        "phase": "fall-2026",
        "title": "Volunteer for portfolio analytics projects at work",
        "daily_action": "Look for analytics opportunities at Brown Advisory",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "work_python_tools",
        "phase": "fall-2026",
        "title": "Build Python tools that solve real problems at Brown Advisory",
        "daily_action": "Build/improve a Python tool for work (30 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    # ── Phase 4: Jan–March 2027 (Application Sprint) ──
    {
        "id": "sop_draft",
        "phase": "apps-2027",
        "title": "Draft and finalize Statement of Purpose",
        "daily_action": "Work on SoP drafts and revisions (45 min)",
        "start": date(2027, 1, 1),
        "end": date(2027, 2, 28),
    },
    {
        "id": "grinold_kahn",
        "phase": "apps-2027",
        "title": "Grinold & Kahn: Active Portfolio Management",
        "daily_action": "Read Grinold & Kahn (30 min)",
        "start": date(2027, 1, 1),
        "end": date(2027, 3, 31),
    },
    {
        "id": "portfolio_dashboard",
        "phase": "apps-2027",
        "title": "Interactive portfolio dashboard (Streamlit/Dash)",
        "daily_action": "Build portfolio dashboard (45 min)",
        "start": date(2027, 1, 1),
        "end": date(2027, 2, 28),
    },
    {
        "id": "app_gatech",
        "phase": "apps-2027",
        "title": "Submit Georgia Tech MSQCF application",
        "daily_action": None,
        "deadline": date(2027, 3, 1),
        "start": date(2027, 1, 1),
        "end": date(2027, 3, 1),
    },
    {
        "id": "app_others",
        "phase": "apps-2027",
        "title": "Submit NC State, UNC Charlotte, JHU applications",
        "daily_action": None,
        "deadline": date(2027, 3, 15),
        "start": date(2027, 1, 1),
        "end": date(2027, 3, 15),
    },
    {
        "id": "github_portfolio",
        "phase": "apps-2027",
        "title": "GitHub portfolio: 3+ well-documented quant repos",
        "daily_action": "Polish and document GitHub repos (30 min)",
        "start": date(2027, 1, 1),
        "end": date(2027, 3, 15),
    },
]

PHASES = {
    "spring-2026": {"label": "Spring 2026 — Final Semester", "start": date(2026, 1, 13), "end": date(2026, 5, 31)},
    "summer-2026": {"label": "Summer 2026 — Brown Advisory Start", "start": date(2026, 6, 1), "end": date(2026, 9, 30)},
    "fall-2026": {"label": "Fall 2026 — Building at Brown Advisory", "start": date(2026, 9, 1), "end": date(2026, 12, 31)},
    "apps-2027": {"label": "Jan–Mar 2027 — Application Sprint", "start": date(2027, 1, 1), "end": date(2027, 3, 31)},
}


def get_active_milestones(today: date) -> list[dict]:
    """Return milestones that are active on the given date (between start and end)."""
    return [m for m in ROADMAP if m["start"] <= today <= m["end"]]


def get_current_phase(today: date) -> str | None:
    """Return the phase key for today's date."""
    for key, phase in PHASES.items():
        if phase["start"] <= today <= phase["end"]:
            return key
    return None
