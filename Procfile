release: python manage.py collectstatic --noinput
release: python manage.py compress --force
release: python manage.py collectstatic --noinput
release: python manage.py migrate
web: gunicorn purbeurre.wsgi