# Dynamic configuration with INI files
# INI files may be parsed with configparser, but the object we get is a configparser.ConfigParser. We can create a class to encapsulate such an object and provide identifiers for keys. For the key = value part of the INI file, we can reuse our previous DynamicConfig class above, but we need to handle the [sections] in the INI file separately.
import configparser


class DynamicConfig:
    def __init__(self, conf):
        if not isinstance(conf, dict):
            raise TypeError(f'dict expected, found {type(conf).__name__}')

        self._raw = conf
        for key, value in self._raw.items():
            setattr(self, key, value)


class DynamicConfigIni:
    def __init__(self, conf):
        if not isinstance(conf, configparser.ConfigParser):
            raise TypeError(f'ConfigParser expected, found {type(conf).__name__}')

        self._raw = conf
        for key, value in self._raw.items():
            if key == "DEFAULT":
                key = 'default'
            setattr(self, key, DynamicConfig(dict(value.items())))


parser = configparser.ConfigParser()
parser.read_file(open('config.ini'))
config = DynamicConfigIni(parser)
print(config)
print('server:', config.server.host, config.server.port, config.server.timeout)
print('user:', config.user.username, config.user.level)
