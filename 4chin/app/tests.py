from django.test import TestCase
import pytest
from rest_framework.test import APIClient  # Importa APIClient desde rest_framework.test
from rest_framework import status
from .repository import categoryRepository

@pytest.mark.django_db
def test_create_category():
    name = "ciencia"
    repository = categoryRepository()
    category = repository.create_category(
        name
    )
    assert category.name == name
    print("La categoría se creó exitosamente.")

@pytest.mark.django_db
def test_lista_usuarios():
    client = APIClient()  
    response = client.get('/api/usuarios/')
    assert response.status_code == status.HTTP_200_OK
    print("La lista de usuarios se obtuvo exitosamente.")

@pytest.mark.django_db
def test_creacion_usuario():
    client = APIClient()  
    data = {
        'username': 'Test',
        'email': 'Test@example.com',
        'password': 'test'
    }

    response = client.post('/api/usuarios/', data)
    assert response.status_code == status.HTTP_201_CREATED
    print("El usuario se creó exitosamente.")

@pytest.mark.django_db
def test_lista_posts():
    client = APIClient()  
    response = client.get('/api/posts/')
    assert response.status_code == status.HTTP_200_OK
    print("La lista de posts se obtuvo exitosamente.")

@pytest.mark.django_db
def test_creacion_post():
    client = APIClient()  
    data = {
        "title": "prueba23",
        "content": "prueba23",
        "author_id":21,
        "creation_date":"2023-11-05 00:08:11.646248",
        "category_id": 3
    }

    response = client.post('/api/posts/', data)
    assert response.status_code == status.HTTP_201_CREATED
    print("El post se creó exitosamente.")

@pytest.mark.django_db
def test_creacion_comment():
    client = APIClient()  
    data = {
        "author_id":21,
        "post_id": 34,
        "text":"eeeeeeeee"
    }

    response = client.post('/api/comentarios/', data)
    assert response.status_code == status.HTTP_201_CREATED
    print("El comentario se creó exitosamente.")

    
