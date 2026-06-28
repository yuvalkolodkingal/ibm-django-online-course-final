# IBM Django Final Project — Online Course Assessment

Django assessment feature for the IBM "Django Application Development with SQL and Databases" final project.

## Coursera submission URLs

Replace `REPO` with this repository name after push:

| Task | URL |
|------|-----|
| 1 — models.py | `https://github.com/yuvalkolodkingal/REPO/blob/master/onlinecourse/models.py` |
| 2 — admin.py | `https://github.com/yuvalkolodkingal/REPO/blob/master/onlinecourse/admin.py` |
| 4 — course_details_bootstrap.html | `https://github.com/yuvalkolodkingal/REPO/blob/master/onlinecourse/templates/onlinecourse/course_details_bootstrap.html` |
| 5 — views.py | `https://github.com/yuvalkolodkingal/REPO/blob/master/onlinecourse/views.py` |
| 6 — urls.py | `https://github.com/yuvalkolodkingal/REPO/blob/master/onlinecourse/urls.py` |

Screenshots (Tasks 3 & 7): see `submission/03-admin-site.png` and `submission/07-final.png`.

## Run locally

```bash
python -m venv venv
./venv/bin/pip install Django Pillow
./venv/bin/python manage.py migrate
./venv/bin/python manage.py createsuperuser
./venv/bin/python manage.py runserver
```

Test user (if seeded): `testuser` / `testpass123`
