# git subtree add --prefix=folder/ remote-name <URL to Git repo> subtree-branchname
git subtree add --prefix=subdirectory https://github.com/example/repo.git master


# If error, refer to code and check
# https://github.com/git/git/blob/master/contrib/subtree/git-subtree.sh
# Usage: ensure_clean
ensure_clean () {
	assert test $# = 0
	if ! git diff-index HEAD --exit-code --quiet 2>&1
	then
		die "fatal: working tree has modifications.  Cannot add."
	fi
	if ! git diff-index --cached HEAD --exit-code --quiet 2>&1
	then
		die "fatal: index has modifications.  Cannot add."
	fi
}

# Fix for git diff-index --cached HEAD
# git rm -r --cached . or git rm -r --cached ... (define)