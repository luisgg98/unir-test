import unittest
from unittest.mock import patch
import pytest
import sys
from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True

@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Tests for divide
    def test_divide_success(self):
        self.assertEqual(2, self.calc.divide(4, 2))

    def test_divide_failure_type_error(self):
        self.assertRaises(TypeError,self.calc.divide,'4', 2)
            
    def test_divide_failure_division_by_zero(self):
        self.assertRaises(TypeError,self.calc.divide,4, 0)

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    # Tests for add
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_success(self):
        self.assertEqual(5, self.calc.add(2, 3))

    def test_add_failure_type_error(self):
        self.assertRaises(TypeError,self.calc.add,'a', 3)

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    # Tests for subtract
    def test_subtract_success(self):
        self.assertEqual(1, self.calc.substract(3, 2))

    def test_subtract_failure_type_error(self):
        self.assertRaises(TypeError,self.calc.substract,3, 'b')

    # Tests for multiply
    def test_multiply_success(self):
        self.assertEqual(6, self.calc.multiply(2, 3))

    def test_multiply_failure_type_error(self):
        self.assertRaises(TypeError,self.calc.multiply,2, 'b')
            
    # Tests for power
    def test_power_success(self):
        self.assertEqual(8, self.calc.power(2, 3))

    def test_power_failure_type_error(self):
        self.assertRaises(TypeError,self.calc.power,'2', 3)
            
    # Tests for sqrt
    def test_sqrt_success(self):
        self.assertEqual(3, self.calc.sqrt(9))

    def test_sqrt_failure_negative_input(self):
        self.assertRaises(ValueError,self.calc.sqrt,-1)
            
    # Tests for log10
    def test_log10_success(self):
        self.assertAlmostEqual(1, self.calc.log10(10))

    def test_log10_failure_negative_input(self):
        self.assertRaises(ValueError,self.calc.log10,-10)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
