rm -r /etc/nginx/sites-enabled/default
ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled
git clone https://github.com/gdancerx/sweb.git /home/box/web
