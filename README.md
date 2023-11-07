# Blog_Django

Este es un blog desarrollado utilizando el framework Django.

## Requisitos

- Python 3.x
- Django 3.x
- Django REST FrameWork 3.x
- Otros requisitos del entorno virtual o servidor de desarrollo si los hay

## Instalación

1. Clonar el repositorio o descargar el código fuente.
2. Crear y activar un entorno virtual.
3. Instalar las dependencias del proyecto ejecutando el comando `pip install -r requirements.txt`.
4. Aplicar las migraciones de la base de datos ejecutando el comando `python3 manage.py migrate`.
5. Iniciar el servidor de desarrollo ejecutando el comando `python3 manage.py runserver`.

## Admin

- Usuario: admin
- Contraseña: admin

## Uso

- Accede al blog en tu navegador web utilizando la URL `http://localhost:8000`.
- Regístrate o Logueate como usuario para poder crear, y eliminar tus propios artículos.
- Navega por los diferentes artículos publicados.
- Comenta en los artículos publicados por otros usuarios.


## Uso de la API

La API Posee los endpoints de Users, Posts, Comments y Categories.

<<<<<<< HEAD
Tanto el GET como el POST se realizan de igual forma para cualquier modelo:
=======
Tanto el GET, POST y DELETE se realizan de igual forma para cualquier modelo:
>>>>>>> prueba

- Endpoint: http://127.0.0.1:8000/api/-modelo_requerido-/

- Endpoint: http://127.0.0.1:8000/api/posts/

<<<<<<< HEAD
=======
- Endpoint: http://127.0.0.1:8000/api/usuarios/

- Endpoint: http://127.0.0.1:8000/api/comentarios/

>>>>>>> prueba

#### Traer un Usuario

- Método: `GET`
- Endpoint: http://127.0.0.1:8000/api/usuarios/

<<<<<<< HEAD
```json
=======
>>>>>>> prueba
Respuesta:

[
  {
    "id": 21,
    "username": "tadeo",
    "email": "parianitadeo@gmail.com",
    "password": "tadeo"
  },
  {
    "id": 22,
    "username": "prueba1",
    "email": "email@gmail.com",
    "password": "1234"
  },
  {
    "id": 23,
    "username": "prueba2",
    "email": "email@gmail.com",
    "password": "1234"
  }
]
<<<<<<< HEAD
```json
=======

>>>>>>> prueba

#### Crear un nuevo usuario

- Método: `POST`
- Endpoint: http://127.0.0.1:8000/api/usuarios/

<<<<<<< HEAD

**Solicitud**


=======
**Solicitud**

>>>>>>> prueba
{
    "nombre": "Juan",
    "correo": "juan@example.com",
    "edad": 25
}

Respuesta:

{
    "id": 1,
    "nombre": "Juan",
    "correo": "juan@example.com",
    "edad": 25
}

<<<<<<< HEAD
Response Headers: 

Header Value
date: Wed, 01 Nov 2023 22:39:12 GMT
server: WSGIServer/0.2 CPython/3.10.12
content-type: application/json
vary: Accept, Cookie
allow: GET, POST, HEAD, OPTIONS
x-frame-options: DENY
content-length: 74
x-content-type-options: nosniff
referrer-policy: same-origin
cross-origin-opener-policy: same-origin
=======
---------------------------------------------------------------------------------

#### Crear un post

- Método: `POST`
- Endpoint: http://127.0.0.1:8000/api/posts/

**Solicitud**

{
  "author":21,
  "title": "prueba23",
  "content": "prueba23",
  "category_id": 2
}


#### Borrar un post

debe incluir en la url el id del post a borrar

- Método: `DELETE`
- Endpoint: http://127.0.0.1:8000/api/posts/34

Puede verificar si se ha borrado realizando un GET o viendolo desde el Admin de Django
>>>>>>> prueba


# Otros 

- La base de datos ya deberia tener categorias precargadas, si no es el caso, las puede crear desde el admin de Django