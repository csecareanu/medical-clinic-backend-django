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
    County: any number value between 1 and 41
    User type: any nubmer value between 1 and 4 (ADMIN = 4 will set automatically)
mkdir log
python3 manage.py runserver
```
The admin user created with `python3 manage.py createsuperuser` doesn't have a token associated.\
To create a token open a web browser:
- http://127.0.0.1:8000/admin/
- Tokens
- ADD TOKEN
- Choose the admin user from 'User' drop down box
- Save


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
