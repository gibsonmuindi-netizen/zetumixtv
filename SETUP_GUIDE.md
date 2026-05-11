# Streaming Platform - Setup Guide

## ✅ Completed Setup

You now have a fully initialized Kenyan Entertainment & Educational Streaming Platform with:

### Backend (Django)
- **Framework**: Django 6.0.5
- **Database Driver**: PostgreSQL (psycopg2)
- **API Framework**: Django REST Framework 3.17.1
- **Image Processing**: Pillow 12.2.0
- **Environment Management**: python-decouple 3.8

### Apps Created
1. **users** - User authentication and profiles
2. **videos** - Video upload and management
3. **payments** - M-Pesa integration
4. **subscriptions** - Subscription plans and management
5. **watchhistory** - Track user viewing activity

### Frontend (Next.js)
- **React** with TypeScript
- **Framework**: Next.js 16.2.5
- **Styling**: Tailwind CSS
- **Mobile-first design**

---

## 📁 Project Structure

```
streaming-platform/
├── backend_env/              # Python virtual environment
├── streaming_platform/       # Django project directory
│   ├── manage.py            # Django management command
│   ├── streaming_platform/  # Main Django settings
│   │   ├── settings.py      # Configuration (needs updating)
│   │   ├── urls.py          # Main URL routes
│   │   ├── asgi.py          # ASGI config
│   │   └── wsgi.py          # WSGI config
│   ├── users/               # User app
│   ├── videos/              # Video app
│   ├── payments/            # Payments app
│   ├── subscriptions/       # Subscriptions app
│   └── watchhistory/        # Watch history app
├── frontend/                 # Next.js project
│   ├── app/                 # App directory (Next.js 13+)
│   ├── public/              # Static files
│   ├── components/          # React components
│   ├── package.json         # Frontend dependencies
│   └── tsconfig.json        # TypeScript config
└── SETUP_GUIDE.md          # This file
```

---

## 🚀 Next Steps

### 1. **Configure Django Settings**

Edit `streaming_platform/settings.py`:

```python
# Add these apps to INSTALLED_APPS:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your apps
    'users.apps.UsersConfig',
    'videos.apps.VideosConfig',
    'payments.apps.PaymentsConfig',
    'subscriptions.apps.SubscriptionsConfig',
    'watchhistory.apps.WatchhistoryConfig',
    
    # Third party
    'rest_framework',
]

# Database configuration (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'streaming_platform_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',  # Change this
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# CORS configuration for frontend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Next.js frontend
]
```

Install CORS package:
```bash
backend_env\Scripts\pip.exe install django-cors-headers
```

### 2. **Create Database Models**

**users/models.py** - User model with custom fields
**videos/models.py** - Video and category models
**payments/models.py** - Payment transactions
**subscriptions/models.py** - Subscription plans and user subscriptions
**watchhistory/models.py** - Watch history records

### 3. **Run Migrations**

```bash
# Activate virtual environment
backend_env\Scripts\activate.bat

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### 4. **Install Frontend Dependencies**

```bash
cd frontend
npm install
```

### 5. **Start Development Servers**

**Terminal 1 - Backend:**
```bash
cd backend
backend_env\Scripts\activate.bat
python manage.py runserver
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Backend will run on: `http://localhost:8000`
Frontend will run on: `http://localhost:3000`

---

## 🔐 Environment Variables

Create `.env` files for configuration:

### Backend (.env in project root)
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/streaming_platform_db
MPESA_CONSUMER_KEY=your_mpesa_key
MPESA_CONSUMER_SECRET=your_mpesa_secret
MPESA_SHORTCODE=123456
CLOUDFLARE_R2_URL=your_r2_url
```

### Frontend (.env.local in frontend/)
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

---

## 📝 Key Database Tables Structure

### Users Table
- id (PK)
- full_name
- email (unique)
- phone_number
- password_hash
- subscription_status
- created_at
- updated_at

### Videos Table
- id (PK)
- title
- description
- thumbnail_url
- video_url
- category_id (FK)
- is_premium
- duration
- views
- created_at

### Subscriptions Table
- id (PK)
- user_id (FK)
- plan_name (Weekly/Monthly/Premium)
- amount (KES)
- start_date
- end_date
- status (active/expired)
- created_at

### Payments Table
- id (PK)
- user_id (FK)
- amount
- mpesa_receipt
- phone_number
- status (pending/completed/failed)
- created_at

---

## 🎨 Frontend Page Structure (Next.js)

```
app/
├── layout.tsx              # Root layout
├── page.tsx                # Homepage
├── login/
│   └── page.tsx           # Login page
├── register/
│   └── page.tsx           # Registration page
├── videos/
│   ├── page.tsx           # Videos list
│   └── [id]/
│       └── page.tsx       # Video detail
├── dashboard/
│   ├── page.tsx           # User dashboard
│   ├── watchlist/
│   │   └── page.tsx
│   └── subscription/
│       └── page.tsx
├── admin/
│   ├── layout.tsx         # Admin layout
│   ├── upload/
│   │   └── page.tsx       # Video upload
│   ├── users/
│   │   └── page.tsx
│   └── analytics/
│       └── page.tsx
```

---

## 🔗 API Endpoints (To Implement)

### Authentication
```
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/logout/
POST /api/auth/password-reset/
```

### Videos
```
GET /api/videos/
GET /api/videos/<id>/
POST /api/videos/upload/
GET /api/categories/
```

### Subscriptions
```
GET /api/subscriptions/plans/
POST /api/subscriptions/subscribe/
GET /api/subscriptions/user/
```

### Payments (M-Pesa)
```
POST /api/payments/mpesa/stkpush/
POST /api/payments/callback/
```

### Watch History
```
POST /api/watchhistory/
GET /api/watchhistory/user/
```

---

## ⚠️ Important: Before You Start

1. **PostgreSQL Setup** - Ensure PostgreSQL is running and you've created the database
2. **Environment Variables** - Create `.env` file with your configuration
3. **Virtual Environment** - Always activate `backend_env` before running Django commands
4. **M-Pesa Integration** - Get API credentials from Safaricom Daraja

---

## 📚 Learning Resources

- Django Docs: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- Next.js Docs: https://nextjs.org/docs
- PostgreSQL: https://www.postgresql.org/docs/
- Tailwind CSS: https://tailwindcss.com/docs

---

## 🆘 Troubleshooting

### Virtual Environment Issues
```bash
# Recreate virtual environment if needed
python -m venv backend_env
backend_env\Scripts\activate.bat
pip install -r requirements.txt
```

### Database Connection Issues
- Ensure PostgreSQL service is running
- Check credentials in `.env`
- Verify database exists: `createdb streaming_platform_db`

### Port Already in Use
```bash
# Change Django port
python manage.py runserver 8001

# Change Next.js port
npm run dev -- -p 3001
```

---

**You're all set! Start building your Kenyan streaming platform! 🚀**
