# std modules:
from unittest import TestCase

import logging
logging.basicConfig(level=logging.DEBUG)


class Test_knit_chunk(TestCase):
    def test_knit_basic_chunk(self):
        """Knit minimal chunk"""
        from eggsmark.knit_chunk import knit_chunk
        from eggsmark._test_xmd_lines import MINIMAL_CHUNK_LINES_1
        result = knit_chunk(MINIMAL_CHUNK_LINES_1, {})

        self.assertEqual(result, ['hellow\n'])

    def test_knit_chunk_with_image_output(self):
        """Knit a chunk w plt.show()"""
        from eggsmark.knit_chunk import knit_chunk
        from eggsmark._test_xmd_lines import MINIMAL_CHUNK_LINES_1
        result = knit_chunk(MINIMAL_CHUNK_LINES_1, {})

        self.assertEqual(result, ['hellow\n'])
