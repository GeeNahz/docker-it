# Project setup process

## Edit the following
- djangodocker/urls.py - L2,L6
- api/urls.py
- djangodocker/settings.py - L13,L16,L37-L39,L48-L61,L97-L106
- api/models.py
- api/admin.py - L2-L8
- api/serializers.py

## Docker compose commands
- docker-compose build &rightarrow; build images
- docker-compose up db &rightarrow; run db container
- docker-compose up &rightarrow; run api container
- docker exec -it <container_name> sh &rightarrow; enter interactive (-it) container shell
- * Ensure that you're in the same directory as **manage.py** file
```
$ ls
```
- Run migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
