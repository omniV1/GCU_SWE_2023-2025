#!/bin/bash
# Run the MNIST Digit Recognition Streamlit app
# This script uses mise to ensure the correct Python version (3.12) is used

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Activate mise to use the correct Python version (3.12 - required for TensorFlow)
eval "$(mise activate bash)"

echo "Using Python: $(python --version)"
echo "Starting Streamlit app..."
echo ""

cd frontend
exec streamlit run app.py "$@"
