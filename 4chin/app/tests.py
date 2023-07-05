from django.test import TestCase
import pytest

from .repository import categoryRepository
from .models import Category


@pytest.mark.django_db
def test_create_category():
    name = "ciencia"
    repository = categoryRepository()
    category = repository.create_category(
        name
    )

    assert category.name == name
    print("La categoría se creó exitosamente.")