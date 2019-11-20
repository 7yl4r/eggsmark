#!/usr/bin/env python3
from argparse import ArgumentParser
import logging
import sys
from subprocess import run
import os.path

def parse_args(argv):
    # =========================================================================
    # === set up arguments
    # =========================================================================
    parser = ArgumentParser(description='short desc of projname goes here')

    # === arguments for the main command
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity",
        action="count",
        default=0
    )
    parser.add_argument(
        "input_path", help="input xmd"
    )
    parser.add_argument(
        "output_path", help="output .html"
    )

    args = parser.parse_args()
    # =========================================================================
    # === set up logging behavior
    # =========================================================================
    if (args.verbose == 0):
        logging.basicConfig(level=logging.WARNING)
    elif (args.verbose == 1):
        logging.basicConfig(level=logging.INFO)
    else:  # } (args.verbose == 2){
        logging.basicConfig(level=logging.DEBUG)

    return args


def main(*, input_path, output_path, verbose=0):
    OUT_DIR, OUT_FILENAME = os.path.split(output_path)
    tmp_path = "/tmp/{}.Rmd".format(os.path.basename(input_path))
    run([
        'cp',
        input_path,
        tmp_path
    ])
    result = run([
        'R',
        '-e',
        (
            'rmarkdown::render('
                '"{}", '
                'output_dir="{}", '
                'output_file="{}"'
            ')'
        ).format(tmp_path, OUT_DIR, OUT_FILENAME)
    ])
    print(result)
    # TODO: assert result is zero or...?


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(**vars(args))
