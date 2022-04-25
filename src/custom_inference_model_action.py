#!/usr/bin/env python
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--branch', required=True, help='The branch against which PRs take action')

args = parser.parse_args()
print(f'The main branch is: {args.branch}')
print(f'GITHUB_WORKSPACE: {os.environ["GITHUB_WORKSPACE"]}')

print('::set-output name=new-model-created::True')
print('::set-output name=model-deleted::False')
print('::set-output name=new-model-version-created::True')
print('::set-output name=test-result::The test passed with success.')
