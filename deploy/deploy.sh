cd /root/biserici-inlemnite
git pull
docker-compose -f production.yml build django
docker-compose -f production.yml run django python manage.py dump_config --format amd > frontend/src/models_fragmente.js
docker-compose -f production.yml run django python manage.py save-biserici-options
docker-compose -f production.yml build frontend
docker-compose -f production.yml run postgres backup
docker-compose -f production.yml run django python manage.py migrate
docker-compose -f production.yml run django python manage.py invalidate all
docker-compose -f production.yml down
docker-compose -f production.yml up -d

