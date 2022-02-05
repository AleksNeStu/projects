# https://hub.docker.com/_/python
FROM ubuntu:20.04
MAINTAINER AlexNeStu

# can be used mapped /pypi to realtime develpment end debugging
ADD . /pypi_run
WORKDIR /pypi_run

#
#ADD . /pypi
#WORKDIR /pypi

# Time zone
# apt-get install tzdata noninteractive
RUN ln -fs /usr/share/zoneinfo/Europe/Warsaw /etc/localtime


#RUN add-apt-repository ppa:deadsnakes/ppa && apt update
RUN apt update
#RUN apt upgrade -y


# Python 3.10
# https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/
# https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-10-on-ubuntu-18-04-and-20-04-lts/
# python-is-python3
#RUN apt install -y python3.10 && update-alternatives --install \
#/usr/bin/python3 python3 /usr/bin/python3.10 1 && sudo update-alternatives \
#--install /usr/bin/python3 python3 /usr/bin/python3.8 2 && \
#update-alternatives --config python3
RUN apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt install -y python3.10 python3-pip python3-dev python3-venv && \
    python3.10-dev python3.10-venv python-is-python3 && \
    # ln -sfn /usr/bin/python3.10 /usr/bin/python && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2 && \
    update-alternatives --auto python3



# Pip3
RUN apt install -y python3.10-distutils
RUN sh -c "curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10" && \
    apt purge -y python-pip python3-pip


# Dependencies OS
RUN apt install -y curl zsh ufw git unzip zip nload tree \
    nginx fail2ban systemd
# gzip support in uwsgi
RUN apt install -y build-essential libpcre3-dev libz-dev \
    default-libmysqlclient-dev


# Shell ZSH
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/\
ohmyzsh/master/tools/install.sh)" "" --unattended \
    && chsh -s $(which zsh)

# Security
# https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
# https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04
#RUN ufw allow 22 && ufw allow 80 && ufw allow 443 && ufw enable


# Git
RUN git config --global credential.helper cache && \
    git config --global credential.helper 'cache --timeout=720000' && \
    git config --global user.email "git_user@gmail.com" && \
    git config --global user.name "Git User"


# Dependencies Python
RUN pip install --upgrade setuptools glances poetry
RUN cd /pypi_run && poetry config virtualenvs.in-project true && \
    rm -rf .venv && poetry install && poetry add httpie uwsgi

## Venv
##RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
##RUN source .venv/bin/activate && pip3 install -r requirements.txt
#
#
#### App daemon
##RUN cp server/pypi.service /etc/systemd/system/pypi.service && \
##    systemctl start pypi && systemctl enable pypi
##
##
### Nginx
##RUN cp server/pypi.nginx /etc/nginx/sites-enabled/pypi.nginx && \
##    update-rc.d nginx enable && service nginx restart