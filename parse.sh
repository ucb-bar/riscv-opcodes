#!/usr/bin/env bash

# This is a simple script to handle Python's venv nonsense.

set -e

# Create the virtual environment if it doesn't already exist.
if [ ! -e ".venv/bin/activate" ]; then
    echo "Creating venv"
    python3 -m venv ".venv"
fi

# Activate it
. ".venv/bin/activate"

# See https://github.com/microsoft/pyright/issues/6209#issuecomment-1772924061
# for why editable_mode=compat is required.
python3 -m pip install --config-settings editable_mode=compat --editable .

riscv_opcodes $@
