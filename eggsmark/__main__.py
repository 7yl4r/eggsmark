"""cmd line interface definition"""
import sys
import logging
from argparse import ArgumentParser

import eggsmark
from eggsmark.xmd_knit import main as knit


def parse_args(argvs):
    # =========================================================================
    parser = ArgumentParser(description='eggs-acutable markdown')

    # === arguments for the main command
    parser.add_argument(
        "-v", "--verbose",
        help="increase output verbosity",
        action="count",
        default=0
    )
    parser.add_argument(
        "-q", "--quiet",
        help="output only results",
        action="store_true"
    )
    parser.add_argument(
        "-V", "--version",
        help="print version & exit",
        action="store_true"
    )

    # =========================================================================
    # === subcommands
    # =========================================================================
    subparsers = parser.add_subparsers(
        title='subcommands',
        description='usage: `eggsmark $subcommand` ',
        help='addtnl help for subcommands: `eggsmark $subcommand -h`'
    )

    parser_knit = subparsers.add_parser(
        'knit',
        help='download file from data warehouse'
    )
    parser_knit.set_defaults(func=knit)
    parser_knit.add_argument(
        "input_path", help="input xmd"
    )
    parser_knit.add_argument(
        "output_path", help="output .html"
    )

    args = parser.parse_args(argvs)

    # =========================================================================
    # === set up logging behavior
    # =========================================================================
    if (args.verbose == 0):
        logging.basicConfig(level=logging.WARNING)
    elif (args.verbose == 1):
        logging.basicConfig(level=logging.INFO)
    else:  # } (args.verbose == 2){
        logging.basicConfig(level=logging.DEBUG)
    # =========================================================================

    if (
        getattr(args, 'version', False) is False and
        getattr(args, "func", None) is None
    ):
        SEP = "\n-------------------------------------------------------\n"
        print(SEP)
        parser.print_help()
        print(SEP)
        raise ValueError(
            "\n\n\tSubcommand is required. See help above."
        )

    return args


def _welcome_message():
    logger = logging.getLogger("eggsmark.{}".format(
        __name__,
    ))
    HELLO = '=== Eggs-acutable Markdown Tool v{} ==='.format(
        eggsmark.__version__
    )
    logger.info(HELLO)
    logger.info('=' * len(HELLO))


def main(argvs):
    args = parse_args(argvs)
    # config_logger(verbosity=args.verbose, quiet=args.quiet)

    _welcome_message()

    if getattr(args, 'version', False):
        print("v{}".format(eggsmark.__version__))
        exit()
    else:
        del args.version
        fn = args.func
        del args.func
        result = fn(**vars(args))
    return result


def _main():
    main(sys.argv[1:])

if __name__ == "__main__":
    _main()
