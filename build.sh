#!/bin/sh
# Собирает самодостаточный HTML из prototype.html (см. build.py)
cd "$(dirname "$0")" || exit 1
python3 build.py
