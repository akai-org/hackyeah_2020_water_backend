release: cp hackyeah_2020_water_backend/.settings.py hackyeah_2020_water_backend/settings.py
release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn hackyeah_2020_water_backend.wsgi --log-file -
