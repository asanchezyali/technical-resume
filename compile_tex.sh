#!/bin/zsh

# compile_tex.sh - LaTeX compilation and cleanup script
# This script compiles all .tex files and removes temporary files
# while preserving .tex, .pdf, and .sh files

echo "=== LaTeX Compilation and Cleanup Script ==="
echo ""

# Function to compile a single tex file
compile_tex() {
    local tex_file=$1
    local filename=$(basename "$tex_file" .tex)
    
    echo "Compiling $tex_file..."
    
    # Run pdflatex twice to resolve references properly
    pdflatex -interaction=nonstopmode "$tex_file"
    pdflatex -interaction=nonstopmode "$tex_file"
    
    if [ -f "${filename}.pdf" ]; then
        echo "✓ Successfully created ${filename}.pdf"
    else
        echo "✗ Failed to create ${filename}.pdf"
    fi
}

# Function to clean up temporary files for a specific file
cleanup_file() {
    local filename=$(basename "$1" .tex)
    
    # Remove auxiliary files but keep .tex, .pdf, and .sh
    rm -f "${filename}.aux" "${filename}.log" "${filename}.out" \
          "${filename}.toc" "${filename}.lof" "${filename}.lot" \
          "${filename}.fls" "${filename}.fdb_latexmk" "${filename}.synctex.gz" \
          "${filename}.bbl" "${filename}.blg" "${filename}.nav" \
          "${filename}.snm" "${filename}.vrb"
}

# Compile and clean up a specific file if provided as argument
if [ $# -gt 0 ]; then
    for file in "$@"; do
        if [ -f "$file" ] && [[ "$file" == *.tex ]]; then
            compile_tex "$file"
            cleanup_file "$file"
        else
            echo "Error: $file is not a valid .tex file"
        fi
    done
else
    # Compile and clean up all .tex files in the current directory
    for tex_file in *.tex; do
        if [ -f "$tex_file" ]; then
            compile_tex "$tex_file"
            cleanup_file "$tex_file"
        fi
    done
fi

echo ""
echo "=== Cleanup Complete ==="
echo "Preserved files: .tex, .pdf, and .sh"
