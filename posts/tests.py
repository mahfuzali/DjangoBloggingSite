from django.test import TestCase
from posts.models import Post

import datetime


# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="example title", subtitle="example subtitle", description="example subtitle",
                            date=datetime.date(2020, 5, 4))

    def test_animals_can_speak(self):
        post = Post.objects.get(title="example title")
        self.assertIsNotNone(post)
