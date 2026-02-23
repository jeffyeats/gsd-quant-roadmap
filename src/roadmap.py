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
        "title": "Crawl core: Finish Calculus 3 strong (target A)",
        "daily_action": "3-5 Calc 3 practice problems (30 min)",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 8),
    },
    {
        "id": "linalg",
        "phase": "spring-2026",
        "title": "Crawl core: Finish Linear Algebra strong (target A)",
        "daily_action": "3-5 Linear Algebra practice problems (30 min)",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 8),
    },
    {
        "id": "econ4960r",
        "phase": "spring-2026",
        "title": "Crawl core: Finish ECON 4960R (quant-focused research)",
        "daily_action": "45 min on research data/analysis/writing",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 8),
    },
    {
        "id": "hull_derivatives_spring",
        "phase": "spring-2026",
        "title": "Crawl core: Finish Hull (first pass + problems)",
        "daily_action": "10-20 pages Hull + notes/problems (30-45 min)",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 31),
    },
    {
        "id": "python_numpy_pandas",
        "phase": "spring-2026",
        "title": "Crawl support: Python for quant workflows (NumPy/Pandas basics)",
        "daily_action": "One financial data exercise in NumPy/Pandas (30 min)",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 31),
    },
    {
        "id": "rust_book",
        "phase": "spring-2026",
        "title": "Crawl core: Finish Rust book + build chapter projects",
        "daily_action": "Rust book + code-along + one exercise/project rep (30-45 min)",
        "start": date(2026, 1, 13),
        "end": date(2026, 5, 31),
    },
    {
        "id": "gre_prep_spring",
        "phase": "spring-2026",
        "title": "Crawl support: Start GRE prep (consistency phase)",
        "daily_action": "30 min GRE quant problems or verbal review",
        "start": date(2026, 2, 1),
        "end": date(2026, 5, 31),
    },
    # ── Phase 2: June–August 2026 (Summer → Start at Brown Advisory) ──
    {
        "id": "diff_eq",
        "phase": "summer-2026",
        "title": "Walk [Math]: Differential Equations (MIT OCW 18.03, ODE intuition + reps)",
        "daily_action": "45-60 min DiffEq lecture/problems + short derivation notes",
        "start": date(2026, 6, 1),
        "end": date(2026, 8, 31),
    },
    {
        "id": "probability_ross",
        "phase": "summer-2026",
        "title": "Walk [Math]: Probability (Ross) + problem solving for interviews/coursework",
        "daily_action": "Ross reading + 5-10 probability problems (45 min)",
        "start": date(2026, 6, 1),
        "end": date(2026, 8, 31),
    },
    {
        "id": "advanced_sql",
        "phase": "summer-2026",
        "title": "Walk [Coding]: Advanced SQL (CTEs, window functions, analytics queries)",
        "daily_action": "One LeetCode SQL problem (20 min)",
        "start": date(2026, 6, 1),
        "end": date(2026, 8, 31),
    },
    {
        "id": "scipy_statsmodels",
        "phase": "summer-2026",
        "title": "Walk [Coding]: SciPy + statsmodels (regression, time series, GARCH)",
        "daily_action": "Implement one regression/time-series/stat model (30-45 min)",
        "start": date(2026, 6, 1),
        "end": date(2026, 8, 31),
    },
    {
        "id": "numerical_methods",
        "phase": "summer-2026",
        "title": "Walk [Math]: Numerical methods foundations (root finding, optimization, Monte Carlo)",
        "daily_action": "One numerical methods concept + implementation rep (30-45 min)",
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
        "title": "Walk [Coding]: Git/GitHub workflows mastery",
        "daily_action": "Practice Git workflows + cleaner commit habits (20-30 min)",
        "start": date(2026, 6, 1),
        "end": date(2026, 7, 31),
    },
    # ── Phase 3: Sept–Dec 2026 (Building at Brown Advisory) ──
    {
        "id": "real_analysis",
        "phase": "fall-2026",
        "title": "Walk [Math]: Real Analysis foundations (Abbott, selected sections)",
        "daily_action": "Abbott reading + proof practice (45 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "shreve_vol1",
        "phase": "fall-2026",
        "title": "Walk [Math]: Shreve Vol I (discrete-time stochastic calculus)",
        "daily_action": "Shreve reading + worked examples/notes (45 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "hull_derivatives",
        "phase": "fall-2026",
        "title": "Walk [Finance]: Hull second pass (deeper chapters + harder problems)",
        "daily_action": "One section Hull + worked problems + formula notes (30-45 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "portfolio_theory",
        "phase": "fall-2026",
        "title": "Walk [Finance]: Portfolio theory (Markowitz, Black-Litterman, factors)",
        "daily_action": "Portfolio theory study + small implementation reps (30-45 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "cpp_oop",
        "phase": "fall-2026",
        "title": "Walk [Coding]: C++ for quant (OOP, STL, templates)",
        "daily_action": "C++ practice (syntax + STL/problem) (30 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "sklearn_ml",
        "phase": "fall-2026",
        "title": "Walk [Coding]: Numerical methods / optimization / ML basics (SciPy + sklearn)",
        "daily_action": "Alternate days: optimization/numerical methods and ML exercises (30-45 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "stochastic_processes_intro",
        "phase": "fall-2026",
        "title": "Walk [Math]: Stochastic processes intro (Markov chains, Brownian motion intuition)",
        "daily_action": "Stochastic processes reading + notes/problem rep (30-45 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "rec_letters",
        "phase": "fall-2026",
        "title": "Run prep: Lock recommendation letters (faculty + work)",
        "daily_action": None,
        "deadline": date(2026, 12, 15),
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 15),
    },
    {
        "id": "quant_projects",
        "phase": "fall-2026",
        "title": "Walk [Projects] -> Run bridge: Build quant projects (optimizer, factor/momentum backtests)",
        "daily_action": "Quant project coding + writeup progress (45-60 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "work_analytics",
        "phase": "fall-2026",
        "title": "Walk [Projects]: Portfolio analytics projects at work",
        "daily_action": "Look for analytics opportunities at Brown Advisory",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    {
        "id": "work_python_tools",
        "phase": "fall-2026",
        "title": "Walk [Projects]: Python tools that solve real problems at Brown Advisory",
        "daily_action": "Build/improve a Python tool for work (30 min)",
        "start": date(2026, 9, 1),
        "end": date(2026, 12, 31),
    },
    # ── Phase 4: Jan–March 2027 (Application Sprint) ──
    {
        "id": "sop_draft",
        "phase": "apps-2027",
        "title": "Run (MFE apps): Draft and finalize Statement of Purpose",
        "daily_action": "SoP drafting/revisions + school-specific tailoring (45 min)",
        "start": date(2027, 1, 1),
        "end": date(2027, 2, 28),
    },
    {
        "id": "grinold_kahn",
        "phase": "apps-2027",
        "title": "Run reading: Grinold & Kahn (support portfolio/risk project depth)",
        "daily_action": "Read + extract ideas for projects/interviews (30 min)",
        "start": date(2027, 1, 1),
        "end": date(2027, 3, 31),
    },
    {
        "id": "portfolio_dashboard",
        "phase": "apps-2027",
        "title": "Run project: Interactive portfolio dashboard (Streamlit/Dash)",
        "daily_action": "Build/polish dashboard + docs/screenshots (45 min)",
        "start": date(2027, 1, 1),
        "end": date(2027, 2, 28),
    },
    {
        "id": "app_gatech",
        "phase": "apps-2027",
        "title": "Run (MFE apps): Submit Georgia Tech MSQCF application",
        "daily_action": None,
        "deadline": date(2027, 3, 1),
        "start": date(2027, 1, 1),
        "end": date(2027, 3, 1),
    },
    {
        "id": "app_others",
        "phase": "apps-2027",
        "title": "Run (MFE apps): Submit NC State, UNC Charlotte, JHU applications",
        "daily_action": None,
        "deadline": date(2027, 3, 15),
        "start": date(2027, 1, 1),
        "end": date(2027, 3, 15),
    },
    {
        "id": "github_portfolio",
        "phase": "apps-2027",
        "title": "Run deliverable: GitHub portfolio (3+ well-documented quant repos)",
        "daily_action": "Polish repos, READMEs, and project writeups (30-45 min)",
        "start": date(2027, 1, 1),
        "end": date(2027, 3, 15),
    },
    {
        "id": "quant_interview_prep",
        "phase": "apps-2027",
        "title": "Run prep: Quant interview drills (probability, stats, coding, market intuition)",
        "daily_action": "45 min quant interview drills (probability/stats/coding/finance)",
        "start": date(2027, 1, 1),
        "end": date(2027, 3, 31),
    },
    {
        "id": "mfe_application_assets",
        "phase": "apps-2027",
        "title": "Run deliverable: MFE application assets (resume, project summaries, coding writeups)",
        "daily_action": "Polish resume + project summaries + application short answers (30-45 min)",
        "start": date(2027, 1, 1),
        "end": date(2027, 3, 31),
    },
]

PHASES = {
    "spring-2026": {"label": "Crawl — Foundations (Spring 2026)", "start": date(2026, 1, 13), "end": date(2026, 5, 31)},
    "summer-2026": {"label": "Walk — Core Quant Buildout I (Summer 2026)", "start": date(2026, 6, 1), "end": date(2026, 9, 30)},
    "fall-2026": {"label": "Walk — Core Quant Buildout II (Fall 2026)", "start": date(2026, 9, 1), "end": date(2026, 12, 31)},
    "apps-2027": {"label": "Run — Quant Projects + MFE Applications (Jan–Mar 2027)", "start": date(2027, 1, 1), "end": date(2027, 3, 31)},
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
