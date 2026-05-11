# 🚀 Quick Start Guide

## Open in VS Code

```bash
code .
```

Or open VS Code and navigate to: `c:\Users\Hp\Desktop\G\Microsoft VS Code\streaming-platform`

---

## One-Time Database Setup

### 1. Create PostgreSQL Database

Open PostgreSQL terminal or run:

```sql
CREATE DATABASE streaming_platform_db;
```

### 2. Update Django Settings

Edit `streaming_platform/settings.py` - Update the DATABASES section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'streaming_platform_db',
        'USER': 'postgres',
        'PASSWORD': 'your_postgres_password',  # ← Change this
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. Create .env File

Create `.env` in the project root:

```env
DEBUG=True
SECRET_KEY=django-insecure-YOUR-SECRET-KEY-HERE
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/streaming_platform_db
MPESA_CONSUMER_KEY=your_key_here
MPESA_CONSUMER_SECRET=your_secret_here
```

### 4. Run Migrations

```bash
# Activate virtual environment
backend_env\Scripts\activate.bat

# Install CORS package
pip install django-cors-headers

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
```

### 5. Install Frontend Dependencies

```bash
cd frontend
npm install
```

---

## Development Workflow

### Terminal 1 - Start Backend

```bash
backend_env\Scripts\activate.bat
python manage.py runserver
```

✅ Backend: http://localhost:8000
📊 Admin: http://localhost:8000/admin

### Terminal 2 - Start Frontend

```bash
cd frontend
npm run dev
```

✅ Frontend: http://localhost:3000

---

## 📂 Where to Start Implementing

### Backend Models (Django)

1. **[users/models.py](users/models.py)** - User authentication
   ```python
   from django.contrib.auth.models import AbstractUser
   
   class CustomUser(AbstractUser):
       phone_number = models.CharField(max_length=15, unique=True)
       subscription_status = models.CharField(max_length=20, default='free')
   ```

2. **[videos/models.py](videos/models.py)** - Video management
   ```python
   class Category(models.Model):
       name = models.CharField(max_length=100)
   
   class Video(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()
       video_file = models.FileField(upload_to='videos/')
       category = models.ForeignKey(Category, on_delete=models.CASCADE)
       is_premium = models.BooleanField(default=False)
   ```

3. **[payments/models.py](payments/models.py)** - M-Pesa integration
4. **[subscriptions/models.py](subscriptions/models.py)** - Subscription plans
5. **[watchhistory/models.py](watchhistory/models.py)** - Watch tracking

### Frontend Pages (Next.js)

1. **[frontend/app/page.tsx](frontend/app/page.tsx)** - Homepage
2. **Create login/register pages** in `frontend/app/auth/`
3. **Create video listing** in `frontend/app/videos/`
4. **Create dashboard** in `frontend/app/dashboard/`

---

## API Endpoint Implementation Order

### Priority 1 (Authentication)
- [ ] User registration endpoint
- [ ] User login endpoint  
- [ ] JWT token generation
- [ ] Password reset

### Priority 2 (Videos)
- [ ] List videos with pagination
- [ ] Get video details
- [ ] Video upload (admin)
- [ ] Video streaming

### Priority 3 (Payments)
- [ ] M-Pesa STK push
- [ ] Payment callback handler
- [ ] Payment history

### Priority 4 (Subscriptions)
- [ ] List subscription plans
- [ ] Subscribe to plan
- [ ] Check subscription status

---

## Useful Commands

```bash
# Create new Django app
python manage.py startapp appname

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Shell (interactive Python with Django context)
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic

# Run tests
python manage.py test

# Flush database (CAREFUL - deletes all data)
python manage.py flush
```

---

## Frontend Commands

```bash
# Install dependencies
npm install

# Development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Run linter
npm run lint
```

---

## 🔍 File Structure Reference

```
streaming-platform/
├── manage.py                    # Django CLI
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (create this)
├── .gitignore                   # Git ignore rules
│
├── streaming_platform/          # Main Django config
│   ├── settings.py             # ← Update database config here
│   ├── urls.py                 # ← Add app routes here
│   ├── asgi.py
│   └── wsgi.py
│
├── users/                       # User management app
│   ├── models.py               # ← Define User model here
│   ├── views.py                # ← Create API views
│   ├── serializers.py          # ← Create (new file)
│   ├── urls.py                 # ← Create (new file)
│   └── admin.py
│
├── videos/                      # Video management app
│   ├── models.py               # ← Define Video models
│   ├── views.py
│   ├── serializers.py          # ← Create (new file)
│   ├── urls.py                 # ← Create (new file)
│   └── admin.py
│
├── payments/                    # M-Pesa integration
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── subscriptions/               # Subscription management
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── watchhistory/                # Watch tracking
│   ├── models.py
│   └── views.py
│
└── frontend/                    # Next.js frontend
    ├── app/
    │   ├── layout.tsx          # Root layout
    │   ├── page.tsx            # Homepage
    │   ├── login/
    │   ├── register/
    │   ├── videos/
    │   ├── dashboard/
    │   └── admin/
    ├── components/             # React components
    ├── public/                 # Static files
    ├── package.json
    └── tsconfig.json
```

---

## 🎯 Your First Task

Start here if you don't know what to do next:

1. **Create the User model** in `users/models.py`
2. **Create serializers.py** in users app
3. **Create API views** for registration and login in `users/views.py`
4. **Create urls.py** in users app with auth endpoints
5. **Add users app to Django settings**
6. **Run migrations**
7. **Test in Django admin** at http://localhost:8000/admin

---

## 🆘 Getting Help

Check SETUP_GUIDE.md for more detailed information on each component.

**Happy coding! 🎉**
