# std modules:
from unittest import TestCase

import logging
logging.basicConfig(level=logging.DEBUG)


class Test_get_params_from_header_lines(TestCase):
    def test_get_minimal_param_eggs_from_header_lines(self):
        """Get minimal params from header lines"""
        from eggsmark.get_param_eggs import _get_header_param_eggs
        from eggsmark._test_xmd_lines import HEADER_MINIMAL_PARAMS
        from eggsmark._test_xmd_lines import HEADER_MINIMAL_PARAMS_DICT
        param_eggs = _get_header_param_eggs(HEADER_MINIMAL_PARAMS)

        self.assertEqual(param_eggs, HEADER_MINIMAL_PARAMS_DICT)


class Test_get_header_lines(TestCase):
    def test_get_minimal_header_w_params(self):
        """Get the minimal header lines with params"""
        from eggsmark.get_param_eggs import _get_header_lines
        from eggsmark._test_xmd_lines import XMD_LINES_W_HEADER
        from eggsmark._test_xmd_lines import HEADER_MINIMAL_PARAMS

        header_lines = _get_header_lines(XMD_LINES_W_HEADER)

        self.assertEqual(header_lines, HEADER_MINIMAL_PARAMS)


class Test_get_param_eggs(TestCase):
    def test_get_params_eggs(self):
        """Get the minimal header param eggs from file contents"""
        from eggsmark.get_param_eggs import get_header_param_eggs
        from eggsmark._test_xmd_lines import XMD_LINES_W_HEADER
        from eggsmark._test_xmd_lines import HEADER_MINIMAL_PARAMS_DICT

        header_param_eggs = get_header_param_eggs(XMD_LINES_W_HEADER)
        self.assertEqual(header_param_eggs, HEADER_MINIMAL_PARAMS_DICT)
