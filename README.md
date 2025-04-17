
# دو بیتی های عاشقانه


یه پروژه ی ساده اما کاربردی.
این پروژه برای یک صفحه ی فیسبوک آماده شده
که گویا در آن با شعر و ویدیو های کوتاه تولید محتوا میکند.

## ویژگی‌ها

### پست
<blockquote>
    <li> پست گذاری فقط برای ادمیت از طریق پنل مدیریت. </li>
    <li> موزیک و ویدیو و تصویر برای هر پست </li>
    <li> لایک و کامنت برای پست ها</li>
    <li> تاریخ شمسی</li>
    <li> پلیر شخصی سازی شده برای ویدیو و موزیک</li>
</blockquote>

### اکانت
<blockquote>
    <li> ثبت نام برای کاربر</li>
    <li> تایید ایمیل</li>
    <li> ورود به سیستم</li>
</blockquote>

## ابزار ها
- `django`
- `persiantools` برای تاریخ شمسی
- `pillow` برای کار تصایر در پست ها
- `python-decouple` .env


## نصب و راه‌اندازی

برای نصب و راه‌اندازی پروژه به صورت محلی، مراحل زیر را دنبال کنید:

1. **کلون کردن پروژه**:
   ```bash
   git clone https://github.com/Akbaroo/dobiti.git
   ```

2. **نصب وابستگی‌ها**:
   از `pip` برای نصب وابستگی‌ها استفاده کنید:
   ```bash
   pip install -r requirements.txt
   ```

3. **تنظیمات محیطی**:
   فایل `.env` خود را پیکربندی کنید. مثال:
   ```
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=your_email@gmail.com
    EMAIL_HOST_PASSWORD=your_app_password
    DEFAULT_FROM_EMAIL=your_email@gmail.com
   ```

4. **اجرای پروژه**:
   برای راه‌اندازی پروژه محلی:
   ```bash
   python manage.py collectstatic
   python manage.py runserver
   ```

5. **اجرای مایگریشن‌ها**:
   اگر از پایگاه‌داده استفاده می‌کنید، مایگریشن‌ها را اجرا کنید:
   ```bash
   python manage.py migrate
   ```


## آزمایش‌ها
فعلا تست درستی نوشته نشده

## ساختار پوشه‌ها

شرحی از ساختار پوشه‌ها و فایل‌های پروژه:

```
dobiti/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
|
├── blogs/
│   ├── migrations/
│   ├── static/
│   ├── tests/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── sitemap.py
│   ├── urls.py
│   └── views.py
│
├── media/
├── static/
├── templates/
├── .env
├── .gitignore
├── commit_name_chatgpt.md
├── manage.py
├── README.md
├── requirements.txt
└── roadmap.md
```

## همکاری و مشارکت

برای مشارکت در پروژه، مراحل زیر را دنبال کنید:

1. این مخزن را fork کنید.
2. تغییرات خود را اعمال کرده و یک pull request ارسال کنید.

## لایسنس

### MIT