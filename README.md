# HACKYEAH 2020 Water App

## How to install

1. Download repo,
2. Initialize virtual environment in it: `python -m venv venv`,
3. Run that venv: `source venv/bin/activate`,
4. Install dependencies: `pip install -r requirements.txt`,
5. Copy pyvenv.example.cnf to pyvenv.cnf and fill in credentials
6. Migrate database: `python manage.py migrate`,
7. Seed data: `python manage.py loaddata seed.json`
8. To run dev server: `python manage.py runserver`
9. PRODUCTION ONLY -> manage static files `python manage.py collectstatic`

## Tips for devs

### Dumping pip installations into the file

If you installed new pip dependency you need to allow others to know about it. To do so it is best to save all requirements
in one file, which in this case in named `requirements.txt`. You can do this by typing following command:

`pip freeze > requirements.txt`

### Dumping down data

`python manage.py dumpdata --indent 2 -e=admin.logentry -e=sessions -e=contenttypes -e=auth.permission --natural-foreign --natural-primary -o seed.json`
