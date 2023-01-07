# PyCharm Stubs For Albert Launcher Python Plugins
## Install
To install, follow [Stubs | PyCharm Documentation](https://www.jetbrains.com/help/pycharm/stubs.html#reuse-stubs).

In *Status Bar* -> *Project Interpreter* selector -> `Interpreter Settings...` -> `Python Interpreter:` dropdown -> `Show All...` -> `Show Interpreter Paths` icon -> Add a stub to the `python_stubs/` directory.

## Development Setup
To setup the project for development, run:

    $ cd albert_python_stubs/
    $ pre-commit install --hook-type pre-commit --hook-type commit-msg

To lint and format files, run:

    $ pre-commit run --all-files
