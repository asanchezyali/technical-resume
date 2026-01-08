import subprocess
from pathlib import Path

class LatexCompiler:
    def __init__(self, output_dir: str = "generated"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    # Compile .tex to .pdf, return (success, error_log)
    def compile(self, tex_content: str, filename: str = "resume-draft") -> tuple[bool, str]:
        # Use absolute paths to avoid cwd issues
        abs_output_dir = self.output_dir.absolute()
        tex_path = abs_output_dir / f"{filename}.tex"
        pdf_path = abs_output_dir / f"{filename}.pdf"

        # Write .tex file
        tex_path.write_text(tex_content, encoding="utf-8")

        # Run pdflatex twice (for references)
        try:
            for _ in range(2):
                result = subprocess.run(
                    [
                        "pdflatex",
                        "-interaction=nonstopmode",
                        f"-output-directory={abs_output_dir}",
                        str(tex_path)
                    ],
                    capture_output=True,
                    timeout=60
                )
        except subprocess.TimeoutExpired:
            return False, "Compilation timed out after 60 seconds"
        except FileNotFoundError:
            return False, "pdflatex not found. Please install TeX distribution."

        # Check if PDF was created
        if pdf_path.exists():
            self._cleanup(filename)
            return True, ""
        else:
            log_path = self.output_dir / f"{filename}.log"
            if log_path.exists():
                error_log = log_path.read_text(encoding="utf-8", errors="ignore")
                # Extract relevant error lines
                error_lines = [
                    line for line in error_log.split("\n")
                    if line.startswith("!") or "Error" in line
                ]
                return False, "\n".join(error_lines[:20]) if error_lines else error_log[-2000:]
            return False, result.stderr.decode(errors="ignore")

    def _cleanup(self, filename: str):
        # Remove auxiliary files, keep .tex and .pdf
        for ext in [".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".synctex.gz"]:
            aux_file = self.output_dir / f"{filename}{ext}"
            if aux_file.exists():
                aux_file.unlink()

    def get_output_paths(self, filename: str = "resume-draft") -> tuple[Path, Path]:
        # Return paths to .tex and .pdf files
        return (
            self.output_dir / f"{filename}.tex",
            self.output_dir / f"{filename}.pdf"
        )
