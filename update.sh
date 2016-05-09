#!/bin/bash

branch="master"

# throw away compiled python files to prevent errors while `pull`ing
sudo rm -f *.pyc

git fetch origin
# Check which files have changed
DIFFLIST=$(git --no-pager diff --name-only "$branch..origin/$branch")
git pull
git fetch origin
git checkout "$branch"
git reset --hard "origin/$branch" && git clean -f -d

# Set permissions
chmod -R 744 ./*
