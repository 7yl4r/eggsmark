"""
test knitting the basic file from ./examples/
"""

# std modules:
from unittest import TestCase
from subprocess import run
import hashlib


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class Test_basic_xmd_test(TestCase):
    def test_can_default_knit_basic_xmd(self):
        """Knit basic xmd example"""
        INP_FPATH = "examples/basic.x.md"

        OUT_FILENAME = 'basic_xmd.html'
        OUT_DIR = 'tests/output/'
        OUT_FPATH = OUT_DIR + OUT_FILENAME

        result = run([
            'eggsmark/xmd_knit.py',
            INP_FPATH,
            OUT_FPATH
        ])

        print(result)
        self.assertEqual(md5(OUT_FPATH), '51d6839df5e56948ac3279075bdf9641')
