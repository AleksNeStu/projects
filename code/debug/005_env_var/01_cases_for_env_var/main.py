# Today’s post focuses on environment variables in Python. They are one of several possible mechanisms for setting various configuration parameters. We can:
#
# read environment variables (through os.environ or dotenv) [the current post]
# have the script accept command-line arguments (use argparse)
# load configuration settings from a file, such as:
# a JSON file (use json)
# a YAML file (use pyyaml)
# a XML file (use lxml, ElementTree or minidom)
# an INI file (use configparser) [check out this post]
# your DIY file format (for which you will be rolling your own parser)

# Accessing environment variables in Python
# Environment variables are read through os.environ. Although they can also be modified or cleared, such changes are only effective in the current Python session (and for subprocesses started with os.system(), popen(), fork() and execv()). In other words, if you change an environment variable in a Python script, the change will not be reflected in the environment once that script exits.

# os.environ

import os
import subprocess

subprocess.run("export foo='bar'", shell=True)

g = os.environ.get("foo")
print(g)



# Also note that the values of all environment variables are strings. To address this, you may want to roll your own small environment parser. Mine looks like this:
import os


def parse_string(value):
    if value.lower() == 'true':
        return True
    if value.lower() == 'false':
        return False

    try:
        value = int(value)
        return value
    except ValueError:
        try:
            value = float(value)
        finally:
            return value


def get_env_setting(setting):
    if setting not in os.environ:
        return None

    return parse_string(os.environ[setting])
# first, as a bool (this is because if set boolean environment variables in Python, store their str() representation, meaning 'True' for True and 'False' for False);
# if this fails, the value is converted to an int;
# if this fails as well, the value is converted to a float:
# if successful, parse_string() returns a float;
# if not, it returns a str.

val = get_env_setting('SSH_AGENT_PID')
assert type(val) is int


from dotenv import load_dotenv
load_dotenv("./config.env")

print(os.environ.get("DOMAIN"))

# Use case: securing access tokens

# Use case: injecting configuration into a black box
# This final use case is something you’re not going to come across very often in internet discussions. It’s something I call a “black box”, meaning code that you have no control over: you didn’t write it, you cannot change it but you have to run it.