#!/usr/bin/env python
"""
generate_outdir creates a unique output directory based on
the template passed in.
"""
import os
import sys

def generate_outdir(template):
    parts = template.split('_')
    if len(parts) > 1 and parts[-1].isdigit():
        start = int(parts[-1]) + 1
        num_digits = len(parts[-1])
        prefix = '_'.join(parts[:-1]) + '_'
    else:
        start = 1
        num_digits = 4
        prefix = template
        if prefix[-1] != '_':
            prefix += '_'
    for index in range(start, start+10000):
        dirname = prefix + format(index, f'0{num_digits}d')
        if not os.path.exists(dirname):
            return dirname
    return template

print(generate_outdir(sys.argv[1]))

