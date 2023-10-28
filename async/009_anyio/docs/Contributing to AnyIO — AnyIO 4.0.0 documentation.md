---
source: https://anyio.readthedocs.io/en/stable/contributing.html

created: 2023-10-28T19:52:56 (UTC +02:00)

tags: []

author: 

---

# Contributing to AnyIO — AnyIO 4.0.0 documentation
---
If you wish to contribute a fix or feature to AnyIO, please follow the following guidelines.

When you make a pull request against the main AnyIO codebase, Github runs the AnyIO test suite against your modified
code. Before making a pull request, you should ensure that the modified code passes tests locally. To that end, the use
of [tox](https://tox.readthedocs.io/en/latest/install.html) is recommended. The default tox run first runs `pre-commit`
and then the actual test suite. To run the checks on all environments in parallel, invoke tox with `tox -p`.

To build the documentation, run `tox -e docs` which will generate a directory named `build` in which you may view the
formatted HTML documentation.

AnyIO uses [pre-commit](https://pre-commit.com/#installation) to perform several code style/quality checks. It is
recommended to activate [pre-commit](https://pre-commit.com/#installation) on your local clone of the repository (
using `pre-commit install`) to ensure that your changes will pass the same checks on GitHub.

## Making a pull request on Github[¶](https://anyio.readthedocs.io/en/stable/contributing.html#making-a-pull-request-on-github "Link to this heading")

To get your changes merged to the main codebase, you need a Github account.

1. Fork the repository (if you don’t have your own fork of it yet) by navigating to
   the [main AnyIO repository](https://github.com/agronholm/anyio) and clicking on “Fork” near the top right corner.

2. Clone the forked repository to your local machine with `git clone git@github.com/yourusername/anyio`.

3. Create a branch for your pull request, like `git checkout -b myfixname`

4. Make the desired changes to the code base.

5. Commit your changes locally. If your changes close an existing issue, add the text `Fixes XXX.` or `Closes XXX.` to
   the commit message (where XXX is the issue number).

6. Push the changeset(s) to your forked repository (`git push`)

7. Navigate to Pull requests page on the original repository (not your fork) and click “New pull request”

8. Click on the text “compare across forks”.

9. Select your own fork as the head repository and then select the correct branch name.

10. Click on “Create pull request”.

If you have trouble, consult
the [pull request making guide](https://opensource.com/article/19/7/create-pull-request-github) on opensource.com.
