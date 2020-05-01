release: python manage.py collectstatic --noinput
release: python manage.py compress --force
release: python manage.py collectstatic --noinput
release: python manage.py migrate
release: python manage.py populate_db --categories 10 --products 20
web: gunicorn purbeurre.wsgi