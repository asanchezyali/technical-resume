# Getting Started

## Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer
- pdflatex (for PDF compilation)
- Anthropic API key

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd technical-resume
```

### 2. Install Dependencies

```bash
uv sync
```

This installs all required packages:
- `litellm` - LLM API integration
- `click` - CLI framework
- `rich` - Terminal formatting

### 3. Set Up API Key

```bash
export ANTHROPIC_API_KEY=your-key-here
```

Or add to your shell profile (`~/.bashrc`, `~/.zshrc`):

```bash
echo 'export ANTHROPIC_API_KEY=your-key-here' >> ~/.zshrc
```

### 4. Install LaTeX (if not installed)

**macOS:**
```bash
brew install --cask mactex
```

**Ubuntu/Debian:**
```bash
sudo apt-get install texlive-full
```

**Windows:**
Download and install [MiKTeX](https://miktex.org/download)

## Verify Installation

```bash
# Check CLI is working
uv run python agent.py --help

# Check pdflatex
pdflatex --version
```

## Your First Resume

### 1. Create a Job Description File

Create `jobs/my-job.txt`:

```
Senior Python Developer
Company: TechCorp
Location: Remote

Requirements:
- 5+ years Python experience
- Django or FastAPI
- PostgreSQL
- Docker

Responsibilities:
- Build scalable APIs
- Mentor junior developers
```

### 2. Generate the Resume

```bash
uv run python agent.py generate -f jobs/my-job.txt -o my-resume
```

### 3. Check Output

Your resume will be in:
- `generated/my-resume.pdf` - The PDF
- `generated/my-resume.tex` - The LaTeX source

## Next Steps

- [CLI Reference](./cli-reference.md) - Learn all commands
- [Master Data Structure](./master-data.md) - Customize your CV data
- [Architecture](./architecture.md) - Understand how it works
