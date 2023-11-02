#!/bin/bash
cd /home/uk/Netology-Django-1
git pull origin video
source 3.2-crud/env/bin/actiavte
pip install -r 3.2-crud/stocks_products/requirements.txt
python 3.2-crud/stocks_products/manage.py migrate
sudo systemctl restart gunicorn
