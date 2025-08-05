# from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import BlogPost, Comment

class BlogAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.blog = BlogPost.objects.create(
            title='Test Blog',
            content='This is a test blog.',
            author=self.user
        )

    def test_blog_post_creation(self):
        self.assertEqual(self.blog.title, 'Test Blog')
        self.assertEqual(self.blog.author.username, 'testuser')

    def test_login_view(self):
        login = self.client.login(username='testuser', password='testpass')
        self.assertTrue(login)

    def test_post_list_view_requires_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_post_list_view_after_login(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Blog')

    def test_comment_creation(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(f'/post/{self.blog.pk}/', {
            'content': 'Nice post!'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after comment
        self.assertEqual(Comment.objects.count(), 1)
