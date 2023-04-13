from __future__ import annotations

import argparse
import fileinput
import os
import re
from typing import Sequence

PASS = 0
FAIL = 1

REGEX_OBSIDIAN_LINK = re.compile('\[\[.*\]\]')
REGEX_FILE = re.compile('.*\..*')


def find_file(name, path):
    # finds the first file with a matching name in the given directory
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith(name) and REGEX_FILE.match(file):
                return os.path.join(root, file)


def parse_link(link, root_file):
    # parses a link from Obsidian link format to standard Markdown link format
    link = link.strip('[]')
    link = link.split('|')
    link_name = link[0]
    file_name = link[-1]
    root_dir = os.getcwd()
    file_path = find_file(file_name, root_dir)
    if file_path:
        file_path = os.path.relpath(file_path, root_file)
        return f'[{link_name}]({file_path})'
    else:
        return None

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    for filename in args.filenames:
        if filename.endswith('.md'):
            with fileinput.input(filename, inplace=True) as f:
                for line in f:
                    for link in REGEX_OBSIDIAN_LINK.findall(line):
                        new_link = parse_link(link, filename)
                        if new_link:
                            line = line.replace(link, new_link)
                    print(line, end='')

    return PASS


if __name__ == '__main__':
    raise SystemExit(main())
