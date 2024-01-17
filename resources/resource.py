import os

import tests

PATH = os.path.join(os.path.dirname(os.path.abspath(tests.__file__)), os.path.pardir, "resources")


def path(file_name):
    return os.path.abspath(os.path.join(PATH, file_name))
