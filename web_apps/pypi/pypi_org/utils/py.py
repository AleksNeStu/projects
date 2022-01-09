import os
from importlib import import_module
from inspect import isclass
from pkgutil import iter_modules


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