#!/usr/bin/env python3
from subprocess import run
import os.path
import logging


def knit(
    input_path, output_path, verbose=0, quiet=False
):
    logger = logging.getLogger("eggsmark.{}".format(
        __name__,
    ))
    OUT_DIR, OUT_FILENAME = os.path.split(output_path)
    tmp_path = "/tmp/{}.Rmd".format(os.path.basename(input_path))
    logger.info("creating tmp files...")
    run([
        'cp',
        input_path,
        tmp_path
    ])
    logger.info("knitting...")

    # TODO: use _get_chunks here instead
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
