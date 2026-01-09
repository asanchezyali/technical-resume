# Architecture

## System Overview

The Resume Generator Agent is a CLI tool that uses Claude AI to generate tailored LaTeX resumes from job descriptions.

```mermaid
graph TB
    subgraph Input
        JD[Job Description]
        MD[Master Data<br/>resume-master.json]
        TP[LaTeX Template]
        SP[System Prompt]
    end

    subgraph Processing
        LLM[Claude AI<br/>via LiteLLM]
        GEN[LaTeX Generator]
        FIX[Error Fixer]
    end

    subgraph Compilation
        TEX[.tex File]
        PDF[pdflatex]
    end

    subgraph Output
        RESUME[PDF Resume]
        README[README.md]
    end

    JD --> LLM
    MD --> LLM
    TP --> LLM
    SP --> LLM
    LLM --> GEN
    GEN --> TEX
    TEX --> PDF
    PDF -->|Success| RESUME
    PDF -->|Error| FIX
    FIX --> TEX
    MD --> README
```

## Component Architecture

```mermaid
classDiagram
    class CLI {
        +generate()
        +batch()
        +interactive()
        +compile()
        +readme()
    }

    class LLMHandler {
        -model: str
        -client: LiteLLM
        +generate_resume()
        +fix_latex_error()
        +adjust_resume()
    }

    class LatexCompiler {
        -output_dir: Path
        +compile()
        +get_output_paths()
    }

    class DataLoader {
        +load_master_data()
        +load_master_data_with_updated_years()
        +load_template()
        +load_prompt()
        +calculate_years_of_experience()
        +update_skill_years()
    }

    class MarkdownGenerator {
        +generate_readme()
    }

    CLI --> LLMHandler
    CLI --> LatexCompiler
    CLI --> DataLoader
    CLI --> MarkdownGenerator
```

## Data Flow

### Resume Generation Flow

```mermaid
sequenceDiagram
    participant User
    participant CLI as agent.py
    participant DL as DataLoader
    participant LLM as LLMHandler
    participant LC as LatexCompiler

    User->>CLI: generate -f job.txt

    CLI->>DL: load_master_data_with_updated_years()
    DL-->>CLI: master_data

    CLI->>DL: load_template()
    DL-->>CLI: latex_template

    CLI->>DL: load_prompt("system_prompt.txt")
    DL-->>CLI: system_prompt

    CLI->>LLM: generate_resume(job, data, template, prompt)
    Note over LLM: Claude analyzes job<br/>and selects relevant<br/>skills/experiences
    LLM-->>CLI: tex_content

    loop Up to 3 retries
        CLI->>LC: compile(tex_content, filename)
        alt Success
            LC-->>CLI: (True, "")
        else Error
            LC-->>CLI: (False, error_log)
            CLI->>LLM: fix_latex_error(tex_content, error_log)
            LLM-->>CLI: fixed_tex_content
        end
    end

    CLI-->>User: PDF path
```

### Years Calculation Flow

```mermaid
flowchart TD
    A[Load resume-master.json] --> B[update_skill_years]
    B --> C{For each skill}
    C --> D[Calculate: current_year - start_year]
    D --> E{years >= 5 AND<br/>in SHOW_YEARS?}
    E -->|Yes| F["display = 'Name (X+ years)'"]
    E -->|No| G["display = 'Name'"]
    F --> H{More skills?}
    G --> H
    H -->|Yes| C
    H -->|No| I[Return updated data]
```

## File Structure

```mermaid
graph TD
    subgraph Root
        A[agent.py]
        B[pyproject.toml]
        C[README.md]
    end

    subgraph src
        D[llm_handler.py]
        E[latex_compiler.py]
        F[data_loader.py]
        G[markdown_generator.py]
    end

    subgraph data
        H[resume-master.json]
    end

    subgraph templates
        I[example.tex]
        subgraph prompts
            J[system_prompt.txt]
        end
    end

    subgraph jobs
        K[*.txt / *.md files]
    end

    subgraph generated
        L[*.pdf]
        M[*.tex]
    end

    A --> src
    A --> data
    A --> templates
    A --> jobs
    A --> generated
```

## LLM Integration

The system uses LiteLLM as an abstraction layer for Claude API:

```mermaid
flowchart LR
    subgraph Application
        LH[LLMHandler]
    end

    subgraph LiteLLM
        LL[LiteLLM Client]
    end

    subgraph Anthropic
        C[Claude API]
    end

    LH -->|completion()| LL
    LL -->|HTTP POST| C
    C -->|Response| LL
    LL -->|Parsed response| LH
```

### Prompt Structure

```mermaid
graph TD
    subgraph System Message
        A[System Prompt]
        B[Instructions for<br/>resume generation]
        C[LaTeX constraints]
    end

    subgraph User Message
        D[Job Description]
        E[Master Data JSON]
        F[Example Template]
    end

    A --> G[Claude]
    B --> G
    C --> G
    D --> G
    E --> G
    F --> G
    G --> H[Generated LaTeX]
```

## Error Handling

### Self-Healing LaTeX Compilation

```mermaid
stateDiagram-v2
    [*] --> Generate
    Generate --> Compile

    Compile --> Success: Return code 0
    Compile --> Error: Return code != 0

    Success --> [*]

    Error --> CheckRetries
    CheckRetries --> Fix: attempts < 3
    CheckRetries --> Fail: attempts >= 3

    Fix --> Compile

    Fail --> [*]
```

The error fixing process:
1. Capture pdflatex error log
2. Send error log to Claude with original LaTeX
3. Claude returns corrected LaTeX
4. Retry compilation
5. Repeat up to 3 times

## Key Design Decisions

### 1. Single Source of Truth
All CV data is stored in `resume-master.json`. The LLM selects and tailors content but never invents information.

### 2. Direct LaTeX Generation
The LLM generates LaTeX directly (no Jinja2 templating). This gives Claude full control over formatting and structure.

### 3. Dynamic Years Calculation
Skill years are calculated at runtime from `start_year` fields, ensuring the CV is always current.

### 4. Self-Healing Compilation
LaTeX errors are automatically fixed by Claude, reducing manual intervention.

### 5. Batch Processing
Multiple job applications can be processed in one command, streamlining the job search workflow.
