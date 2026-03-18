import json
import os
from litellm import completion
from dotenv import load_dotenv
from src.data_loader import calculate_years_of_experience

load_dotenv()

class LLMHandler:
    def __init__(self, model: str = "anthropic/claude-sonnet-4-20250514"):
        self.model = model

    # Generate complete LaTeX resume
    def generate_resume(
        self,
        job_description: str,
        master_data: dict,
        template_tex: str,
        system_prompt: str
    ) -> str:
        user_prompt = self._build_generation_prompt(
            job_description,
            master_data,
            template_tex
        )

        response = completion(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=8000,
            temperature=0.3
        )

        return self._extract_latex(response)

    # Adjust resume based on user feedback
    def adjust_resume(
        self,
        current_tex: str,
        feedback: str,
        master_data: dict
    ) -> str:
        system_prompt = (
            "You are a resume expert. Adjust the LaTeX resume based on user feedback. "
            "Output only the complete modified .tex file, no explanations."
        )

        user_prompt = f"""Current resume:
```latex
{current_tex}
```

Master data available:
```json
{json.dumps(master_data, indent=2)}
```

Feedback: {feedback}

Generate the adjusted .tex file:"""

        response = completion(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=8000,
            temperature=0.3
        )

        return self._extract_latex(response)

    # Fix LaTeX compilation errors
    def fix_latex_error(self, tex_content: str, error_log: str) -> str:
        system_prompt = (
            "You are a LaTeX expert. Fix the compilation error in this .tex file. "
            "Output only the corrected .tex file, no explanations."
        )

        user_prompt = f"""LaTeX file with error:
```latex
{tex_content}
```

Compilation error:
```
{error_log}
```

Fix the error and output the corrected .tex file:"""

        response = completion(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=8000,
            temperature=0.1
        )

        return self._extract_latex(response)

    def _extract_latex(self, response) -> str:
        # Extract LaTeX from response, handling markdown code blocks
        content = response.choices[0].message.content.strip()

        # If it starts with \documentclass, it's already clean LaTeX
        if content.startswith("\\documentclass"):
            return content

        # Try to extract from code blocks
        if "```latex" in content:
            content = content.split("```latex", 1)[1].split("```", 1)[0]
        elif "```tex" in content:
            content = content.split("```tex", 1)[1].split("```", 1)[0]
        elif "```" in content:
            # Generic code block
            parts = content.split("```")
            if len(parts) >= 3:
                content = parts[1]
                # Remove language identifier if present
                lines = content.split("\n", 1)
                if len(lines) > 1 and lines[0].strip() in ("latex", "tex", ""):
                    content = lines[1]

        content = content.strip()

        # Final check: find \documentclass if there's text before it
        if not content.startswith("\\documentclass") and "\\documentclass" in content:
            idx = content.find("\\documentclass")
            content = content[idx:]

        return content

    def _build_generation_prompt(
        self,
        job_description: str,
        master_data: dict,
        template_tex: str
    ) -> str:
        # Calculate years of experience
        years = calculate_years_of_experience(master_data)

        # Build explicit list of all jobs that MUST appear
        experience = master_data.get("experience", [])
        jobs_list = "\n".join(
            f"  - {exp['title']} @ {exp['company']} ({exp['date_range']})"
            for exp in experience
        )

        return f"""TARGET ROLE: {job_description}

YEARS OF EXPERIENCE (use these exact numbers):
{json.dumps(years, indent=2)}

MASTER DATA:
{json.dumps(master_data, indent=2)}

EXAMPLE TEMPLATE (copy this exact LaTeX structure):
{template_tex}

TASK: Generate a .tex file for the target role. Copy the exact preamble and structure from the example template.

ALL JOBS THAT MUST APPEAR (do NOT skip any):
{jobs_list}
You MUST include a \\resumeSubheading for EACH of these {len(experience)} jobs. If you omit any, the resume is invalid.

IMPORTANT RULES:
1. Use years from YEARS OF EXPERIENCE above (e.g., "{years['software_development_display']} years")
2. Include ALL {len(experience)} jobs listed above — every single one must have its own \\resumeSubheading
3. Keep experiences in chronological order (most recent first) — do NOT reorder by relevance
4. For each job, select 3-4 most relevant bullet points

Changes to make:
- Role title in header (match the target role)
- Summary text (tailored to role, use correct years)
- Skills selection (6-9 most relevant categories)
- Experience order and bullet selection (include ALL {len(experience)} jobs)
- Project selection (2-3 most relevant)

Output the complete .tex file starting with \\documentclass:"""
