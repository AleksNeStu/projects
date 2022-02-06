# https://hub.docker.com/_/python
FROM ubuntu:20.04
MAINTAINER AlexNeStu


#TODO: Make possibility to chose approach:
# 1) Real time 2) Copy projecet 3) Git clone (default)
#TODO: Add SSH
# Real time approach
# WORKDIR /pypi


# Copy approach
#ADD . /pypi


# Git clone approach
RUN mkdir /pypi && chmod 777 /pypi
WORKDIR /pypi


# Time zone
RUN ln -fs /usr/share/zoneinfo/Europe/Warsaw /etc/localtime
# for apt-get install tzdata noninteractive


RUN apt update
RUN apt upgrade -y


# Python 3.10
RUN apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt install -y python3.10 python3-pip python3-dev python3-venv \
    python3.10-dev python3.10-venv python-is-python3 && \
    # ln -sfn /usr/bin/python3.10 /usr/bin/python && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2 && \
    update-alternatives --auto python3
# https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/
# https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-10-on-ubuntu-18-04-and-20-04-lts/
# python-is-python3
#RUN apt install -y python3.10 && update-alternatives --install \
#/usr/bin/python3 python3 /usr/bin/python3.10 1 && sudo update-alternatives \
#--install /usr/bin/python3 python3 /usr/bin/python3.8 2 && \
#update-alternatives --config python3


# Pip3
RUN apt install -y python3.10-distutils curl
RUN sh -c "curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10" && \
#    apt purge -y python-pip python3-pip
     apt reinstall -y python3-pip


# Dependencies OS
RUN apt install -y zsh ufw git unzip zip nload tree \
    nginx fail2ban systemd
# gzip support in uwsgi
RUN apt install -y build-essential libpcre3-dev libz-dev \
    default-libmysqlclient-dev


# Shell ZSH
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/\
ohmyzsh/master/tools/install.sh)" "" --unattended \
    && chsh -s $(which zsh)
SHELL ["/bin/zsh", "-c"]

# Security
# https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
# https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04
#RUN ufw allow 22 && ufw allow 80 && ufw allow 443 && ufw enable


# Git
RUN git config --global credential.helper cache && \
    git config --global credential.helper 'cache --timeout=720000' && \
    #NOTE: Specify your account details
    git config --global user.email "git_user@gmail.com" && \
    git config --global user.name "Git User"



# Clone project (partialy)
RUN cd /tmp && git clone https://github.com/AleksNeStu/projects.git \
    --no-checkout --depth 1 --filter=blob:none && cd projects && \
    git sparse-checkout set web_apps/pypi
RUN cp -rf /tmp/projects/web_apps/pypi/* /pypi && rm -rf /tmp/projects


# Dependencies Python
RUN pip install --upgrade setuptools glances poetry
RUN cd /pypi && poetry config virtualenvs.in-project true && \
    rm -rf .venv && poetry install
# Server specific dependencies
RUN poetry add httpie uwsgi && poetry update
RUN echo "source /pypi/.venv/bin/activate" >> ~/.zshrc
RUN source /pypi/.venv/bin/activate

#NOTE: Connect to the container shell: `docker exec -it os zsh`
#NOTE: To access via browser: http://localhost:8080/

#NOTE: Docker commands:
# docker-compose -f docker-compose.yml build
# docker-compose -f docker-compose.yml build --no-cache
# docker-compose -f docker-compose.yml up + CTRL-C

# docker-compose -f docker-compose.yml up -d +
# docker-compose -f docker-compose.yml stop