#!/bin/bash

# Create or overwrite README.md
cat << EOF > README.md
# Alejandro Sánchez Yalí - Sr. Full Stack Developer

Last updated: $1

## Summary
EOF

# Extract and clean up Summary section
sed -n '/section\*{Summary}/,/section{/p' main.tex | 
sed '1d;$d' | 
sed 's/\\//g' >> README.md

# Add Skills section
cat << EOF >> README.md

## Skills

Programming Languages: Python, JavaScript, TypeScript, Rust, C++, C
Frameworks & Libraries: Django, React, TensorFlow, PyTorch, JAX
Technologies: AI, Blockchain, Machine Learning, Natural Language Processing
Databases: MongoDB, MySQL
Cloud Platforms: AWS, GCP
EOF

# The PDF link will be added by the GitHub Action