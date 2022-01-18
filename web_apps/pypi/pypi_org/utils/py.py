import os
from importlib import import_module
from inspect import isclass
from pkgutil import iter_modules
import email_validator as email_validator
import validate_email

import sys


def import_modules(file, name, w_classes=True):
    # Iterate through the modules in the current package
    imported_modules = {}
    imported_classes = {}

    package_dir = os.path.dirname(file)
    for (_, module_name, _) in iter_modules([package_dir]):

        # Import the module and iterate through its attributes
        module = import_module(f"{name}.{module_name}")
        imported_modules[module_name] = module

        if w_classes:
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if isclass(attribute):
                    # Add the class to this package's variables
                    globals()[attribute_name] = attribute
                    imported_classes[attribute_name] = attribute

    return imported_modules, imported_classes


def add_module_do_sys_path(file, dir_path_part):
    directory = os.path.abspath(
        os.path.join(os.path.dirname(file), *dir_path_part))
    sys.path.insert(0, directory)


def str_to_int(str) -> int:
    try:
        return int(str)
    except:
        return 0

def is_email_valid(email, check_if_email_existing=False):
    try:
        normalized_email = email_validator.validate_email(email).email
        if check_if_email_existing:
            return validate_email.validate_email(normalized_email)
        return True

    except email_validator.EmailNotValidError:
        return False