"""
test knitting the basic file from ./examples/
"""

# std modules:
from unittest import TestCase

import logging
logging.basicConfig(level=logging.DEBUG)


class Test_basic_get_next_chunk(TestCase):

    def test_can_default_knit_basic_xmd(self):
        """Get a single simple chunk in file"""
        from eggsmark.get_chunks import _get_next_chunk
        CHUNK_LINE = "print('hellow')"
        LINES = [
            "---",
            "title: test",
            "---",
            "```{python}",
            CHUNK_LINE,
            "```",
        ]
        chunk = _get_next_chunk(LINES, 0)
        self.assertEqual(chunk, [CHUNK_LINE])
