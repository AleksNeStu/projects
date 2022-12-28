from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0.0',
    description='Capitalize strings',
    author='John Doe',
    author_email='doe@example.com',
    packages=find_packages(),
    # The only thing left to do now is to point setup.py to the main() function of the __main__.py module and to ask it to add it as a console script “entry point” called capitalize:
    # [snip]
    entry_points = {'console_scripts': [
        'capitalize = mypackage.__main__:main',
        'runner = mypackage.__main__:runner',  # this gets added
    ]},
)