API client for Allegro.pl.

Project run:
1) Clone repo.
2) Install Python 3.x and pip3.
3) Create venv:\
`virtualenv .venv & source .venv/bin/activate`
`pipreqs` - tools to generate deps based on project imports.
4) Install deps: \
`pip3 install -r requirements.txt`
5) Check deps:\
`pipdeptree`
`yolk -V requests`
6) Request oauth app via:\
https://apps.developer.allegro.pl/new \
Type: `Aplikacja otrzyma OAuth grant-type: authorization_code`\
Redirect URL: `http://localhost:7777`


**NOTE:** Partially was used code snippets from:\
https://github.com/chawel/python-allegro