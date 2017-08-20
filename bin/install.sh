#!/usr/bin/env bash

if ! python --version | grep 'Python 3.6'; then
    echo "you must use Python 3.6 or above"
else
    pip install -r requirements.txt
fi
