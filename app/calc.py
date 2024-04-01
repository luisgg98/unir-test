import app
import math  # Necesario para sqrt y log10
from app.config import InvalidPermissions

class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")
        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def sqrt(self, x):
        self.check_type(x)  # Solo necesita una comprobación
        if x < 0:
            raise ValueError("Cannot compute square root of negative number")
        return math.sqrt(x)

    def log10(self, x):
        self.check_type(x)
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive values")
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")

    def check_type(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be a number")

if __name__ == "__main__":
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
