# pylint: disable=no-else-return
from app import config
from urllib.error import URLError
from urllib.request import urlopen

def convert_to_number(operand):
    try:
        if "." in operand:
            return float(operand)
        else:
            return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")


def InvalidConvertToNumber(operand):
    try:
        if "." in operand:
            return (float(operand))

        return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")


def validate_permissions(operation, user):
    print(f"checking permissions of {user} for operation {operation}")
    return user == "user1"

def make_request(endpoint):
    try:
        url = f"{config.BASE_URL}{endpoint}"
        response = urlopen(url, timeout=config.DEFAULT_TIMEOUT)
        return response.read(), response.status
    except URLError as e:
        return None, e.code