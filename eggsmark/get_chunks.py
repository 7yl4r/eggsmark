import logging

SUPPORTED_LANGUAGES = ["python", "r"]


def get_chunks(lines):
    """
    Get a list of the chunks from an xmd file
    """
    logger = logging.getLogger("eggsmark.{}".format(
        __name__,
    ))
    chunks = []
    chunks_info = []
    line_n = 0
    while line_n < len(lines):
        try:
            chunk, chunk_info = _get_next_chunk(lines, line_n)
            logger.debug("chunk {:02d} found l{:04d}-l{:04d}".format(
                len(chunks_info), chunk_info['start'], chunk_info['end']
            ))
            chunks.append(chunk)
            chunks_info.append(chunk_info)
            line_n = chunk_info['end']
        except EOFError:
            return chunks, chunks_info


def _get_next_chunk(lines, n):
    logger = logging.getLogger("eggsmark.{}".format(
        __name__,
    ))
    n_original = n
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
    raise EOFError("no chunks in l{:04d}-{:04d} (EOF)".format(
        n_original, n
    ))
