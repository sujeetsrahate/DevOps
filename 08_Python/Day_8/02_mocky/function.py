import requests
from typing import Dict
from unittest.mock import patch
import unittest

def get_data(url: str) -> dict[str,str]:
    response = requests.get(url)
    return response.json()

class TestGetData(unittest.TestCase):
    @patch('requests.get')
    def test_Get_Data(self,mock_get: patch) -> None:
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'key': 'value'}

        result = get_data('http://example.com/api')
        self.assertEqual(result,{'key': 'value'})
        mock_get.assert_called_once_with('http://example.com/api')


if __name__ == '__main__':
    unittest.main()     