#To check what happens when writing to stdout if it is not a true TTY, redirect standard output as follows:
source /Projects/projects/.venv/bin/activate

python logger.py > test.out
#When you cat test.out you will see that the ANSI color codes are not printed because we took that extra step in test_verbose() to check whether sys.stdout.isatty().