# git branch -D `git branch --merged | grep -v \* | xargs`
# git branch --merged | grep -v \* | xargs git branch -D

git for-each-ref --format '%(refname:short)' refs/heads | grep -v "master\|main" | xargs git branch -D
