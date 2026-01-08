import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent

def load_master_data() -> dict:
    # Load resume master data from JSON
    data_path = BASE_DIR / "data" / "resume-master.json"
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

def calculate_years_of_experience(master_data: dict) -> dict:
    # Calculate years of experience from the earliest software dev job
    experiences = master_data.get("experience", [])

    # Filter to software development roles (exclude pure teaching if needed)
    dev_roles = ["lapzo-2025", "freelance-2024", "monadical-2021", "bcfort-2018"]
    teaching_role = "professor-2010"

    dev_start_dates = []
    teaching_start = None

    for exp in experiences:
        start_str = exp.get("start_date")
        if start_str:
            start_date = datetime.strptime(start_str, "%Y-%m-%d")
            if exp.get("id") in dev_roles:
                dev_start_dates.append(start_date)
            elif exp.get("id") == teaching_role:
                teaching_start = start_date

    now = datetime.now()

    # Calculate years since first dev job
    dev_years = 0
    if dev_start_dates:
        earliest_dev = min(dev_start_dates)
        dev_years = (now - earliest_dev).days / 365.25

    # Calculate years since teaching started (for ML/AI experience)
    teaching_years = 0
    if teaching_start:
        teaching_years = (now - teaching_start).days / 365.25

    return {
        "software_development": int(dev_years),
        "software_development_display": f"{int(dev_years)}+",
        "teaching_and_research": int(teaching_years),
        "teaching_display": f"{int(teaching_years)}+",
        "total_professional": int(teaching_years),
        "total_display": f"{int(teaching_years)}+"
    }

def update_skill_years(master_data: dict) -> dict:
    # Update skill years based on start_year and current year
    current_year = datetime.now().year

    # Only show years for main languages/frameworks (keeps CV clean)
    SHOW_YEARS = ["Python", "JavaScript", "TypeScript", "React.js", "Next.js", "Node.js"]

    for category in master_data.get("skills", {}):
        for skill in master_data["skills"][category]:
            if "start_year" in skill:
                # Calculate current years of experience
                years = current_year - skill["start_year"]
                skill["years"] = years
                # Only show years for main skills with 5+ years
                name = skill["name"]
                if name in SHOW_YEARS and years >= 5:
                    skill["display"] = f"{name} ({years}+ years)"
                else:
                    skill["display"] = name

    return master_data

def load_master_data_with_updated_years() -> dict:
    # Load master data and update skill years to current date
    data = load_master_data()
    return update_skill_years(data)

def load_template() -> str:
    # Load example LaTeX template
    template_path = BASE_DIR / "templates" / "example.tex"
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()

def load_prompt(filename: str) -> str:
    # Load prompt template by filename
    prompt_path = BASE_DIR / "templates" / "prompts" / filename
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()
