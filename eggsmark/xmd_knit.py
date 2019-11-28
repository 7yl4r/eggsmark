#!/usr/bin/env python3
from subprocess import run
import os.path
import logging

SUPPORTED_LANGUAGES = ["python", "r"]


def _get_chunks(lines, n):
    with open(input_path, "r") as xmd_file:
        n = 0
        lines = xmd_file.readlines()
        print(lines)
        # _get_next_chunk(lines, n)
        # TODO:
        # 1. for each chunk
        #     0. inject EGGS.get() globals from other chunks?
        #     a. run the knitter(s)
        #     3. save EGGS.put() globals for other chunks?
        #     b. inject output
        while n < len(lines):
            start_line = lines[n]
            if start_line.startswith(r"```{"):  # if entering chunk
                language = start_line.split("}")[0].split(",")[0][4:]
                if language not in SUPPORTED_LANGUAGES:
                    raise ValueError(
                        "unknown programming language '{}'".format(language)
                    )
                else:
                    chunk_lines = []
                    while (
                        not lines[n+len(chunk_lines)].strip().endswith("```")
                    ):
                        chunk_lines.append(lines[n+len(chunk_lines)])
            else:
                n += 1  # next line


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
