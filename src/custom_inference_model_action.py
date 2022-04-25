#!/usr/bin/env python
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--branch', required=True, help='The branch against which PRs take action')

args = parser.parse_args()
print(f'The main branch is: {args.branch}')

os.environ['new-model-created'] = "True"
os.environ['model-deleted'] = "False"
os.environ['new-model-version-created'] = "True"
os.environ['test-result'] = 'Test passed with success'
