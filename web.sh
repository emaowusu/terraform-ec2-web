#!/bin/bash

apt update
apt install wget unzip apache2 -y
systemctl start apache2
systemctl enable apache2
wget https://www.tooplate.com/zip-templates/2144_parallax_depth.zip
unzip -o 2144_parallax_depth.zip
cp -r 2144_parallax_depth/* /var/www/html/
systemctl restart apache2
