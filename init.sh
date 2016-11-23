rm -r /etc/nginx/sites-enabled/default
ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled
rm -r /etc/gunicorn.d/*
ln -s /home/box/web/etc/hello.conf /etc/gunicorn.d
ln -s /home/box/web/etc/ask.conf /etc/gunicorn.d
git config user.email "gdancerx@gmail.com"
git config user.name "Denis Volkov"

