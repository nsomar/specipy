#!/usr/bin/env python

import argparse


def parse():
    global parser, args
    parser = argparse.ArgumentParser(
        description='Start a mock server that reads input yaml res from inout directory.')

    parser.add_argument('--port',
                        default=9090, type=int,
                        help='Selects the port desired.')

    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--proxy', '-x', action='count')


    parsed_args = parser.parse_args()
    print parsed_args.port
    return parsed_args