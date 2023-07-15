# recipe-app-django
django pilot for testing and studying 

# Run project
docker-compose up

# Run test in the container
docker-compose run --rm app sh -c "python manage.py test"

# Run linting in the container
docker-compose run --rm app sh -c "flake8"