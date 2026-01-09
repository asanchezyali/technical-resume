from datetime import datetime


def generate_readme(master_data: dict) -> str:
    """Generate README.md content from master data."""
    personal = master_data["personal"]
    skills = master_data["skills"]
    experience = master_data["experience"]
    projects = master_data["projects"]
    education = master_data["education"]
    blog_posts = master_data.get("blog_posts", [])
    talks = master_data.get("talks", [])

    lines = []

    # Header
    lines.append(f"# {personal['name']}\n")
    lines.append("**Full Stack Developer & AI Specialist**\n")

    # Badges
    links = personal["links"]
    lines.append(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-{links['linkedin_handle']}-blue?logo=linkedin)]({links['linkedin']})")
    lines.append(f"[![GitHub](https://img.shields.io/badge/GitHub-{links['github_handle']}-black?logo=github)]({links['github']})")
    lines.append(f"[![Website](https://img.shields.io/badge/Website-{links['website_display']}-green)]({links['website']})")
    lines.append(f"[![Email](https://img.shields.io/badge/Email-{personal['email'].replace('@', '%40')}-red?logo=gmail)](mailto:{personal['email']})")
    lines.append(f"[![Schedule](https://img.shields.io/badge/Schedule-Book%20a%20Call-orange)]({links['calendar']})\n")

    lines.append("---\n")

    # About Me
    lines.append("## About Me\n")
    summary = master_data.get("summary_templates", {}).get("ai", "")
    lines.append(f"{summary}\n")

    lines.append("---\n")

    # Technical Skills
    lines.append("## Technical Skills\n")

    # Languages
    lines.append("### Languages")
    lines.append("| Technology | Experience |")
    lines.append("|------------|------------|")
    for lang in skills.get("languages", []):
        years_display = f"{lang['years']}+ years" if lang['years'] >= 5 else f"{lang['years']} years"
        lines.append(f"| {lang['name']} | {years_display} |")
    lines.append("")

    # Frontend
    lines.append("### Frontend")
    frontend = skills.get("frontend", [])
    frameworks = [s["name"] for s in frontend if s["name"] in ["React.js", "Next.js", "Svelte"]]
    styling = [s["name"] for s in frontend if s["name"] in ["Tailwind CSS", "SASS", "Shadcn UI", "Ant Design"]]
    state = [s["name"] for s in frontend if s["name"] in ["Redux", "Zustand"]]
    graphics = [s["name"] for s in frontend if s["name"] in ["Three.js", "React Three Fiber"]]
    tools = [s["name"] for s in frontend if s["name"] in ["Vite", "Zod"]]

    # Add years to main frameworks
    frameworks_display = []
    for name in frameworks:
        skill = next((s for s in frontend if s["name"] == name), None)
        if skill and skill.get("years", 0) >= 5:
            frameworks_display.append(f"{name} ({skill['years']}+ years)")
        else:
            frameworks_display.append(name)

    lines.append(f"- **Frameworks:** {', '.join(frameworks_display)}")
    lines.append(f"- **Styling:** {', '.join(styling)}")
    lines.append(f"- **State Management:** {', '.join(state)}")
    lines.append(f"- **3D/Graphics:** {', '.join(graphics)}")
    lines.append(f"- **Tools:** Vite, Webpack, Zod\n")

    # Backend
    lines.append("### Backend")
    backend = skills.get("backend", [])
    python_be = [s["name"] for s in backend if s["name"] in ["Django", "Django REST Framework", "FastAPI", "Flask"]]
    node_be = [s["name"] for s in backend if s["name"] in ["Node.js", "Express", "NestJS"]]
    node_skill = next((s for s in backend if s["name"] == "Node.js"), None)
    node_years = f" ({node_skill['years']}+ years)" if node_skill and node_skill.get("years", 0) >= 5 else ""

    lines.append(f"- **Python:** {', '.join(python_be)}")
    lines.append(f"- **Node.js:** Node.js{node_years}, Express, NestJS")
    lines.append("- **APIs:** RESTful APIs, GraphQL, Microservices")
    lines.append("- **Payments:** Stripe\n")

    # AI/ML
    lines.append("### AI/ML")
    ai_ml = skills.get("ai_ml", [])
    dl = ["TensorFlow", "PyTorch", "JAX", "Flax"]
    ds = ["Scikit-learn", "Pandas", "NumPy"]
    llms = ["LangChain", "LangGraph", "OpenAI API", "LiteLLM", "RAG", "MCP"]
    speech = ["Whisper", "ElevenLabs API", "Azure Cognitive Services"]

    lines.append(f"- **Deep Learning:** {', '.join(dl)}")
    lines.append(f"- **Data Science:** {', '.join(ds)}")
    lines.append(f"- **LLMs:** {', '.join(llms)}")
    lines.append(f"- **Speech:** {', '.join(speech)}")
    lines.append("- **Automation:** n8n, WhatsApp Cloud API\n")

    # Databases
    lines.append("### Databases")
    databases = skills.get("databases", [])
    db_names = [db["name"] for db in databases]
    lines.append(f"{', '.join(db_names)}\n")

    # Cloud & DevOps
    lines.append("### Cloud & DevOps")
    cloud = skills.get("cloud_devops", [])
    cloud_providers = [s["name"] for s in cloud if s["name"] in ["AWS", "GCP", "IBM Cloud"]]
    lines.append(f"- **Cloud:** {', '.join(cloud_providers)}")
    lines.append("- **Containers:** Docker")
    lines.append("- **CI/CD:** GitHub Actions, CI/CD pipelines\n")

    # Blockchain
    lines.append("### Blockchain")
    blockchain = skills.get("blockchain", [])
    bc_names = [s["name"] for s in blockchain]
    lines.append(f"{', '.join(bc_names)}\n")

    # Testing
    lines.append("### Testing")
    testing = skills.get("testing", [])
    test_names = [s["name"] for s in testing]
    lines.append(f"{', '.join(test_names)}\n")

    # Software Engineering
    lines.append("### Software Engineering")
    se = skills.get("software_engineering", [])
    se_names = [s["name"] for s in se]
    lines.append(f"{', '.join(se_names)}\n")

    # Mathematics
    lines.append("### Mathematics")
    math = skills.get("mathematics", [])
    math_names = [s["name"] for s in math]
    lines.append(f"{', '.join(math_names)}\n")

    lines.append("---\n")

    # Professional Experience
    lines.append("## Professional Experience\n")

    for exp in experience:
        lines.append(f"### {exp['title']} @ {exp['company']}")
        lines.append(f"**{exp['date_range']}** | {exp['location']}\n")
        lines.append(f"*Technologies: {', '.join(exp['technologies'])}*\n")
        for highlight in exp.get("highlights", []):
            text = highlight["text"] if isinstance(highlight, dict) else highlight
            lines.append(f"- {text}")
        lines.append("\n---\n")

    # Featured Projects
    lines.append("## Featured Projects\n")

    for project in projects:
        lines.append(f"### [{project['name']}]({project['url']})")
        lines.append(f"*{', '.join(project['technologies'])}*\n")
        for highlight in project.get("highlights", [])[:2]:
            text = highlight["text"] if isinstance(highlight, dict) else highlight
            lines.append(f"{text}")
        lines.append("\n---\n")

    # Talks & Publications
    lines.append("## Talks & Publications\n")

    if talks:
        lines.append("### Conference Talks")
        for talk in talks:
            lines.append(f"- **[{talk['title']}]({talk['url']})** -- {talk['event']} {talk['year']}")
        lines.append("")

    if blog_posts:
        lines.append("### Blog Posts")
        for post in blog_posts:
            lines.append(f"- [{post['title']}]({post['url']}) -- {post['date']}")
        lines.append("")

    lines.append("---\n")

    # Education
    lines.append("## Education\n")

    for edu in education:
        lines.append(f"**{edu['degree']}**")
        lines.append(f"{edu['institution']} | {edu['location']} | {edu['date_range']}\n")

    lines.append("---\n")

    # Let's Connect
    lines.append("## Let's Connect\n")
    lines.append("I'm always open to discussing new opportunities, collaborations, or interesting projects.\n")
    lines.append(f"- [Schedule a Call]({links['calendar']})")
    lines.append(f"- [LinkedIn]({links['linkedin']})")
    lines.append(f"- [GitHub]({links['github']})")
    lines.append(f"- [Website]({links['website']})")
    lines.append(f"- Email: {personal['email']}")

    return "\n".join(lines)
