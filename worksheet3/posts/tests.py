from django.test import TestCase
from django.urls import reverse
from django.models import Post
# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text+'this is another test')

    def test_view_url_exits_at_proper_location(self):
         resp = self.client.get(reverse('/'))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_corect_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')