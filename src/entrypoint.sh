#!/usr/bin/env bash

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python ${script_dir}/custom_inference_model_action.py "$@"
