#!/usr/bin/env python3
import argparse
import os
import sys

from hackassembler import compiler


def main():
    parser = argparse.ArgumentParser(
        description='Hack Machine Language Assembler'
    )
    parser.add_argument('src_file', help='Source file to compile.')
    args = parser.parse_args()
    if not os.path.isfile(args.src_file):
        print('{0} file not found'.format(args.src_file))
        sys.exit(1)

    compiler_instance = compiler.Compiler(args.src_file)
    compiler_instance.compile()


if __name__ == '__main__':
    main()
