"""Generate complete LaTeX CV from master data."""


def escape_latex(text: str) -> str:
    """Escape special LaTeX characters."""
    if not text:
        return ""
    replacements = [
        ("&", r"\&"),
        ("%", r"\%"),
        ("$", r"\$"),
        ("#", r"\#"),
        ("_", r"\_"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def generate_complete_cv(master_data: dict) -> str:
    """Generate complete LaTeX CV from master data."""
    personal = master_data["personal"]
    skills = master_data["skills"]
    experience = master_data["experience"]
    projects = master_data["projects"]
    education = master_data["education"]
    blog_posts = master_data.get("blog_posts", [])
    talks = master_data.get("talks", [])
    summary = master_data.get("summary_templates", {}).get("fullstack", "")

    lines = []

    # Document preamble
    lines.append(r"""\documentclass[letterpaper,11pt]{article}

\usepackage[left=0.75in,top=0.6in,right=0.75in,bottom=0.6in]{geometry}
\usepackage{hyperref}
\usepackage{fontawesome}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage[T1]{fontenc}
\usepackage{lmodern}

% Define custom colors
\definecolor{linkcolor}{HTML}{2b6cb0}
\definecolor{sectioncolor}{HTML}{1a365d}

% Configure hyperlinks
\hypersetup{
    colorlinks=true,
    linkcolor=linkcolor,
    filecolor=linkcolor,
    urlcolor=linkcolor,
}

% Custom section formatting
\titleformat{\section}
{\Large\bfseries\color{sectioncolor}}
{}{0em}
{\uppercase}[\titlerule]
\titlespacing*{\section}{0pt}{10pt}{4pt}

% Custom commands for entries
\newcommand{\resumeItem}[1]{\item #1}

\newcommand{\entryList}{\begin{itemize}[leftmargin=*,nosep]}
\newcommand{\entryListEnd}{\end{itemize}}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}
  \item[]
  \begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}l r}
    \textbf{#1} & #2 \\
    \textit{#3} & \textit{#4} \\
  \end{tabular*}
  \vspace{-5pt}
}

% Fix for FontAwesome warnings - protect icons from becoming bold
\newcommand{\normalfaCalendar}{{\mdseries\faCalendar}}
\newcommand{\normalfaEnvelope}{{\mdseries\faEnvelope}}
\newcommand{\normalfaLinkedin}{{\mdseries\faLinkedin}}
\newcommand{\normalfaGithub}{{\mdseries\faGithub}}
\newcommand{\normalfaGlobe}{{\mdseries\faGlobe}}
\newcommand{\normalfaExternalLink}{{\mdseries\faExternalLink}}
\newcommand{\normalfaYoutube}{{\mdseries\faYoutube}}

\clubpenalty=1000
\widowpenalty=1000

\begin{document}
""")

    # Header
    links = personal["links"]
    lines.append(r"\begin{center}")
    lines.append(rf"\textbf{{\Huge {escape_latex(personal['name'])}}}\\[0.2em]")
    lines.append(r"\textbf{\Large Full Stack Developer \& AI Specialist}\\[0.4em]")
    lines.append(r"\small")
    lines.append(rf"\normalfaCalendar\ \href{{{links['calendar']}}}{{\textsc{{Let's Connect}}}}")
    lines.append(r"")
    lines.append(r"\vspace{0.8em}")
    lines.append(rf"\normalfaEnvelope\ \href{{mailto:{personal['email']}}}{{{escape_latex(personal['email'])}}}  ~|~")
    lines.append(rf"\normalfaLinkedin\ \href{{{links['linkedin']}}}{{{links['linkedin_handle']}}} ~|~")
    lines.append(rf"\normalfaGithub\ \href{{{links['github']}}}{{{links['github_handle']}}}  ~|~")
    lines.append(rf"\normalfaGlobe\ \href{{{links['website']}}}{{{links['website_display']}}}")
    lines.append(r"\end{center}")
    lines.append("")

    # Summary
    lines.append(r"\section{Summary}")
    lines.append(escape_latex(summary))
    lines.append("")

    # Technical Skills
    lines.append(r"\section{Technical Skills}")
    lines.append(r"\begin{itemize}[leftmargin=*, itemsep=0pt]")

    # Languages
    langs = skills.get("languages", [])
    lang_items = []
    for lang in langs:
        if lang.get("years", 0) >= 5:
            lang_items.append(f"{lang['name']} ({lang['years']}+ years)")
        else:
            lang_items.append(lang["name"])
    lines.append(rf"  \item \textbf{{Languages:}} {', '.join(lang_items)}")

    # Frontend
    frontend = skills.get("frontend", [])
    fe_main = ["React.js", "Next.js", "Svelte", "TypeScript", "Tailwind CSS", "Redux", "Zustand", "Shadcn UI", "SASS"]
    fe_items = []
    for name in fe_main:
        skill = next((s for s in frontend if s["name"] == name), None)
        if skill:
            if skill.get("years", 0) >= 5:
                fe_items.append(f"{name} ({skill['years']}+ years)")
            else:
                fe_items.append(name)
    lines.append(rf"  \item \textbf{{Frontend:}} {', '.join(fe_items)}")

    # Backend
    backend = skills.get("backend", [])
    be_main = ["Django", "FastAPI", "Flask", "Node.js", "Express", "NestJS", "RESTful APIs", "GraphQL", "Microservices"]
    be_items = []
    for name in be_main:
        skill = next((s for s in backend if s["name"] == name), None)
        if skill:
            if skill.get("years", 0) >= 5 and name == "Node.js":
                be_items.append(f"{name} ({skill['years']}+ years)")
            else:
                be_items.append(name)
    lines.append(rf"  \item \textbf{{Backend:}} {', '.join(be_items)}")

    # AI/ML
    ai_ml = skills.get("ai_ml", [])
    ai_items = [s["name"] for s in ai_ml if s["name"] in ["LangChain", "LangGraph", "LLMs", "OpenAI API", "TensorFlow", "PyTorch", "Scikit-learn", "RAG", "Whisper"]]
    lines.append(rf"  \item \textbf{{AI/ML:}} {', '.join(ai_items)}")

    # Databases
    databases = skills.get("databases", [])
    db_items = [db["name"] for db in databases]
    lines.append(rf"  \item \textbf{{Databases:}} {', '.join(db_items)}")

    # Cloud/DevOps
    cloud = skills.get("cloud_devops", [])
    cloud_items = [s["name"] for s in cloud]
    lines.append(rf"  \item \textbf{{Cloud/DevOps:}} {', '.join(cloud_items)}")

    # Testing
    testing = skills.get("testing", [])
    test_items = [s["name"] for s in testing if s["name"] in ["Vitest", "Jest", "TDD", "Unit Testing", "Integration Testing"]]
    lines.append(rf"  \item \textbf{{Testing:}} {', '.join(test_items)}")

    # Software Engineering
    se = skills.get("software_engineering", [])
    se_items = [s["name"] for s in se if s["name"] in ["Clean Architecture", "SOLID principles", "Git", "Microservices"]]
    lines.append(rf"  \item \textbf{{Software Engineering:}} {', '.join(se_items)}")

    lines.append(r"\end{itemize}")
    lines.append("")

    # Experience
    lines.append(r"\section{Experience}")
    lines.append(r"\begin{itemize}[leftmargin=0pt, itemindent=0pt, label={}, itemsep=1pt]")

    for exp in experience:
        title = escape_latex(exp["title"])
        company = escape_latex(exp["company"])
        location = escape_latex(exp["location"])
        date_range = exp["date_range"]

        lines.append(r"\resumeSubheading")
        lines.append(rf"{{{title}}}{{{date_range}}}")
        lines.append(rf"{{{company}}}{{{location}}}")
        lines.append(r"\begin{itemize}[leftmargin=*, itemsep=0pt]")

        for highlight in exp.get("highlights", [])[:5]:  # Limit to 5 bullets
            text = highlight["text"] if isinstance(highlight, dict) else highlight
            lines.append(rf"    \item {escape_latex(text)}")

        lines.append(r"\end{itemize}")
        lines.append("")

    lines.append(r"\end{itemize}")
    lines.append("")

    # Projects
    lines.append(r"\section{Featured Projects}")
    lines.append(r"\begin{itemize}[leftmargin=*, itemsep=1pt]")

    for project in projects:
        name = escape_latex(project["name"])
        url = project["url"]
        lines.append(rf"    \item \textbf{{\href{{{url}}}{{{name} \normalfaExternalLink}}}}")
        lines.append(r"    \begin{itemize}[itemsep=0pt]")

        for highlight in project.get("highlights", [])[:2]:
            text = highlight["text"] if isinstance(highlight, dict) else highlight
            lines.append(rf"        \item {escape_latex(text)}")

        lines.append(r"    \end{itemize}")

    lines.append(r"\end{itemize}")
    lines.append("")

    # Technical Writing
    if blog_posts:
        lines.append(r"\section{Technical Writing}")
        lines.append(r"\begin{itemize}[leftmargin=*, itemsep=0pt]")
        for post in blog_posts:
            title = escape_latex(post["title"])
            url = post["url"]
            date = post["date"]
            lines.append(rf"    \item \textbf{{\href{{{url}}}{{{title}}}}} ({date})")
        lines.append(rf"    \item \href{{{links['website']}}}{{View more articles \normalfaExternalLink}}")
        lines.append(r"\end{itemize}")
        lines.append("")

    # Conference Talks
    if talks:
        lines.append(r"\section{Conference Talks}")
        lines.append(r"\begin{itemize}[leftmargin=*]")
        for talk in talks:
            title = escape_latex(talk["title"])
            url = talk["url"]
            year = talk["year"]
            lines.append(rf"    \item \textbf{{\href{{{url}}}{{{title} \normalfaYoutube}}}} ({year})")
            lines.append(r"    \begin{itemize}[itemsep=0pt]")
            for hl in talk.get("highlights", []):
                lines.append(rf"        \item {escape_latex(hl)}")
            lines.append(r"    \end{itemize}")
        lines.append(r"\end{itemize}")
        lines.append("")

    # Education
    lines.append(r"\section{Education}")
    lines.append(r"\begin{itemize}[leftmargin=0pt, itemindent=0pt, label={}]")

    for edu in education:
        degree = escape_latex(edu["degree"])
        institution = escape_latex(edu["institution"])
        location = escape_latex(edu["location"])
        date_range = edu["date_range"]
        lines.append(r"\resumeSubheading")
        lines.append(rf"{{{degree}}}{{{date_range}}}")
        lines.append(rf"{{{institution}}}{{{location}}}")
        lines.append("")

    lines.append(r"\end{itemize}")
    lines.append(r"\end{document}")

    return "\n".join(lines)
