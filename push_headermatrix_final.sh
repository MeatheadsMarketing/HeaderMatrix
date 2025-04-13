#!/bin/bash

echo "🔧 Setting up GitHub push for HeaderMatrix HEAD-v1-final..."

# Ensure clean repo
git init
git remote remove origin 2> /dev/null
git remote add origin https://github.com/MeatheadsMarketing/HeaderMatrix.git

# Add everything and commit
git add .
git commit -m "🚀 Push HEAD-v1-final complete build with full structure"

# Delete old tag (if exists) and re-tag
git tag -d HEAD-v1 2> /dev/null
git push origin :refs/tags/HEAD-v1
git tag HEAD-v1
git push origin main --tags

echo "✅ GitHub push complete: HEAD-v1-final is live."
