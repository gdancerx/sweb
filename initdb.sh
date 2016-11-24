mysql -uroot -e "CREATE DATABASE sweb;"
mysql -uroot -e "CREATE USER 'sweb'@'localhost' IDENTIFIED BY 'qazqwe';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON sweb.* TO 'sweb'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
