"""
test knitting the basic file from ./examples/
"""

# std modules:
from unittest import TestCase

import logging
logging.basicConfig(level=logging.DEBUG)

MINIMAL_CHUNK_LINES_1 = ["print('hellow')"]
MINIMAL_CHUNK_LINES_2 = [
    "print('this is a 2nd chunk')",
    "print('this chunk has 2 lines too')"
]
XMD_LINES_MINIMAL = [
    "---",
    "```{python}",
    *MINIMAL_CHUNK_LINES_1,
    "```"
]
XMD_LINES_TWO_CHUNK = [
    "---",
    "```{python}",
    *MINIMAL_CHUNK_LINES_1,
    "```"
    "",
    "This is raw *markdown* text",
    "",
    "```{python}",
    *MINIMAL_CHUNK_LINES_2,
    "```"
]


class Test_basic_get_chunks(TestCase):
    def test_can_get_minimal_chunks(self):
        """Get the only simple chunk in lines"""
        from eggsmark.get_chunks import get_chunks
        chunks, chunks_info = get_chunks(XMD_LINES_MINIMAL)
        self.assertEqual(chunks, [
            MINIMAL_CHUNK_LINES_1
        ])

    def test_can_get_two_chunks(self):
        """Get two simple chunks from lines"""
        from eggsmark.get_chunks import get_chunks
        chunks, chunks_info = get_chunks(XMD_LINES_TWO_CHUNK)
        self.assertEqual(
            chunks,
            [MINIMAL_CHUNK_LINES_1, MINIMAL_CHUNK_LINES_2]
        )


class Test_basic_get_next_chunk(TestCase):
    def test_can_get_minimal_chunk(self):
        """Get first simple chunk in file"""
        from eggsmark.get_chunks import _get_next_chunk
        chunk, chunk_info = _get_next_chunk(XMD_LINES_MINIMAL, 0)
        self.assertEqual(chunk, MINIMAL_CHUNK_LINES_1)

    def test_minimal_chunk_start_n_end_info(self):
        """Minimal chunk from file lines has correct start & end info"""
        from eggsmark.get_chunks import _get_next_chunk
        chunk, chunk_info = _get_next_chunk(XMD_LINES_MINIMAL, 0)

        # check that test hasn't been modified
        assert MINIMAL_CHUNK_LINES_1[0] == XMD_LINES_MINIMAL[2]

        # test for start/end line number for chunk
        self.assertEqual(chunk_info['start'], 1)
        self.assertEqual(chunk_info['end'], 3)
