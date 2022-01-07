import os
from importlib import import_module
from inspect import isclass
from pkgutil import iter_modules


def import_all_modules_w_classes(file, name):
    # Iterate through the modules in the current package
    package_dir = os.path.dirname(file)
    for (_, module_name, _) in iter_modules([package_dir]):

        # Import the module and iterate through its attributes
        module = import_module(f"{name}.{module_name}")
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isclass(attribute):
                # Add the class to this package's variables
                globals()[attribute_name] = attribute