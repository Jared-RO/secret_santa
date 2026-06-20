#!/bin/bash}
set -e

# remember to run chmod +x run.sh to make this script executable
THIS_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}")"  >/dev/null 2>&1 && pwd )"
echo "Running from $THIS_DIR"

function install {
    python -m pip install --upgrade pip
    python -m pip install --editable "$THIS_DIR[dev]"
}

function build {
    python -m build --sdist --wheel "$THIS_DIR"
}

function code_checks {
    # /bin/bash "$THIS_DIR/check-code-quality.sh"
    # git add .
    pre-commit run --all-files --verbose
}

function clean {
    rm -rf dist build
    find .\
    -type d \
    \( \
        -name "*cache*" \
        -o -name "*.egg-info" \
        -o -name "*dist-info*" \
    \) \
    -not -path "./venv/*" \
    -exec rm -rf {} +
}


function publish:test {
    try-load-dotenv || true
    twine upload dist/* \
    --repository testpypi \
    --username __token__ \
    --password "$TESTPYPI_API_TOKEN" --verbose
}

function release {
    install
    clean
    code_checks
    build
}


TIMEFORMAT="Task completed in %3lR"
time ${@:-help}
