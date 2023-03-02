from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create(
            username = 'test username',
            password = 'test password',
            email = 'test email@gmail.com',
        )

        cls.post = Post.objects.create(
            title = 'test title',
            body = 'test body',
            author = cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'test username')
        self.assertEqual(self.post.title, 'test title')
        self.assertEqual(self.post.body, 'test body')
        self.assertEqual(str(self.post), 'test title')
