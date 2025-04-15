# build.shファイル

#!/usr/bin/env bash
# exit on error
set -o errexit

git config --global user.email "k22rs131@st.kyusan-u.ac.jp"
git config --global user.name "k22rs131"

pip install -r requirements.txt
pip install django-environ

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py superuser