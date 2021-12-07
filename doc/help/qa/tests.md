1. equals \
   https://github.com/jwtk/jjwt/issues/169
   https://stackoverflow.com/questions/2404978/why-are-assertequals-parameters-in-the-order-expected-actual
   
2. python + tests \
   https://realpython.com/python-testing/

3. Types
- [unittest](https://docs.python.org/3/library/unittest.html) \
   The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting frame. \

- [pytest](https://docs.pytest.org/en/) \
  The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries. \
  https://pypi.org/project/pytest-xdist/ - xdist: pytest distributed testing plugin
  https://pypi.org/project/pytest-timeout/ - pytest plugin to abort hanging tests
  https://pypi.org/project/pytest-coverage/ -
  https://pypi.org/project/pytest-flakes/ - pytest plugin to check source code with pyflakes


- [mock](https://docs.python.org/3/library/unittest.mock.html) \
unittest.mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used. \

- [doctest](https://docs.python.org/3/library/doctest.html) \
The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

- [flake8](https://flake8.pycqa.org/en/latest/)
Flake8: Your Tool For Style Guide Enforcement
Flake8 is a wrapper around these tools:
PyFlakes
pycodestyle
Ned Batchelder’s McCabe script
Flake8 runs all the tools by launching the single flake8 command. It displays the warnings in a per-file, merged output.

- [pylama](https://github.com/klen/pylama) \
    Code audit tool for Python and JavaScript. Pylama wraps these tools:
  pycodestyle (formerly pep8) © 2012-2013, Florent Xicluna;
  pydocstyle (formerly pep257 by Vladimir Keleshev) © 2014, Amir Rachum;
  PyFlakes © 2005-2013, Kevin Watters;
  Mccabe © Ned Batchelder;
  Pylint © 2013, Logilab (should be installed 'pylama_pylint' module);
  Radon © Michele Lacchia
  gjslint © The Closure Linter Authors (should be installed 'pylama_gjslint' module);
  eradicate © Steven Myint;
  Mypy © Jukka Lehtosalo and contributors;

- [tox](https://pypi.org/project/tox/) \
  tox is a generic virtualenv management and test command line tool you can use for:
checking that your package installs correctly with different Python versions and interpreters
running your tests in each of the environments, configuring your test tool of choice
acting as a frontend to Continuous Integration servers, greatly reducing boilerplate and merging CI and shell-based testing.

- `assert`
  [Disable assertions in Python](https://stackoverflow.com/questions/1273211/disable-assertions-in-python) \:
  `PYTHONOPTIMIZE=TRUE` or `Using the -O flag (capital O) disables all assert statements in a process.`
  http://pybites.blogspot.com/2011/07/behind-scenes-of-pytests-new-assertion.html
  https://docs.pytest.org/en/latest/how-to/assert.html
  Операция -- это некоторое действие, которое необходимо совершить.
  Оператор -- это объект, который выполняет операцию.
  Операнд -- это объект, над которым оператор выполняет операцию.

