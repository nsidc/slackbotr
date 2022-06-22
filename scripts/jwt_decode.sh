#!/bin/bash
set -eu

jwt="$1"
shift

if [ -z "$jwt" ]; then
    echo "JWT must be provided as only positional argument."
    exit 1
fi

THIS_DIR="$( cd "$( dirname "$0" )"; pwd -P )"
cd "${THIS_DIR}"
GIT_ROOT="$(git rev-parse --show-toplevel)"
cd "${GIT_ROOT}"

PYTHONPATH=. python -c \
    "from slackbotr.util.auth import decode_jwt; print(decode_jwt('${jwt}'))"
