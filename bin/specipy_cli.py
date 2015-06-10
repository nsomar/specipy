#!/usr/bin/env python

import specipy, argparse, os


def parse():
    global parser, args
    parser = argparse.ArgumentParser(
        description='Display the parsed Kiwi spec in formatted text.')

    # parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('file', type=str,
                       help='kiwi file path')

    parsed_args = parser.parse_args()

    file = parsed_args.file

    if not os.path.exists(file):
        print "The provided file does not exist %s" % file
        exit(0)

    with open(file, "r") as open_file:
        parsed = specipy.SpecParser(open_file.read())
        print parsed.root.elements_description()
