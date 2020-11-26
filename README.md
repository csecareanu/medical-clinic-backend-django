# medical-clinic-backend-django

## Documentation

### Install the project
```
git clone https://github.com/csecareanu/medical-clinic-backend-django.git
cd medical-clinic-backend-django
python3 -m venv venv
source venv/bin/activate
pip install Django
pip install Djangorestframework
python3 manage.py makemigrations authentication
python3 manage.py migrate
python3 manage.py createsuperuser
    User type: 1 (1 = admin)
mkdir log
python3 manage.py runserver
```

### Django REST framework

* Quickstart
    - https://www.django-rest-framework.org/tutorial/quickstart/
* Tutorial
    - https://www.django-rest-framework.org/tutorial/1-serialization/    
* Serializers
    - https://www.django-rest-framework.org/api-guide/serializers/
* Permissions 
    - https://www.django-rest-framework.org/api-guide/permissions/
* ViewSets
    - https://www.django-rest-framework.org/api-guide/viewsets/
    
### Models
* Model API reference
    - https://docs.djangoproject.com/en/3.1/ref/models/
* QuerySet API reference
    - https://docs.djangoproject.com/en/3.1/ref/models/querysets/
