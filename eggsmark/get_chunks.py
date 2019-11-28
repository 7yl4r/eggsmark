import logging

SUPPORTED_LANGUAGES = ["python", "r"]


def get_chunks(lines, n):
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
        chunk, chunk_info = _get_next_chunk(lines, n)


def _get_next_chunk(lines, n):
    logger = logging.getLogger("eggsmark.{}".format(
        __name__,
    ))
    inside_a_chunk = False
    while n < len(lines):
        logger.debug("l{:04d} / {:04d}".format(n, len(lines)))
        start_line = lines[n]
        # if entering chunk
        if not inside_a_chunk and start_line.startswith(r"```{"):
            chunk_start = n
            language = start_line.split("}")[0].split(",")[0][4:]
            if language not in SUPPORTED_LANGUAGES:
                raise ValueError(
                    "unknown programming language '{}'".format(language)
                )
            else:
                inside_a_chunk = True
                chunk_lines = []
        elif inside_a_chunk:
            if lines[n].strip().endswith("```"):
                chunk_end = n
                return chunk_lines, {"start": chunk_start, "end": chunk_end}
            else:
                chunk_lines.append(lines[n])
        n += 1  # next line
