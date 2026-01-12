# TajribaBlog

Oddiy, to'liq Django freymvorkida yozilgan blog loyihasi.  
Bu loyihada REST API (Django REST Framework) ishlatilmagan — hammasi klassik Django usulida: templates, views, forms va models orqali.

Foydalanuvchilar ro'yxatdan o'tib, o'z tajribalari/postlarini yozishi, tahrirlashi, o'chirishi va boshqalarga ko'rsatishi mumkin.

Dizayn juda sodda (Bootstrap 5 ishlatilgan), chunki loyiha asosan backend va oddiy frontendni o'rganish uchun qilingan.

## Asosiy xususiyatlar

- Foydalanuvchi ro'yxatdan o'tish / kirish / chiqish (Django built-in auth)
- Yangi post (tajriba) qo'shish
- O'z postlarini tahrirlash va o'chirish
- Barcha postlarni ko'rish (home page)
- Har bir postning batafsil sahifasi
- Postga oddiy comment qoldirish (kelajakda rivojlantirish mumkin)
- Admin panel orqali to'liq boshqaruv

## Texnologiyalar stacki

- **Backend**: Django 4.x / 5.x (Python 3.10+)
- **Frontend**: Django Templates + Bootstrap 5 (oddiy HTML/CSS/JS)
- **Ma'lumotlar bazasi**: SQLite (development uchun), PostgreSQL (productionda tavsiya etiladi)
- Hech qanday JavaScript framework yo'q (React, Vue va h.k. ishlatilmagan)
- REST API yo'q — hammasi server-side rendering

## Loyiha holati

- Development bosqichida / o'quv loyihasi
- Funksional, lekin dizayn va optimallashtirish hali sodda

## Tezkor o'rnatish (Installation)

```bash
# 1. Repozitoriyani klon qilish
git clone https://github.com/Abdumajid77/TajribaBlog.git
cd Blog

# 2. Virtual muhit yaratish va faollashtirish
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Kerakli paketlarni o'rnatish
pip install -r requirements.txt

# 4. Muhit o'zgaruvchilari (ixtiyoriy, lekin tavsiya etiladi)
# .env fayl yarating va quyidagilarni qo'shing:
# SECRET_KEY='sizning-yashirin-kalitingiz'
# DEBUG=True

# 5. Migratsiyalarni bajarish va superuser yaratish
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 6. Serverni ishga tushirish
python manage.py runserver