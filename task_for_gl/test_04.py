import unittest
from unittest.mock import patch
from task_for_gl.task_04 import valid_admin_user


class TestValid(unittest.TestCase):

    @patch('task_for_gl.task_04.get_password')
    @patch('task_for_gl.task_04.get_password')
    @patch('crypt.crypt')
    def test_valid_admin_user_positive(self, mock, mock_user, mock_password):
        mock.return_value = "crypt_pass"
        mock_user.return_value = "user"
        mock_password.return_value = "crypt_pass"

        result = valid_admin_user("user", "crypt_pass")

        self.assertTrue(result)
        mock.assert_called_once_with("crypt_pass", "usSrrplukrCq.")
        mock_user.assert_called_once()
        mock_password.assert_called_once()

    @patch('task_for_gl.task_04.get_password')
    @patch('task_for_gl.task_04.get_password')
    @patch('crypt.crypt')
    def test_valid_admin_user_negative(self, mock, mock_user, mock_password):
        mock.return_value = "incorrect_pass"
        mock_user.return_value = "user"
        mock_password.return_value = "crypt_pass"

        result = valid_admin_user("user", "crypt_pass")

        self.assertFalse(result)
        mock.assert_called_once_with("incorrect_pass", "usSrrplukrCq.")
        mock_user.assert_called_once()
        mock_password.assert_called_once()
