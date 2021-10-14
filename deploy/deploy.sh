cd /root/biserici-inlemnite
git pull
docker-compose -f production.yml build
docker-compose -f production.yml run postgres backup
docker-compose -f production.yml run django python manage.py migrate
docker-compose -f production.yml run django python manage.py import-constante
docker-compose -f production.yml down
docker-compose -f production.yml up -d

