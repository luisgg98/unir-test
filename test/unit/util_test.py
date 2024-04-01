import unittest
from unittest.mock import patch, MagicMock
import pytest
from urllib.error import HTTPError, URLError
from app import util


@pytest.mark.unit
class TestUtil(unittest.TestCase):
    def test_convert_to_number_correct_param(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(0, util.convert_to_number("-0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertAlmostEqual(4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.convert_to_number("-1.0"), delta=0.0000001)

    def test_convert_to_number_invalid_type(self):
        self.assertRaises(TypeError, util.convert_to_number, "")
        self.assertRaises(TypeError, util.convert_to_number, "3.h")
        self.assertRaises(TypeError, util.convert_to_number, "s")
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())

    def test_InvalidConvertToNumber_correct_param(self):
        self.assertEqual(4, util.InvalidConvertToNumber("4"))
        self.assertAlmostEqual(4.5, util.InvalidConvertToNumber("4.5"), delta=0.0000001)

    def test_InvalidConvertToNumber_invalid_type(self):
        with self.assertRaises(TypeError):
            util.InvalidConvertToNumber("abc")

    def test_validate_permissions_allowed(self):
        self.assertTrue(util.validate_permissions("any_operation", "user1"))

    def test_validate_permissions_denied(self):
        self.assertFalse(util.validate_permissions("any_operation", "user2"))

    @patch('app.util.urlopen')
    def test_make_request_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b"Success"
        mock_response.status = 200
        mock_urlopen.return_value = mock_response

        response_body, status_code = util.make_request("/test")
        self.assertEqual(response_body, b"Success")
        self.assertEqual(status_code, 200)

    @patch('app.util.urlopen')
    def test_make_request_error(self, mock_urlopen):
        url = 'http://0.0.0.0:5000/test'
        code = 400
        msg = 'Not Found'
        hdrs = ''
        fp = None
        mock_urlopen.side_effect = HTTPError(url, code, msg, hdrs, fp)

        response_body, status_code = util.make_request("/test")
        self.assertIsNone(response_body)
        self.assertEqual(status_code, code)
