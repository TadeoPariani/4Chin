from .models import Category

class categoryRepository:

    def get_all_categories(self) -> Category.objects:
        return Category.objects.all()

    def create_category(
        self, name:str
    ) -> Category:

        category = Category.objects.create(
            name=name,
        )
        return category