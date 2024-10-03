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
EOF

# Extract and clean up Skills section
sed -n '/section{Technical Skills}/,/resumeSubHeadingListEnd/p' main.tex | 
sed '1d;$d' | 
sed 's/\\resumeItem{//g; s/}//g; s/\\textbf{//g; s/textbf{//g' |
sed 's/\\resumeSubHeadingListStart//g; s/\\resumeSubHeadingListEnd//g' |
sed 's/\\resumeSubHeadingList//g' |
sed '/^$/d' |
sed 's/^[ \t]*//' |
sed '/Programming Languages:/!s/:/:\n- /' |
sed '/Programming Languages:/!s/, /\n- /g' |
sed '/Programming Languages:/s/: /: /' |
sed '/Programming Languages:/s/, /, /g' >> README.md

# The PDF link will be added by the GitHub Action