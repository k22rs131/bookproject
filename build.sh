# build.shファイル

#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

git add requirements.txt
git commit -m "fix: add python-decouple"
git push

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py superuser