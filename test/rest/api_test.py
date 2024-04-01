import http.client
import unittest
from app import config
from app.util import make_request
from urllib.request import urlopen
import pytest


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(config.BASE_URL, "URL no configurada")
        self.assertTrue(len(config.BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{config.BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=config.DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_divide_by_zero(self):
        _, status = make_request(f"/calc/divide/1/0")
        self.assertNotEqual(status, http.client.OK, "Divide by zero should not be OK")

    # Test add
    def test_add_success(self):
        body, status = make_request("/calc/add/2/2")
        self.assertEqual(status, http.client.OK)
        self.assertEqual(int(body), 4)

    def test_add_failure(self):
        _, status = make_request("/calc/add/two/2")
        self.assertEqual(status, http.client.BAD_REQUEST)

    # Test subtract
    def test_subtract_success(self):
        body, status = make_request("/calc/subtract/5/3")
        self.assertEqual(status, http.client.OK)
        self.assertEqual(int(body), 2)

    def test_subtract_failure(self):
        _, status = make_request("/calc/subtract/5/two")
        self.assertEqual(status, http.client.BAD_REQUEST)

    # Test multiply
    def test_multiply_success(self):
        body, status = make_request("/calc/multiply/3/4")
        self.assertEqual(status, http.client.OK)
        self.assertEqual(int(body), 12)

    def test_multiply_failure(self):
        _, status = make_request("/calc/multiply/three/4")
        self.assertEqual(status, http.client.BAD_REQUEST)

    # Test divide
    def test_divide_success(self):
        body, status = make_request("/calc/divide/10/2")
        self.assertEqual(status, http.client.OK)
        self.assertEqual(int(float(body)), 5)

    def test_divide_failure(self):
        _, status = make_request("/calc/divide/10/0")
        self.assertEqual(status, http.client.BAD_REQUEST)

    # Test power
    def test_power_success(self):
        body, status = make_request("/calc/power/2/3")
        self.assertEqual(status, http.client.OK)
        self.assertEqual(int(float(body)), 8)

    def test_power_failure(self):
        _, status = make_request("/calc/power/two/3")
        self.assertEqual(status, http.client.BAD_REQUEST)

    # Test sqrt
    def test_sqrt_success(self):
        body, status = make_request("/calc/sqrt/16")
        self.assertEqual(status, http.client.OK)
        self.assertEqual(int(float(body)), 4)

    def test_sqrt_failure(self):
        _, status = make_request("/calc/sqrt/-1")
        self.assertEqual(status, http.client.BAD_REQUEST)

    # Test log10
    def test_log10_success(self):
        body, status = make_request("/calc/log10/100")
        self.assertEqual(status, http.client.OK)
        self.assertEqual(int(float(body)), 2)

    def test_log10_failure(self):
        _, status = make_request("/calc/log10/-100")
        self.assertEqual(status, http.client.BAD_REQUEST)
