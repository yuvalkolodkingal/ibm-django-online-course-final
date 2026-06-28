# IBM Django Final Project — Online Course Assessment

Django assessment feature for the IBM "Django Application Development with SQL and Databases" final project.

## Coursera submission URLs

| Task | URL |
|------|-----|
| 1 — models.py | https://github.com/yuvalkolodkingal/ibm-django-online-course-final/blob/main/onlinecourse/models.py |
| 2 — admin.py | https://github.com/yuvalkolodkingal/ibm-django-online-course-final/blob/main/onlinecourse/admin.py |
| 4 — course_details_bootstrap.html | https://github.com/yuvalkolodkingal/ibm-django-online-course-final/blob/main/onlinecourse/templates/onlinecourse/course_details_bootstrap.html |
| 5 — views.py | https://github.com/yuvalkolodkingal/ibm-django-online-course-final/blob/main/onlinecourse/views.py |
| 6 — urls.py | https://github.com/yuvalkolodkingal/ibm-django-online-course-final/blob/main/onlinecourse/urls.py |

Screenshots (Tasks 3 & 7): upload `submission/03-admin-site.png` and `submission/07-final.png` from this repo (or your local copy).

## Run locally

```bash
python -m venv venv
./venv/bin/pip install Django Pillow
./venv/bin/python manage.py migrate
./venv/bin/python manage.py createsuperuser
./venv/bin/python manage.py runserver
```

Test user (if seeded): `testuser` / `testpass123`
