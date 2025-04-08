from django.test import TestCase
from ..models import Post

class PostModelTest(TestCase):

    def test_create_post(self):
        # ساخت یک پست جدید
        post = Post.objects.create(title='اولین پست', content='این محتوا است')
        
        # بررسی اینکه پست به درستی ذخیره شده
        self.assertEqual(post.title, 'اولین پست')
        self.assertEqual(post.content, 'این محتوا است')
        self.assertTrue(post.created_at)  # باید تاریخ ایجاد داشته باشه
