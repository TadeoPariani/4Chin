# Blog_Django

Este es un blog desarrollado utilizando el framework Django.

## Requisitos

- Python 3.x
- Django 3.x
- Otros requisitos del entorno virtual o servidor de desarrollo si los hay

## Instalación

1. Clonar el repositorio o descargar el código fuente.
2. Crear y activar un entorno virtual.
3. Instalar las dependencias del proyecto ejecutando el comando `pip install -r requirements.txt`.
4. Aplicar las migraciones de la base de datos ejecutando el comando `python manage.py migrate`.
5. Iniciar el servidor de desarrollo ejecutando el comando `python manage.py runserver`.

## Uso

## Admin
Usuario: admin
Contraseña: admin

- Accede al blog en tu navegador web utilizando la URL `http://localhost:8000`.
- Navega por los diferentes artículos publicados.
- Regístrate como usuario para poder crear, editar y eliminar tus propios artículos.
- Comenta en los artículos publicados por otros usuarios.

## Estructura del proyecto

El proyecto está estructurado de la siguiente manera:

- `sitio/`: Contiene la configuración principal del proyecto Django.
- `app/`: Contiene la aplicación principal del blog.
- `templates/`: Directorio que almacena las plantillas HTML.
- `static/`: Directorio que almacena los archivos estáticos como CSS, JS e imágenes.
- `media/`: Directorio donde se guardan los archivos multimedia subidos por los usuarios.
- `manage.py`: Archivo de gestión del proyecto Django.
