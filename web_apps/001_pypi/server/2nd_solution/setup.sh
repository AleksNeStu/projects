#!/usr/bin/env zsh

# uwsgi
/pypi/server/2nd_solution/pypi.service /etc/systemd/system/pypi.service
systemctl start pypi && systemctl enable pypi

# nginx
rm /etc/nginx/sites-enabled/default
cp /pypi/server/2nd_solution/pypi.nginx /etc/nginx/sites-enabled/pypi.nginx
update-rc.d nginx enable
service nginx restart

# ssl
add-apt-repository ppa:certbot/certbot
apt install python-certbot-nginx
certbot --nginx -d fake-pypi.nestu.com
