import unittest
from unittest.mock import patch
from assignment4 import get_repo_info

class TestGetRepoInfo(unittest.TestCase):
    @patch('assignment4.requests.get')
    def test_empty_string(self, mock_get):
        mock_get.return_value.status_code = 200
        self.assertEqual(get_repo_info(" "), {}, 'Empty string is invalid')

    @patch('assignment4.requests.get')
    def test_invalid_input(self, mock_get):
        mock_get.return_value.status_code = 200
        self.assertEqual(get_repo_info(123), {}, 'Invalid input')  
        self.assertEqual(get_repo_info("..."), {}, 'Invalid input')  

    @patch('assignment4.requests.get')
    def test_invalid_id(self, mock_get):
        mock_get.return_value.status_code = 404
        self.assertEqual(get_repo_info("wrong_id"), {}, 'Wrong id is invalid')
        self.assertEqual(get_repo_info("!@#"), {}, 'Special characters in id are invalid')

    @patch('assignment4.requests.get')
    def test_no_repositories(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []
        self.assertEqual(get_repo_info("hello956"), {}, 'User has no repositories')

if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
