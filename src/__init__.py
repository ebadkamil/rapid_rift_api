import os

__version__ = "v1.0.0"

ROOT_PATH = os.path.join(os.path.expanduser("~"), ".rapid_rift_api")


if not os.path.isdir(ROOT_PATH):
    os.makedirs(ROOT_PATH)
