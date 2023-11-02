from django.test import TestCase
import pytest
# from rest_framework.test import APITestCase
# from rest_framework import status
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



# @pytest.mark.django_db
# def test_lista_usuarios(self):
#         response = self.client.get('/api/usuarios/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         print("La categoría se creó exitosamente.")

# @pytest.mark.django_db
# def test_creacion_usuario(self):
#     data = {
#         'username': 'Test',
#         'email': 'Test@example.com',
#         'password': 'test'
#     }

#     response = self.client.post('/api/usuarios/', data)
#     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     print("La categoría se creó exitosamente.")
