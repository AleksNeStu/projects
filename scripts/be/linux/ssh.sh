#!/bin/bash
# https://www.cyberciti.biz/faq/how-to-set-up-ssh-keys-on-linux-unix/
# - Create the key pair
ssh-keygen -m PEM -t rsa -b 4096
# - Install the public key in remote server
ssh-copy-id -i $HOME/.ssh/id_rsa.pub user@server_ip
# or
scp $HOME/.ssh/id_rsa.pub user@server_ip:~/.ssh/authorized_keys
# - Connect
ssh user@server_ip
ssh -i ~/.ssh/your-key user@server_ip




# Connect
sshpass -p “ENTER PASSWORD HERE” ssh testuser@192.168.10.10

ssh -p “MY@Password”  ssh shusain@192.168.10.10