# Ejercicio 25: test for Post model
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
User = get_user_model()
class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
    def test_crear_post(self):
        p = Post.objects.create(titulo='t', cuerpo='c', autor=self.user)
        self.assertEqual(str(p), 't')
