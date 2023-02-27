from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book

# Create your tests here.
class APITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = 'test title api',
            subtitle = 'test subtitle api',
            author = 'test author api',
            isbn = 'test isbn api',
        )

    def test_api_listview(self):
        response = self.client.get(reverse('book_list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Book.objects.count(), 1)
        self.assertContains(response, self.book)
