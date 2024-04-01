import os
BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs

class InvalidPermissions(Exception):
    pass
