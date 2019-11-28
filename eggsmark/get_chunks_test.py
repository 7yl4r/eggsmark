"""
test knitting the basic file from ./examples/
"""

# std modules:
from unittest import TestCase

import logging
logging.basicConfig(level=logging.DEBUG)

MINIMAL_CHUNK_LINE = "print('hellow')"
MINIMAL_XMD_LINES = [
    "---",
    "title: test",
    "---",
    "```{python}",
    MINIMAL_CHUNK_LINE,
    "```",
]


class Test_basic_get_chunks(TestCase):
    def test_can_get_minimal_chunks(self):
        """Get only simple chunk in file"""
        from eggsmark.get_chunks import get_chunks
        chunks, chunks_info = get_chunks(MINIMAL_XMD_LINES)
        self.assertEqual(chunks, [[MINIMAL_CHUNK_LINE]])


class Test_basic_get_next_chunk(TestCase):
    def test_can_get_minimal_chunk(self):
        """Get first simple chunk in file"""
        from eggsmark.get_chunks import _get_next_chunk
        chunk, chunk_info = _get_next_chunk(MINIMAL_XMD_LINES, 0)
        self.assertEqual(chunk, [MINIMAL_CHUNK_LINE])

    def test_minimal_chunk_start_n_end_info(self):
        """Minimal chunk from file lines has correct start & end info"""
        from eggsmark.get_chunks import _get_next_chunk
        chunk, chunk_info = _get_next_chunk(MINIMAL_XMD_LINES, 0)

        # check that test hasn't been modified
        assert MINIMAL_CHUNK_LINE == MINIMAL_XMD_LINES[4]

        # test for start/end line number for chunk
        self.assertEqual(chunk_info['start'], 3)
        self.assertEqual(chunk_info['end'], 5)
