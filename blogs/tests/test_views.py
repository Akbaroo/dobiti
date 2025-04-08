from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):

    def test_homepage_loads(self):
        # ارسال درخواست GET به صفحه اصلی
        response = self.client.get(reverse('home'))  # فرض می‌کنیم نام URL شما 'home' است

        # بررسی اینکه صفحه به درستی بارگذاری شده
        self.assertEqual(response.status_code, 200)  # باید 200 OK برگردونه
        self.assertContains(response, 'آخرین پست‌ها')  # بررسی اینکه عنوان «آخرین پست‌ها» در صفحه هست
