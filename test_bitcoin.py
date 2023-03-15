import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestBitcoin(TestCase):
    @patch('bitcoin.get_us_dollar_bitcoin_value')
    def test_convert_dollars_to_bitcoin(self, mock_dollar_values):
        mock_dollar_value = 5000
        converted = bitcoin.convert_dollars_to_bitcoin(2, mock_dollar_value)
        expected = 10000
        self.assertEqual(expected, converted)