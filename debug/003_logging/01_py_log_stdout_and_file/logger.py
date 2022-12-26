# Adding both console and file handlers (i.e. logging to both stdout and to a file)
# Temporarily disabling console logging (e.g. if a global verbose flag is False)
# Temporarily disabling file logging (e.g. if we want to print with color to stdout using ANSI codes, but without color to the log file)
# Adding an extra logging level that logs to both console and log file (e.g. even if a global verbose flag is False)


import datetime
import logging
import os
import sys

from color import Color


class CustomLogger(logging.getLoggerClass()):
    def __init__(self, name, verbose, log_dir=None):
        """Create a custom logger with the specified `name`. When `log_dir` is None, a simple
        console logger is created. Otherwise, a file logger is created in addition to the console
        logger.

        This custom logger class adds an extra logging level FRAMEWORK (at INFO priority), with the
        aim of logging messages irrespective of any verbosity settings.

        By default, the five standard logging levels (DEBUG through CRITICAL) only display
        information in the log file if a file handler is added to the logger, but **not** to the
        console.

        :param name: name for the logger
        :param verbose: bool: whether the logging should be verbose; if True, then all messages get
            logged both to stdout and to the log file (if `log_dir` is specified); if False, then
            messages only get logged to the log file (if `log_dir` is specified), with the exception
            of FRAMEWORK level messages which get logged either way
        :param log_dir: str: (optional) the directory for the log file; if not present, no log file
            is created
        """
        # Create custom logger logging all five levels
        super().__init__(name)
        self.setLevel(logging.DEBUG)

        # Add new logging level
        logging.addLevelName(logging.INFO, 'FRAMEWORK')

        # Determine verbosity settings
        self.verbose = verbose

        # Create stream handler for logging to stdout (log all five levels)
        self.stdout_handler = logging.StreamHandler(sys.stdout)
        self.stdout_handler.setLevel(logging.DEBUG)
        self.stdout_handler.setFormatter(logging.Formatter('%(message)s'))
        self.enable_console_output()

        self.file_handler = None
        if log_dir:
            self.add_file_handler(name, log_dir)

    def add_file_handler(self, name, log_dir):
        """Add a file handler for this logger with the specified `name` (and store the log file
        under `log_dir`)."""
        # Format for file log
        fmt = '%(asctime)s | %(levelname)9s | %(filename)s:%(lineno)d | %(message)s'
        formatter = logging.Formatter(fmt)

        # Determine log path and file name; create log path if it does not exist
        now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        log_name = f'{str(name).replace(" ", "_")}_{now}'
        if not os.path.exists(log_dir):
            try:
                os.makedirs(log_dir)
            except:
                print(f'{self.__class__.__name__}: Cannot create directory {log_dir}. ',
                      end='', file=sys.stderr)
                log_dir = '/tmp' if sys.platform.startswith('linux') else '.'
                print(f'Defaulting to {log_dir}.', file=sys.stderr)

        log_file = os.path.join(log_dir, log_name) + '.log'

        # Create file handler for logging to a file (log all five levels)
        self.file_handler = logging.FileHandler(log_file)
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(formatter)
        self.addHandler(self.file_handler)

    def has_console_handler(self):
        return len([h for h in self.handlers if type(h) == logging.StreamHandler]) > 0

    def has_file_handler(self):
        return len([h for h in self.handlers if isinstance(h, logging.FileHandler)]) > 0

    def disable_console_output(self):
        if not self.has_console_handler():
            return
        self.removeHandler(self.stdout_handler)

    def enable_console_output(self):
        if self.has_console_handler():
            return
        self.addHandler(self.stdout_handler)

    def disable_file_output(self):
        if not self.has_file_handler():
            return
        self.removeHandler(self.file_handler)

    def enable_file_output(self):
        if self.has_file_handler():
            return
        self.addHandler(self.file_handler)

    def framework(self, msg, *args, **kwargs):
        """Logging method for the FRAMEWORK level. The `msg` gets logged both to stdout and to file
        (if a file handler is present), irrespective of verbosity settings."""
        return super().info(msg, *args, **kwargs)

    def _custom_log(self, func, msg, *args, **kwargs):
        """Helper method for logging DEBUG through CRITICAL messages by calling the appropriate
        `func()` from the base class."""
        # Log normally if verbosity is on
        if self.verbose:
            return func(msg, *args, **kwargs)

        # If verbosity is off and there is no file handler, there is nothing left to do
        if not self.has_file_handler():
            return

        # If verbosity is off and a file handler is present, then disable stdout logging, log, and
        # finally reenable stdout logging
        self.disable_console_output()
        func(msg, *args, **kwargs)
        self.enable_console_output()

    def debug(self, msg, *args, **kwargs):
        self._custom_log(super().debug, msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self._custom_log(super().info, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self._custom_log(super().warning, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._custom_log(super().error, msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self._custom_log(super().critical, msg, *args, **kwargs)


def test_verbose():
    print('*' * 80 + '\nVerbose logging (stdout + file)\n' + '*' * 80)
    verbose_log = CustomLogger('verbose', verbose=True, log_dir='logs')

    verbose_log.warning('We now log to both stdout and a file log')

    verbose_log.disable_file_output()
    msg = 'Use color in a true TTY'
    if sys.stdout.isatty():
        verbose_log.info(Color.colored(Color.LIGHTYELLOW, msg))
    else:
        verbose_log.info(msg + ', but not here')
    verbose_log.enable_file_output()

    verbose_log.framework('We now log everywhere irrespective of verbosity')


def test_quiet():
    print('*' * 80 + '\nQuiet logging (stdout: only FRAMEWORK + file: all levels)\n' + '*' * 80)
    quiet_log = CustomLogger('quiet', verbose=False, log_dir='logs')
    quiet_log.warning('We now log only to a file log')
    quiet_log.framework('We now log everywhere irrespective of verbosity')


if __name__ == '__main__':
    test_verbose()
    test_quiet()