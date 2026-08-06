#!/bin/bash

set -e

PYTHON_BIN="${PYTHON_BIN:-python3}"

cd code
MPLCONFIGDIR="../.matplotlib-cache" "$PYTHON_BIN" SpectralO14_simulation.py
shasum -a 256 -c ARTIFACT_SHA256SUMS
cd ..

bash compile.sh
