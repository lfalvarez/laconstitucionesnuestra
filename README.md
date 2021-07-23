# La Constitución es Nuestra

Este es un proyecto que busca hacer llegar propuestas de la ciudadanía a las personas que escriben la Constitución de Chile =)

## Para instalar:

1) Primero debes tener un virtualenv que puedes crear as:
```shell
mkvirtualenv lcen -a $(pwd) --python=python3
```

2) Debes instalar las dependencias así:
```shell
pip install -r requirments.txt
```


3) Debes crear un archivo `lcen/.env` y llenarlo con los siguientes datos:

```
SECRET_KEY=un_secret
DEBUG=True
ALLOWED_HOSTS=localhost
STATIC_URL=/static/
STATIC_ROOT=/static
STATICFILES_DIRS=static
MEDIA_ROOT=<PUEDE_SER_EL_DIRECTORIO_ACTUAL>
MEDIA_URL=""
DB_NAME=<NOMBRE_DB>
DB_USER=<USER_DB>
DB_PASSWORD=<PASSWORD_DE_MYSQL>
DB_HOST=<HOST_DE_MYSQL>
```


4) Debes correr el proyecto así:

```
python lcen/manage.py runserver
```

5) podrás acceder desde [localhost:8000](http://localhost:8000)
