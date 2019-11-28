#!/usr/bin/env python3
from subprocess import run
import os.path
import logging

from eggsmark.get_chunks import get_chunks


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

    # TDOO: DO THIS:
    # with open(input_path) as f_obj:
    #     param_eggs = get_header_param_eggs(f_obj)
    #     for chunk, chunk_info in get_chunks(f_obj.readlines()):
    #         #     0. inject EGGS.get() globals from other chunks?
    #         #     a. run the knitter(s)
    #         result_output, new_eggs = execute_chunk(chunk, param_eggs)
    #         #     3. save EGGS.put() globals for other chunks?
    #         # param_eggs.extend(new_eggs)
    #         replace_in_output_file(chunk_info, result_output)
    #         # b. inject output
    # TODO: INSTEAD OF THIS:
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
