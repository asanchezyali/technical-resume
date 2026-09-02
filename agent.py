import click
from pathlib import Path
from rich.console import Console

from src.latex_compiler import LatexCompiler

console = Console()

@click.group()
def cli():
    # Resume toolkit: compile the curated CV variants in variants/
    pass

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
        console.print("[bold red]Compilation failed:[/]")
        console.print(error_log[:500])
        raise SystemExit(1)

if __name__ == "__main__":
    cli()
