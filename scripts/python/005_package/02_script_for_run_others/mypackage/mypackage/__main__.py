# We will be creating the standalone script in a file called __main__.py that we place in the subdirectory containing the other Python modules:

import argparse
import sys
import os
import runpy
from datetime import datetime

from mypackage import capitalize


def main():
    parser = argparse.ArgumentParser(prog='capitalize')
    parser.add_argument('string', nargs='*', help='string to capitalize')
    parser.add_argument('-v', '--version', help='display version', action='version',
                        version=f'%(prog)s 1.0.0')
    args = parser.parse_args()

    if args.string:
        text = ' '.join(word for word in args.string)
        print(capitalize(text))
    else:
        parser.print_usage()
        sys.exit(1)

def now():
    return datetime.now().strftime('%Y-%m-%d %H:%m:%S')


def runner():
    version = '1.0.0'
    parser = argparse.ArgumentParser(prog='runner')
    parser.add_argument('script', help='Python script to run')
    parser.add_argument('-v', '--version', help='display version', action='version',
                        version=f'%(prog)s {version}')
    args = parser.parse_args()

    if args.script:
        print(f'{parser.prog} v{version} started on {now()}')
        # exec(compile(open(args.script).read(), os.path.basename(args.script), 'exec'))
        # exec(open(args.script).read())
        # The runpy module is used to locate and run Python modules without importing them first. Its main use is to implement the -m command line switch that allows scripts to be located using the Python module namespace rather than the filesystem.
        argparse.Namespace(**runpy.run_path(args.script))

        print(f'{parser.prog} v{version} finished on {now()}')
    else:
        parser.print_usage()
        sys.exit(1)


if __name__ == '__main__':
    sys.exit(main())