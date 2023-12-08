#!/bin/bash
# 0) FUNCS
ask_to_delete() {
  local dir_path="$1"

  read -p "Do you want to delete the directory '$dir_path'? (y/n): " confirm
  if [ "$confirm" == "y" ] || [ "$confirm" == "Y" ]; then
    echo "Deleting the directory '$dir_path'..."
    rm -rf "$dir_path"
  else
    echo "Skipping the deletion."
  fi
}

get_sudo_password() {
  # Prompt the user for the sudo password
  read -s -p "Please enter your sudo password: " sudo_password
  echo "$sudo_password"
}

# 1) SUDO AUTH
# Get sudo password from user input
sudo_password=$(get_sudo_password)
# Auth script using sudo password
echo -n "$sudo_password" | sudo -S pwd
# Check if authentication was successful (optional)
if [ $? -eq 0 ]; then
  echo "Authentication successful"
else
  echo "Authentication failed"
  exit 1
fi

# 2) ENV VARS
# Define system env vars
export GIT_DIR="/opt/git"
export PROJECT_NAME="projects"
export PROJECT_DIR="$GIT_DIR/$PROJECT_NAME"
export POETRY_VERSION=1.7.0
export PYTHON_VERSION=3.11
export PYTHON=python$PYTHON_VERSION
export REPO_URL="https://github.com/AleksNeStu/projects.git"

# 3) SYSTEM DEPENDENCIES
# Install system python dependencies and poetry dependency management
sudo dnf install $PYTHON -y
sudo dnf install $PYTHON-devel.x86_64 -y # for Cython compilation for IDE
sudo install git-subtree -y
#curl -sSL https://install.python-poetry.org | $PYTHON - --version $POETRY_VERSION
$PYTHON -m pip install poetry==$POETRY_VERSION

# 4) CLONE PROJECT
# Specify the target directory where you want to clone the repository
# Check if the target directory already exists
if [ -d "$PROJECT_DIR" ]; then
  read -p "Git project already exists in $PROJECT_DIR. Do you want to delete it and re-clone? (y/n): " confirm
  if [ "$confirm" == "y" ] || [ "$confirm" == "Y" ]; then
    echo "Deleting the existing directory and re-cloning."
    rm -rf "$PROJECT_DIR" # Remove the existing directory
    # Create project dir and clone the project
    mkdir -p $PROJECT_DIR
    cd $PROJECT_DIR
    # Clone the repository if it doesn't exist
    git clone --depth=1 "$REPO_URL" "$PROJECT_DIR"
  else
    echo "Skipping the clone operation, just pull."
    cd $PROJECT_DIR && pwd
    #    git config --unset core.bare
    git pull $REPO_URL
  fi
else
  # Create project dir and clone the project
  mkdir -p $PROJECT_DIR && cd $PROJECT_DIR
  # Clone the repository if it doesn't exist
  git clone --depth=1 "$REPO_URL" "$PROJECT_DIR"
fi

## 5) PROJECT (PYTHON) DEPENDENCIES
## Install project dependencies
#cd $PROJECT_DIR; rm -rf .venv
#$PYTHON -m poetry config virtualenvs.in-project true
#$PYTHON -m poetry env use $PYTHON_VERSION
#source $PROJECT_DIR/.venv/bin/activate
#which python
##!/opt/git/projects/.venv/bin/python
#$PYTHON -m poetry in

# 5) PROJECT (PYTHON) DEPENDENCIES
# Install project dependencies
cd $PROJECT_DIR
# Handle .venv
if [ -d "$PROJECT_DIR/.venv" ]; then
  ask_to_delete "$PROJECT_DIR/.venv"
else
  echo "The directory '$PROJECT_DIR/.venv' does not exist."
fi

poetry config virtualenvs.in-project true
#$PYTHON -m poetry config virtualenvs.in-project true
poetry env use $PYTHON_VERSION
#$PYTHON -m poetry env use $PYTHON_VERSION
source .venv/bin/activate
which python
#!/opt/git/projects/.venv/bin/python
#$PYTHON -m poetry install --no-root
poetry install --no-root

# Warning: The file chosen for install of executing 2.0.0 (executing-2.0.0-py2.py3-none-any.whl) is yanked. Reason for being yanked: Released 2.0.1 which is equivalent but added 'python_requires = >=3.5' so that pip install with Python 2 uses the previous version 1.2.0.
