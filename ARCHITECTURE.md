# Resume Generator Agent - Architecture

## Executive Summary

Intelligent system for generating personalized CVs on demand using Claude AI via LiteLLM. The agent:
1. **Interprets** job requirements in natural language
2. **Selects** relevant data from master JSON based on job profile
3. **Generates** LaTeX directly using LLM with template reference
4. **Validates** compilation and allows iterative feedback
5. **Compiles** final PDF automatically

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    RESUME GENERATOR AGENT                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. INPUT: Natural language prompt                          │
│     "Need CV for AI Specialist at startup"                  │
│     "Senior Blockchain Developer at fintech"                │
│     "Full Stack with emphasis on ML and DevOps"             │
│                                                             │
│                         ↓                                   │
│                                                             │
│  2. LLM GENERATION: Claude generates LaTeX directly         │
│     Inputs:                                                 │
│     ├─ Job description / requirements                       │
│     ├─ Master data (resume-master.json)                     │
│     ├─ Template reference (main.tex example)                │
│     └─ System prompt with instructions                      │
│                                                             │
│     LLM decides:                                            │
│     ├─ Which skills to include and how to group them        │
│     ├─ Which experiences are most relevant                  │
│     ├─ Which highlights to select per experience            │
│     ├─ Which projects to feature                            │
│     ├─ Whether to include blog posts / talks                │
│     ├─ How to write the professional summary                │
│     └─ Outputs complete .tex file                           │
│                                                             │
│                         ↓                                   │
│                                                             │
│  3. VALIDATION: Compile and check                           │
│     ├─ Run pdflatex on generated .tex                       │
│     ├─ Check for compilation errors                         │
│     ├─ If errors → send back to LLM for fix                 │
│     └─ Output: resume-draft.tex + resume-draft.pdf          │
│                                                             │
│                         ↓                                   │
│                                                             │
│  4. HUMAN FEEDBACK: Iterative editing                       │
│     ┌──────────────────────────────────┐                    │
│     │ Changes?                         │                    │
│     │ 1. Perfect, save final PDF       │                    │
│     │ 2. Adjust content/emphasis       │                    │
│     │ 3. Regenerate from scratch       │                    │
│     └──────────────────────────────────┘                    │
│     └─ Feedback → Back to LLM (multi-turn conversation)     │
│                                                             │
│                         ↓                                   │
│                                                             │
│  5. OUTPUT: Final PDF                                       │
│     ├─ Save .tex and .pdf with descriptive name             │
│     ├─ Clean temporary files                                │
│     └─ Output: resume-{role}-{date}.pdf                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Why LLM-Generated LaTeX?

### Approach Comparison

| Approach | Pros | Cons |
|----------|------|------|
| **Jinja2 Templates** | Deterministic, no LaTeX errors, cheaper | Rigid, must handle all edge cases |
| **LLM Direct** | Flexible, adapts to content | Possible errors, more tokens |
| **Hybrid (chosen)** | Best of both - LLM intelligence + template consistency | Slightly more complex prompt |

### Hybrid Approach Benefits

1. **LLM as Template Engine**: Claude follows the example .tex structure while making intelligent content decisions
2. **Flexible Content Selection**: LLM decides what's relevant, not rigid filtering rules
3. **Natural Language Adjustments**: "Add more AI experience" works naturally
4. **Self-Healing**: If LaTeX fails, LLM can fix its own errors
5. **Simpler Codebase**: No Jinja2 layer, fewer dependencies

---

## File Structure

```
resume-agent/
│
├── agent.py                        # Main CLI entry point
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables (API keys)
│
├── data/
│   └── resume-master.json          # Single source of truth for all CV data
│
├── templates/
│   ├── example.tex                 # Reference template (copy of main.tex)
│   └── prompts/
│       ├── system_prompt.txt       # System instructions for Claude
│       └── generate_resume.txt     # Main generation prompt
│
├── generated/
│   ├── resume-draft.tex            # Latest generated LaTeX
│   ├── resume-draft.pdf            # Latest compiled PDF
│   └── archive/                    # Previous versions
│
├── src/
│   ├── __init__.py
│   ├── llm_handler.py              # LiteLLM integration (Claude API)
│   ├── latex_compiler.py           # pdflatex compilation + validation
│   └── data_loader.py              # Load master data and templates
│
└── tests/
    ├── test_llm_handler.py
    └── test_latex_compiler.py
```

---

## LiteLLM Integration

### Why LiteLLM?

- **Provider flexibility**: Easy switching between Claude, OpenAI, etc.
- **Consistent API**: Same code works across providers
- **Cost tracking**: Built-in token usage monitoring
- **Fallbacks**: Automatic retry with different models

### Configuration

```python
# src/llm_handler.py
from litellm import completion
from pathlib import Path
import os

class LLMHandler:
    def __init__(self):
        self.model = "claude-sonnet-4-20250514"

    # Generate complete LaTeX resume
    def generate_resume(
        self,
        job_description: str,
        master_data: dict,
        template_tex: str
    ) -> str:
        system_prompt = self._load_prompt("system_prompt.txt")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": self._build_generation_prompt(
                        job_description,
                        master_data,
                        template_tex
                    )
                }
            ],
            max_tokens=8000,
            temperature=0.3
        )

        return self._extract_latex(response)

    # Adjust resume based on feedback
    def adjust_resume(
        self,
        current_tex: str,
        feedback: str,
        master_data: dict
    ) -> str:
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a resume expert. Adjust the LaTeX resume based on user feedback. Output only the complete modified .tex file."
                },
                {
                    "role": "user",
                    "content": f"Current resume:\n```latex\n{current_tex}\n```\n\nMaster data available:\n```json\n{json.dumps(master_data, indent=2)}\n```\n\nFeedback: {feedback}\n\nGenerate the adjusted .tex file:"
                }
            ],
            max_tokens=8000,
            temperature=0.3
        )

        return self._extract_latex(response)

    # Fix LaTeX compilation errors
    def fix_latex_error(self, tex_content: str, error_log: str) -> str:
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a LaTeX expert. Fix the compilation error in this .tex file. Output only the corrected .tex file."
                },
                {
                    "role": "user",
                    "content": f"LaTeX file:\n```latex\n{tex_content}\n```\n\nCompilation error:\n```\n{error_log}\n```\n\nFix the error and output the corrected .tex file:"
                }
            ],
            max_tokens=8000,
            temperature=0.1
        )

        return self._extract_latex(response)

    def _extract_latex(self, response) -> str:
        # Extract LaTeX from response, handling markdown code blocks
        content = response.choices[0].message.content
        if "```latex" in content:
            content = content.split("```latex")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]
        return content.strip()

    def _load_prompt(self, filename: str) -> str:
        path = Path(__file__).parent.parent / "templates" / "prompts" / filename
        return path.read_text()

    def _build_generation_prompt(
        self,
        job_description: str,
        master_data: dict,
        template_tex: str
    ) -> str:
        return f"""Generate a tailored resume for this job:

## Job Description / Target Role:
{job_description}

## Master Data (all available information):
```json
{json.dumps(master_data, indent=2)}
```

## Template Reference (follow this exact LaTeX structure and styling):
```latex
{template_tex}
```

## Instructions:
1. Select the most relevant skills, experiences, and projects for this role
2. Write a compelling summary tailored to this specific job
3. Choose 3-4 highlights per experience that best match the job requirements
4. Include blog posts and talks only if relevant to the role
5. Follow the exact LaTeX structure from the template
6. Output ONLY the complete .tex file, no explanations

Generate the .tex file:"""
```

### Environment Variables

```bash
# .env
ANTHROPIC_API_KEY=sk-ant-...
LITELLM_LOG=DEBUG  # Optional: for debugging
```

### Model Options

| Model ID (LiteLLM) | Use Case |
|-------------------|----------|
| `claude-sonnet-4-20250514` | Default - best balance of speed/quality |
| `claude-opus-4-20250514` | Complex analysis requiring deep reasoning |
| `claude-3-haiku-20240307` | Quick iterations, cost-sensitive |

---

## LaTeX Compilation

```python
# src/latex_compiler.py
import subprocess
import tempfile
from pathlib import Path

class LatexCompiler:
    def __init__(self, output_dir: str = "generated"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    # Compile .tex to .pdf, return (success, error_log)
    def compile(self, tex_content: str, filename: str = "resume-draft") -> tuple[bool, str]:
        tex_path = self.output_dir / f"{filename}.tex"
        pdf_path = self.output_dir / f"{filename}.pdf"

        # Write .tex file
        tex_path.write_text(tex_content)

        # Run pdflatex twice (for references)
        for _ in range(2):
            result = subprocess.run(
                [
                    "pdflatex",
                    "-interaction=nonstopmode",
                    f"-output-directory={self.output_dir}",
                    str(tex_path)
                ],
                capture_output=True,
                timeout=30
            )

        # Check if PDF was created
        if pdf_path.exists():
            self._cleanup(filename)
            return True, ""
        else:
            log_path = self.output_dir / f"{filename}.log"
            error_log = log_path.read_text() if log_path.exists() else result.stderr.decode()
            return False, error_log

    def _cleanup(self, filename: str):
        # Remove auxiliary files
        for ext in [".aux", ".log", ".out", ".toc"]:
            aux_file = self.output_dir / f"{filename}{ext}"
            if aux_file.exists():
                aux_file.unlink()
```

---

## System Prompt

```text
# templates/prompts/system_prompt.txt

You are an expert resume writer and LaTeX specialist. Your task is to generate
tailored, professional resumes in LaTeX format.

## Your Capabilities:
- Select the most relevant information from master data for a specific job
- Write compelling, achievement-focused bullet points
- Create professional summaries that highlight key qualifications
- Structure content for maximum impact and ATS compatibility
- Generate valid, compilable LaTeX code

## Guidelines:
1. **Relevance**: Only include information relevant to the target role
2. **Achievements**: Focus on quantifiable achievements, not just responsibilities
3. **Keywords**: Include industry-relevant keywords naturally
4. **Length**: Keep to 1-2 pages maximum
5. **Format**: Follow the provided template structure exactly
6. **LaTeX**: Ensure all special characters are properly escaped

## Content Selection Rules:
- Skills: Include 6-8 most relevant skill categories
- Experience: Include 3-4 most relevant positions
- Highlights: 3-4 bullet points per position, most impactful first
- Projects: 2-3 most relevant projects
- Blog/Talks: Include only if directly relevant to the role

## LaTeX Best Practices:
- Escape special characters: & % $ # _ { } ~ ^
- Use proper spacing and formatting
- Ensure all environments are properly closed
- Keep consistent indentation

Output only the complete .tex file, no explanations or markdown.
```

---

## Master Data Schema

The `resume-master.json` contains all available information, categorized with tags for intelligent filtering by the LLM:

```json
{
  "personal": {
    "name": "...",
    "email": "...",
    "links": { "linkedin": "...", "github": "...", ... }
  },

  "skills": {
    "languages": [{ "name": "Python", "categories": ["ai", "backend"], "display": "Python (7+ years)" }],
    "frontend": [...],
    "backend": [...],
    "ai_ml": [...],
    ...
  },

  "experience": [
    {
      "id": "job-id",
      "title": "...",
      "company": "...",
      "date_range": "...",
      "categories": ["ai", "fullstack"],
      "highlights": [
        { "text": "...", "categories": ["ai", "leadership"] }
      ]
    }
  ],

  "projects": [...],
  "blog_posts": [...],
  "talks": [...],
  "education": [...],
  "summary_templates": { "ai": "...", "fullstack": "...", ... }
}
```

The LLM uses category tags to understand relevance but makes final selection decisions based on the full context of the job description.

---

## CLI Interface

```python
# agent.py
import click
from rich.console import Console
from rich.prompt import Prompt
from src.llm_handler import LLMHandler
from src.latex_compiler import LatexCompiler
from src.data_loader import load_master_data, load_template

console = Console()

@click.group()
def cli():
    pass

@cli.command()
@click.argument("job_description")
def generate(job_description: str):
    # Generate resume for job description
    console.print(f"[bold blue]Generating resume for:[/] {job_description}")

    llm = LLMHandler()
    compiler = LatexCompiler()

    master_data = load_master_data()
    template = load_template()

    # Generate LaTeX
    console.print("[yellow]Generating LaTeX with Claude...[/]")
    tex_content = llm.generate_resume(job_description, master_data, template)

    # Compile with retry on error
    max_retries = 3
    for attempt in range(max_retries):
        success, error_log = compiler.compile(tex_content)

        if success:
            console.print("[bold green]Resume generated successfully![/]")
            console.print(f"[dim]Output: generated/resume-draft.pdf[/]")
            return
        else:
            console.print(f"[yellow]Compilation failed, fixing (attempt {attempt + 1})...[/]")
            tex_content = llm.fix_latex_error(tex_content, error_log)

    console.print("[bold red]Failed to generate valid LaTeX after retries[/]")

@cli.command()
def interactive():
    # Interactive mode with feedback loop
    job_description = Prompt.ask("[bold]Target role/job description[/]")

    llm = LLMHandler()
    compiler = LatexCompiler()
    master_data = load_master_data()
    template = load_template()

    tex_content = llm.generate_resume(job_description, master_data, template)

    while True:
        success, error_log = compiler.compile(tex_content)

        if not success:
            tex_content = llm.fix_latex_error(tex_content, error_log)
            continue

        console.print("[green]PDF generated: generated/resume-draft.pdf[/]")

        choice = Prompt.ask(
            "What next?",
            choices=["done", "adjust", "regenerate"],
            default="done"
        )

        if choice == "done":
            break
        elif choice == "adjust":
            feedback = Prompt.ask("[bold]What would you like to change?[/]")
            tex_content = llm.adjust_resume(tex_content, feedback, master_data)
        elif choice == "regenerate":
            job_description = Prompt.ask("[bold]New target role[/]")
            tex_content = llm.generate_resume(job_description, master_data, template)

if __name__ == "__main__":
    cli()
```

---

## Dependencies

### requirements.txt

```txt
# LLM Integration
litellm>=1.40.0

# CLI
click>=8.1.7
rich>=13.7.0

# Environment
python-dotenv>=1.0.0

# Development
pytest>=8.0.0
```

---

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env

# Generate resume (one-shot)
python agent.py generate "AI Specialist at fintech startup"

# Interactive mode (with feedback loop)
python agent.py interactive
```

---

## Advantages

| Aspect | Benefit |
|--------|---------|
| **LLM Intelligence** | Claude makes smart content decisions |
| **Flexible** | Handles any job description naturally |
| **Self-healing** | Auto-fixes LaTeX errors |
| **Simple codebase** | No template engine layer |
| **Iterative** | Easy adjustments via natural language |
| **Single source of truth** | All data in resume-master.json |

---

## Future Roadmap

1. **MVP**: Generation + feedback loop
2. **v1.1**: Save versions with metadata
3. **v1.2**: Parse job posting URLs
4. **v1.3**: ATS keyword optimization
5. **v2.0**: Web interface
6. **v2.1**: Cover letter generation
