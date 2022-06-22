#!/bin/bash
set -eu

THIS_DIR="$( cd "$( dirname "$0" )"; pwd -P )"
cd "${THIS_DIR}"
GIT_ROOT="$(git rev-parse --show-toplevel)"
cd "${GIT_ROOT}"

PYTHONPATH=. python -c \
    'from slackbotr.util.auth import generate_jwt; print(generate_jwt())'
