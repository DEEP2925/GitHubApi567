import unittest
from unittest.mock import patch, MagicMock
from assignment4 import get_repo_info

class TestGetRepoInfo(unittest.TestCase):

    @patch('assignment4.requests.get')
    def test_empty_string(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '[]'
        mock_get.return_value = mock_response

        self.assertEqual(get_repo_info(" "), {}, 'Empty string is invalid')

    @patch('assignment4.requests.get')
    def test_invalid_input(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '[]'
        mock_get.return_value = mock_response

        self.assertEqual(get_repo_info("..."), {}, 'Invalid input')

    @patch('assignment4.requests.get')
    def test_no_repositories(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        self.assertEqual(get_repo_info("hello956"), {}, 'User has no repositories')

if __name__ == '__main__':
    unittest.main()
