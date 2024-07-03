# djangoauthtoken

Django auth solution for Token creation/updation for a session.

## Add Djangoauthtoken in your project.

Add `djangoauthtoken` in your INSTALLED_APPS settings to see in action.

## Add This seeting is your project

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'djangoauthtoken.middleware.CustomTokenAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    ],
}
```

### Run make migratons command:

```sh
python manage.py makemigrations djangoauthtoken
```

## Run command to migrate:

```sh
python manage.py migrate
```

## Run command to create superuser

```sh
python manage.py createsuperuser
```

Things to do:

- [X] Add api for Token.
- [X] Add api for login.
- [X] Add api for RefreshToken.
- [X] Add manager for create token.
- [X] Add serializer for user.
- [X] Add manager for create user.
- [X] Add api for user sign up.
- [X] Add github Actions.
- [X] Add pypi module push in this code base.
- [] Add a custom command to delete invalid tokens.
- [] Update README with screenshots and other details.




