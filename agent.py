import shutil
from pathlib import Path

import click
from rich.console import Console

from src.latex_compiler import LatexCompiler

console = Console()

VARIANTS_DIR = Path("variants")
OUTPUT_DIR = Path("generated")

# Recruiter-facing filenames. Add a line here when a new variant is promoted.
VARIANT_LABELS = {
    "ai-engineer": "AIEngineer",
    "ai-fullstack": "AIFullStack",
    "product-engineer": "ProductEngineer",
    "senior-fullstack": "SeniorFullStack",
}

# AlejandroSanchezYaliAIEngineerACME.pdf -- company suffix omitted for the base variants
def output_name(variant: str, company: str | None = None) -> str:
    label = VARIANT_LABELS.get(variant, variant.replace("-", " ").title().replace(" ", ""))
    return f"AlejandroSanchezYali{label}{company or ''}"

def compile_tex(tex_path: Path) -> bool:
    compiler = LatexCompiler(output_dir=str(tex_path.parent))
    success, error_log = compiler.compile(tex_path.read_text(encoding="utf-8"), tex_path.stem)
    if not success:
        console.print(f"[bold red]Compilation failed:[/] {tex_path}")
        console.print(error_log[:500])
    return success

@click.group()
def cli():
    # Compile the curated CV variants in variants/
    pass

@cli.command()
@click.argument("tex_file", type=click.Path(exists=True))
def compile(tex_file: str):
    # Compile a single .tex file to PDF, next to the source
    tex_path = Path(tex_file)
    console.print(f"[yellow]Compiling {tex_file}...[/]")
    if not compile_tex(tex_path):
        raise SystemExit(1)
    console.print(f"[bold green]Compiled:[/] {tex_path.with_suffix('.pdf')}")

@cli.command()
@click.option("--company", "-c", default=None, help="Company suffix for the output filename")
@click.option("--variant", "-v", default=None, help="Build only this variant")
def build(company: str, variant: str):
    # Compile the variants and copy each PDF to generated/ under its recruiter-facing name
    OUTPUT_DIR.mkdir(exist_ok=True)
    names = [variant] if variant else sorted(VARIANT_LABELS)
    failed = False

    for name in names:
        tex_path = VARIANTS_DIR / f"{name}.tex"
        if not tex_path.exists():
            console.print(f"[bold red]No such variant:[/] {tex_path}")
            failed = True
            continue

        console.print(f"[yellow]Building {name}...[/]")
        if not compile_tex(tex_path):
            failed = True
            continue

        target = OUTPUT_DIR / f"{output_name(name, company)}.pdf"
        shutil.copy2(tex_path.with_suffix(".pdf"), target)
        console.print(f"[bold green]->[/] {target}")

    if failed:
        raise SystemExit(1)

if __name__ == "__main__":
    cli()
