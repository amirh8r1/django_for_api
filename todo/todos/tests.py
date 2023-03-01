from django.test import TestCase
from .models import Todo

# Create your tests here.
class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title = 'Test Title',
            body = 'Test Body',
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'Test Title')
        self.assertEqual(self.todo.body, 'Test Body')
        self.assertEqual(str(self.todo), 'Test Title')
