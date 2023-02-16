pip install django

pip install djangorestframework

python manage.py runserver


w razie potrzeby przed runserver robimy 

usuwamy pliczki z pai/migrations poza tymi co sa __costam__

python manage.py makemigrations pai

python manage.py migrate --fake-initial

python manage.py runserver

