> 1. [How to remove the .idea folder from git](https://www.david-merrick.com/2017/08/04/how-to-remove-the-idea-folder-from-git/)
* Blacklist the .idea folder by adding the `“.idea”` folder to the .gitignore file in master, then commit this change.
* In your branch, check this file out from master.\
  `git checkout master -- .gitignore`
* Remove the `.idea` folder from the git tree\
  `git rm --cached -r .idea`
  
> 2. Git cheat sheets:
* [ch1](https://education.github.com/git-cheat-sheet-education.pdf)
* [ch2](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
* [ch3](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)

> 3. Credentials


> 4. Git submodules
- https://devconnected.com/how-to-add-and-update-git-submodules/
- https://stackoverflow.com/questions/1260748/how-do-i-remove-a-submodule

```
Add a Git Submodule
git submodule add <remote_url> <destination_folder>

Pull a Git Submodule
git submodule update --init --recursive

Checkout all branches
for branch in `git branch -a | grep remotes | grep -v HEAD | grep -v master `; do git branch --track ${branch#remotes/origin/} $branch; done

Fully copy Git Submodule dir
cp -rf git-submodule-dir git-submodule-dir-copy

Move Git Submodule dir
git mv BasePython git/BasePython
edit .gitmodules
edit IDE settings 'Version Control'

Commit and push the changes. 
NOTE: Copied Git Submodule will be checkoutable locally but not via Git UI
```
   
> 5. Tools
- https://www.tecmint.com/best-gui-git-clients-git-repository-viewers-for-linux/ \
* `GitKraken` - is a cross-platform, elegant and highly efficient Git client for Linux. It works on Unix-like systems such as Linux and Mac OS X, and Windows as well. Its designed to boost a Git user’s productivity through features such as:
* `SmartGit` - is a also a cross-platform, powerful, popular GUI Git client for Linux, Mac OS X and Windows. Referred to as Git for professionals, it enables users master daily Git challenges and boosts their productivity through efficient workflows.   
* `tig` - Tig is an ncurses-based text-mode interface for git. It functions mainly as a Git repository browser, but can also assist in staging changes for commit at chunk level and act as a pager for output from various Git commands.
* `CLI` https://github.com/cli/cli \
  gh is GitHub on the command line. It brings pull requests, issues, and other GitHub concepts to the terminal next to where you are already working with git and your code. \
  Linux & BSD
  gh is available via Homebrew, Conda, Spack, and as downloadable binaries from the releases page. \
For instructions on specific distributions and package managers, see Linux & BSD installation. \


> 5. Commands
- git status
- git init
- git add / git rm  
- git commit -m ""
- git reset --hard HEAD
- git checkout file or branch

> 6. Remote branches
- [How to clone all remote branches in Git?](https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git) \
  https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git/4754797#4754797 \
  https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git/7216269#7216269
  
- [How to clone all repos at once from GitHub?](https://stackoverflow.com/questions/19576742/how-to-clone-all-repos-at-once-from-github)
```
CNTX={users|orgs}; NAME={username|orgname}; PAGE=1

curl "https://api.github.com/$CNTX/$NAME/repos?page=$PAGE&per_page=100" |
  grep -e 'git_url*' |
  cut -d \" -f 4 |
  xargs -L1 git clone
```
Set CNTX=users and NAME=yourusername, to download all your repositories. \
Set CNTX=orgs and NAME=yourorgname, to download all repositories of your organization.

- [How to clone all repos at once from GitHub?](https://newbedev.com/how-to-clone-all-repos-at-once-from-github) \
```
To clone all repos from your organisation, try the following shell one-liner:
GHORG=company; curl "https://api.github.com/orgs/$GHORG/repos?per_page=1000" | grep -o 'git@[^"]*' | xargs -L1 git clone

Cloning all using Git repository URLs:
GHUSER=CHANGEME; curl "https://api.github.com/users/$GHUSER/repos?per_page=1000" | grep -o 'git@[^"]*' | xargs -L1 git clone

Cloning all using Clone URL:
GHUSER=CHANGEME; curl "https://api.github.com/users/$GHUSER/repos?per_page=1000" | grep -w clone_url | grep -o '[^"]\+://.\+.git' | xargs -L1 git clone
```

FUNC:
```
# Usage: gh-clone-user (user)
gh-clone-user() {
  curl -sL "https://api.github.com/users/$1/repos?per_page=1000" | jq -r '.[]|.clone_url' | xargs -L1 git clone
}
```
NOTE:
To be able to push changes to remote repo need to rename .git dirs to .git_
`find /your/target/path/ -type d -execdir rename 's/.git/.git_/' '{}' \+`
or
https://github.com/neurobin/rnm
Renames files/directories in bulk. Naming scheme (*Name String*) can be applied or regex replace can be performed to modify file names on the fly. It uses PCRE2 (revised version of PCRE) regex to provide search (and replace) functionality.
```
rnm -rs '/.git/___git/g' -dp -1 *
rnm -rs '/___git/.git/g' -dp -1 *
```

- [Git push existing repo to a new and different remote repo server?](https://stackoverflow.com/questions/5181845/git-push-existing-repo-to-a-new-and-different-remote-repo-server) \
```
0. create the new empty repository (say, on github)
1. make a bare clone of the repository in some temporary location
2. change to the temporary location
3. perform a mirror-push to the new repository
4. change to another location and delete the temporary location
```

```
cd $HOME
git clone --bare https://git.fedorahosted.org/the/path/to/my_repo.git
cd my_repo.git
git push --mirror https://github.com/my_username/my_repo.git
cd ..
rm -rf my_repo.git```
```

> 6. Auth

- [GitHub Error Message - Permission denied (publickey)](https://stackoverflow.com/questions/12940626/github-error-message-permission-denied-publickey) \
  GitHub isn't able to authenticate you. So, either you aren't setup with an SSH key, because you haven't set one up on your machine, or your key isn't associated with your GitHub account. \
You can also use the HTTPS URL instead of the SSH/git URL to avoid having to deal with SSH keys. This is GitHub's recommended method. \
Further, GitHub has a help page specifically for that error message, and explains in more detail everything you could check. \
  https://cli.github.com/manual/gh_auth_login
  GH_TOKEN as the token that got generated from github.com.settings/token
  Our documentation for --with-token states: \
Read token from standard input \
Because the command is trying to read the token from standard input, if you don't pass anything on standard input, the command will block, waiting on input. \
  If you've set GH_TOKEN or GITHUB_TOKEN in your environment, there is no need to ever gh auth login. All your gh operations will be authenticated via those environment variables. gh auth login is only useful to store your credentials in case you don't use environment variables, and gh auth logout is only useful to erase the stored credentials (which, again, isn't applicable if you're using environment variables).
- ```
  Options
  -h, --hostname <string>
  The hostname of the GitHub instance to authenticate with
  -s, --scopes <strings>
  Additional authentication scopes for gh to have
  -w, --web
  Open a browser to authenticate
  --with-token
  Read token from standard input
  
  ```

- [Git: How to solve Permission denied (publickey) error when using Git?](https://stackoverflow.com/questions/2643502/git-how-to-solve-permission-denied-publickey-error-when-using-git) \
  `Permission denied (publickey).`
  https://docs.github.com/en/authentication/connecting-to-github-with-ssh 

If the user has generated a ssh public/private key pair set before
check which key have been authorized on your github or gitlab account settings
determine which corresponding private key must be associated from your local computer
`eval $(ssh-agent -s)`
define where the keys are located
`ssh-add ~/.ssh/id_rsa`
More extensive troubleshooting and even automated fixing can be done with:
`ssh -vT git@github.com`

- [Git flow] \
` git remote -v` - get origins

