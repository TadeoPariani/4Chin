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
    client = APIClient()  # Crea una instancia de APIClient
    response = client.get('/api/usuarios/')
    assert response.status_code == status.HTTP_200_OK
    print("La lista de usuarios se obtuvo exitosamente.")

@pytest.mark.django_db
def test_creacion_usuario():
    client = APIClient()  # Crea una instancia de APIClient
    data = {
        'username': 'Test',
        'email': 'Test@example.com',
        'password': 'test'
    }

    response = client.post('/api/usuarios/', data)
    assert response.status_code == status.HTTP_201_CREATED
    print("El usuario se creó exitosamente.")
    
