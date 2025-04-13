#!/bin/bash

# git_stage_filemind_all.sh
# Quickly stages and commits all needed FILEMIND Phase 2 deployment files

echo "🚀 Staging all FILEMIND files for push..."

# Add core deploy files
git add filemind_dashboard.py

git add *.py
git add *.md
git add requirements.txt
git add .streamlit_config.toml
git add .gitignore

# Optional applet folder if using /pages
git add pages/

# Commit and push
git commit -m "🧠 Push all core FILEMIND deploy files and dashboard"
git push

echo "✅ Push complete."

