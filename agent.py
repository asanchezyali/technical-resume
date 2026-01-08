import click
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from pathlib import Path

from src.llm_handler import LLMHandler
from src.latex_compiler import LatexCompiler
from src.data_loader import load_master_data_with_updated_years, load_template, load_prompt

console = Console()

@click.group()
def cli():
    # Resume Generator Agent - AI-powered CV generation
    pass

@cli.command()
@click.argument("job_description", required=False)
@click.option("--job-file", "-f", type=click.Path(exists=True), help="File with full job description")
@click.option("--output", "-o", default="resume-draft", help="Output filename (without extension)")
@click.option("--model", "-m", default="anthropic/claude-sonnet-4-20250514", help="LLM model to use")
def generate(job_description: str, job_file: str, output: str, model: str):
    # Generate resume for a job description
    # Load job description from file if provided
    if job_file:
        job_content = Path(job_file).read_text(encoding="utf-8")
        # Extract title from first line or filename
        first_line = job_content.strip().split("\n")[0][:50]
        console.print(Panel(f"[bold blue]Job File:[/] {job_file}\n[dim]{first_line}...[/]", title="Resume Generator"))
        job_description = job_content
    elif job_description:
        console.print(Panel(f"[bold blue]Target Role:[/] {job_description}", title="Resume Generator"))
    else:
        console.print("[red]Error: Provide JOB_DESCRIPTION or --job-file[/]")
        return

    llm = LLMHandler(model=model)
    compiler = LatexCompiler()

    master_data = load_master_data_with_updated_years()
    template = load_template()
    system_prompt = load_prompt("system_prompt.txt")

    # Generate LaTeX
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("Generating LaTeX with Claude...", total=None)

        tex_content = llm.generate_resume(
            job_description,
            master_data,
            template,
            system_prompt
        )

        progress.update(task, description="Compiling PDF...")

        # Compile with retry on error
        max_retries = 3
        for attempt in range(max_retries):
            success, error_log = compiler.compile(tex_content, output)

            if success:
                break
            else:
                if attempt < max_retries - 1:
                    progress.update(task, description=f"Fixing LaTeX error (attempt {attempt + 2})...")
                    tex_content = llm.fix_latex_error(tex_content, error_log)

    if success:
        tex_path, pdf_path = compiler.get_output_paths(output)
        console.print(f"\n[bold green]Resume generated successfully![/]")
        console.print(f"  [dim]PDF:[/] {pdf_path}")
        console.print(f"  [dim]TeX:[/] {tex_path}")
    else:
        console.print(f"\n[bold red]Failed to generate valid LaTeX after {max_retries} attempts[/]")
        console.print(f"[dim]Error:[/] {error_log[:500]}")

@cli.command()
@click.option("--model", "-m", default="anthropic/claude-sonnet-4-20250514", help="LLM model to use")
def interactive(model: str):
    # Interactive mode with feedback loop
    console.print(Panel("[bold]Interactive Resume Generator[/]", subtitle="Type 'quit' to exit"))

    job_description = Prompt.ask("\n[bold cyan]Target role/job description[/]")
    if job_description.lower() == "quit":
        return

    llm = LLMHandler(model=model)
    compiler = LatexCompiler()
    master_data = load_master_data_with_updated_years()
    template = load_template()
    system_prompt = load_prompt("system_prompt.txt")

    console.print("\n[yellow]Generating resume...[/]")
    tex_content = llm.generate_resume(job_description, master_data, template, system_prompt)

    iteration = 0
    while True:
        iteration += 1
        filename = f"resume-draft-v{iteration}"

        # Compile
        success, error_log = compiler.compile(tex_content, filename)

        if not success:
            console.print(f"[yellow]Compilation failed, attempting fix...[/]")
            tex_content = llm.fix_latex_error(tex_content, error_log)
            success, error_log = compiler.compile(tex_content, filename)

            if not success:
                console.print(f"[red]Could not fix LaTeX error:[/] {error_log[:300]}")
                if not Confirm.ask("Try regenerating from scratch?"):
                    break
                tex_content = llm.generate_resume(job_description, master_data, template, system_prompt)
                continue

        tex_path, pdf_path = compiler.get_output_paths(filename)
        console.print(f"\n[green]PDF generated:[/] {pdf_path}")

        # Ask for next action
        console.print("\n[bold]What would you like to do?[/]")
        console.print("  [cyan]1.[/] Done - keep this version")
        console.print("  [cyan]2.[/] Adjust - modify current resume")
        console.print("  [cyan]3.[/] Regenerate - start fresh with new job description")

        choice = Prompt.ask("Choice", choices=["1", "2", "3", "done", "adjust", "regenerate"], default="1")

        if choice in ["1", "done"]:
            console.print(f"\n[bold green]Final resume saved:[/] {pdf_path}")
            break
        elif choice in ["2", "adjust"]:
            feedback = Prompt.ask("[bold cyan]What would you like to change?[/]")
            console.print("[yellow]Adjusting resume...[/]")
            tex_content = llm.adjust_resume(tex_content, feedback, master_data)
        elif choice in ["3", "regenerate"]:
            job_description = Prompt.ask("[bold cyan]New target role[/]")
            console.print("[yellow]Regenerating resume...[/]")
            tex_content = llm.generate_resume(job_description, master_data, template, system_prompt)
            iteration = 0

@cli.command()
@click.option("--jobs-dir", "-d", default="jobs", help="Directory with job files")
@click.option("--model", "-m", default="anthropic/claude-sonnet-4-20250514", help="LLM model to use")
def batch(jobs_dir: str, model: str):
    # Generate resumes for all job files in a directory
    jobs_path = Path(jobs_dir)

    if not jobs_path.exists():
        console.print(f"[red]Directory not found: {jobs_dir}[/]")
        return

    job_files = list(jobs_path.glob("*.txt")) + list(jobs_path.glob("*.md"))

    if not job_files:
        console.print(f"[yellow]No job files found in {jobs_dir}/[/]")
        console.print("[dim]Add .txt or .md files with job descriptions[/]")
        return

    console.print(Panel(f"[bold]Batch Resume Generator[/]\nFound {len(job_files)} job files", title="Batch Mode"))

    llm = LLMHandler(model=model)
    compiler = LatexCompiler()
    master_data = load_master_data_with_updated_years()
    template = load_template()
    system_prompt = load_prompt("system_prompt.txt")

    results = []

    for job_file in job_files:
        job_name = job_file.stem
        console.print(f"\n[cyan]Processing:[/] {job_file.name}")

        job_content = job_file.read_text(encoding="utf-8")
        first_line = job_content.strip().split("\n")[0][:40]
        console.print(f"  [dim]{first_line}...[/]")

        try:
            # Generate
            tex_content = llm.generate_resume(job_content, master_data, template, system_prompt)

            # Compile with retry
            success = False
            for attempt in range(3):
                success, error_log = compiler.compile(tex_content, job_name)
                if success:
                    break
                tex_content = llm.fix_latex_error(tex_content, error_log)

            if success:
                _, pdf_path = compiler.get_output_paths(job_name)
                console.print(f"  [green]✓[/] {pdf_path}")
                results.append((job_name, "success", str(pdf_path)))
            else:
                console.print(f"  [red]✗[/] Failed to compile")
                results.append((job_name, "failed", error_log[:100]))
        except Exception as e:
            console.print(f"  [red]✗[/] Error: {e}")
            results.append((job_name, "error", str(e)))

    # Summary
    console.print("\n" + "="*50)
    console.print("[bold]Summary:[/]")
    success_count = sum(1 for r in results if r[1] == "success")
    console.print(f"  [green]Success:[/] {success_count}/{len(results)}")

    if success_count < len(results):
        console.print(f"  [red]Failed:[/] {len(results) - success_count}")
        for name, status, msg in results:
            if status != "success":
                console.print(f"    - {name}: {msg[:50]}")

@cli.command()
@click.argument("tex_file", type=click.Path(exists=True))
def compile(tex_file: str):
    # Compile an existing .tex file to PDF
    tex_path = Path(tex_file)
    tex_content = tex_path.read_text(encoding="utf-8")

    compiler = LatexCompiler(output_dir=str(tex_path.parent))
    filename = tex_path.stem

    console.print(f"[yellow]Compiling {tex_file}...[/]")
    success, error_log = compiler.compile(tex_content, filename)

    if success:
        _, pdf_path = compiler.get_output_paths(filename)
        console.print(f"[bold green]Compiled successfully:[/] {pdf_path}")
    else:
        console.print(f"[bold red]Compilation failed:[/]")
        console.print(error_log[:500])

if __name__ == "__main__":
    cli()
