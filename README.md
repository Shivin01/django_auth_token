# djangoauthtoken
Django auth solution for Token creation/updation for a session.

### Run make migratons command:

```
python manage.py makemigrations djangoauthtoken
```

## Run command to migrate:

```
python manage.py migrate
```

## Run command to create superuser

```
python manage.py createsuperuser
```


Things to do:

- [X] Add api for Token.
- [X] Add api for login.
- [] Add api for RefreshToken.
- [] Add manager for create user.
- [] Add manager for create token.
- [] Add serializer for user.
- [] Add serializer for token.
- [] Add JWT token logic to this module.
- [] Add github Actions.
- [] Add pypi module push in this code base.
- [] Add api for user sign up.
- [] Add a custom command to delete invalid tokens.
