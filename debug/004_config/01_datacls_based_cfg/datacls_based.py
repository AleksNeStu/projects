# Data classes are kinda like structs in C++.

from dataclasses import dataclass

@dataclass
class ServerConfig:
    host: str
    port: int
    timeout: float


config = ServerConfig('example.com', 80, 0.5)
print(config)
print(config.host)


# Data classes are fortunately not limited to attributes. They can have methods, and all the built-in methods including __init__() are present. Additionally, there’s __post_init__() which is used to post-process the instance after __init__() is done.
# The data class in the previous example can be modified to accept configuration from a dictionary:
@dataclass
class ServerConfigFromDict:
    host: str
    port: int
    timeout: float

    def __init__(self, conf: dict):
        self.host = conf['host']
        self.port = conf['port']
        self.timeout = conf['timeout']

# If we try to access a non-existing key from the conf dict, a KeyError is raised. Notice in this example that we do not check whether the value for 'port' is an int, nor whether the value for 'timeout' is a float.
data = {'host': 'example.com', 'port': 80, 'timeout': 0.5}
config = ServerConfigFromDict(conf=data)

print(config)
print(config.host)


# Another solution is to use the dacite package:

import dacite

# define converters/validators for the various data types we use
converters = {
    str: str.lower,
    int: lambda x: x * 2,
}

config2 = dacite.from_dict(
    data_class=ServerConfig, data=data, config=dacite.Config(type_hooks=converters))

print(config2)

from types import SimpleNamespace
config2 = SimpleNamespace(**data)


# Dynamically creating a configuration class
# We can do this using the Python setattr built-in method. We don’t even need a data class for this, a “dumb” class can cut it just as well:
class DynamicConfig:
    def __init__(self, conf):
        if not isinstance(conf, dict):
            raise TypeError(f'dict expected, found {type(conf).__name__}')

        self._raw = conf
        for key, value in self._raw.items():
            setattr(self, key, value)

config = DynamicConfig({'host': 'example.com', 'port': 80, 'timeout': 0.5})