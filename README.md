# recipe-app-django
django pilot for testing and studying 

# Run project
docker-compose up

# Run test in the container
docker-compose run --rm app sh -c "python manage.py test"

# Run linting in the container
docker-compose run --rm app sh -c "flake8"

# Run testing and linting in the container
docker-compose run --rm app sh -c "python manage.py test && flake8"

# Starting new app
docker-compose run --rm app sh -c "python manage.py startapp new_app"

# Making migrations 
docker-compose run --rm app sh -c "python manage.py makemigrations"

# Getting down docker-compose
docker-compose down

# Refresing database
docker volume ls
docker-compose down
docker volume rm recipe-app-django_dev-db-data
docker-compose up
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

# Creating super user
docker-compose run --rm app sh -c "python manage.py createsuperuser"
