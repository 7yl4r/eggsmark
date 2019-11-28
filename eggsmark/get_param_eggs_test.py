# std modules:
from unittest import TestCase

import logging
logging.basicConfig(level=logging.DEBUG)


class Test_get_params_from_header_lines(TestCase):
    def test_get_minimal_param_eggs_from_header_lines(self):
        """Get the only simple chunk in lines"""
        from eggsmark.get_param_eggs import _get_header_param_eggs
        from eggsmark._test_xmd_lines import HEADER_MINIMAL_PARAMS
        param_eggs = _get_header_param_eggs(HEADER_MINIMAL_PARAMS)

        self.assertEqual(param_eggs, {"x": True})
