#!/bin/bash

echo "🚀 Pushing HeaderMatrix HEAD-v1-final to GitHub..."

# Start clean
git init
git remote remove origin 2> /dev/null
git remote add origin https://github.com/MeatheadsMarketing/HeaderMatrix.git

# Stage and commit everything
git add .
git commit -m "📦 HEAD-v1-final: Push complete rebuild with all tabs, schemas, data, CI, and launcher files"

# Retag and push cleanly
git tag -d HEAD-v1 2> /dev/null
git push origin :refs/tags/HEAD-v1
git tag HEAD-v1
git push origin main --tags

echo "✅ GitHub push complete. HEAD-v1-final is now fully live."
