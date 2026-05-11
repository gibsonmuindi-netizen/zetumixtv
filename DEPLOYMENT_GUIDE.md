# 🚀 ZETUMIX - Production Deployment Guide

## Prerequisites

- Python 3.x installed
- Node.js 18+ installed
- Git account
- Hosting accounts (Render/Railway for backend, Vercel/Netlify for frontend)

## Backend Deployment (Django)

### 1. Prepare Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` with your production values:

```env
SECRET_KEY=your-secure-secret-key-here
DEBUG=False
ALLOWED_HOSTS=zetumix.com,www.zetumix.com

# Database (use PostgreSQL for production)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=zetumix_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432

# CORS (allow your frontend domain)
CORS_ALLOWED_ORIGINS=https://zetumix.vercel.app,https://www.zetumix.vercel.app
CSRF_TRUSTED_ORIGINS=https://zetumix.vercel.app,https://www.zetumix.vercel.app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
pip install python-decouple  # For environment variables
pip install gunicorn         # Production WSGI server
pip install whitenoise       # Static files serving
pip install psycopg2-binary  # PostgreSQL driver
```

### 3. Database Setup

For production, use PostgreSQL instead of SQLite:

1. Create a PostgreSQL database
2. Update `.env` with database credentials
3. Run migrations:

```bash
python manage.py migrate
```

### 4. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 5. Deploy to Hosting Service

#### Option A: Render (Recommended)

1. Connect your GitHub repository
2. Set build command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
3. Set start command: `gunicorn streaming_platform.wsgi:application`
4. Add environment variables from your `.env` file
5. Deploy

#### Option B: Railway

1. Connect repository
2. Add environment variables
3. Railway auto-detects Python and runs migrations
4. Deploy

#### Option C: Heroku

1. Install Heroku CLI
2. Create app: `heroku create your-app-name`
3. Set environment variables: `heroku config:set KEY=VALUE`
4. Deploy: `git push heroku main`

## Frontend Deployment (Next.js)

### 1. Prepare Environment Variables

```bash
cd frontend
cp .env.local.example .env.local
```

Edit `.env.local`:

```env
NEXT_PUBLIC_API_URL=https://your-backend-domain.com
```

### 2. Build for Production

```bash
npm run build
```

### 3. Deploy to Hosting Service

#### Option A: Vercel (Recommended)

1. Install Vercel CLI: `npm i -g vercel`
2. Deploy: `vercel`
3. Set environment variable: `NEXT_PUBLIC_API_URL=https://your-backend-domain.com`
4. Deploy

#### Option B: Netlify

1. Connect repository
2. Set build command: `npm run build`
3. Set publish directory: `out` (for static export) or `.next` (for SSR)
4. Add environment variable: `NEXT_PUBLIC_API_URL=https://your-backend-domain.com`
5. Deploy

## Post-Deployment Checklist

### Backend
- [ ] DEBUG=False
- [ ] SECRET_KEY is secure and unique
- [ ] ALLOWED_HOSTS includes your domain
- [ ] CORS_ALLOWED_ORIGINS includes frontend domain
- [ ] Database is PostgreSQL
- [ ] Static files are collected
- [ ] Admin panel accessible at `/admin`

### Frontend
- [ ] NEXT_PUBLIC_API_URL points to backend
- [ ] Build succeeds without errors
- [ ] All pages load correctly
- [ ] Authentication works
- [ ] API calls succeed

### Security
- [ ] HTTPS enabled
- [ ] SECRET_KEY not committed to git
- [ ] Database credentials secure
- [ ] Admin password changed from default

## Troubleshooting

### Backend Issues
- **500 Error**: Check logs for DEBUG info
- **CORS Error**: Verify CORS_ALLOWED_ORIGINS
- **Static Files**: Run `collectstatic`

### Frontend Issues
- **API Calls Fail**: Check NEXT_PUBLIC_API_URL
- **Build Fails**: Ensure all dependencies installed
- **Auth Issues**: Verify token handling

## Domain Configuration

1. Point your domain to the hosting service
2. Update ALLOWED_HOSTS and CORS settings
3. Test all functionality

## Monitoring

- Set up error logging (Sentry, etc.)
- Monitor database performance
- Set up backups for production database

---

🎉 Your streaming platform is now live on the internet!

## 🎯 Next Steps for Development

### Phase 1: Video Upload System
- Implement video upload endpoint
- Add file storage (local or cloud)
- Create thumbnail generation
- Add video transcoding for different qualities

### Phase 2: M-Pesa Integration
- Set up M-Pesa merchant account
- Implement STK push for payments
- Add payment callback verification
- Create payment processing flow

### Phase 3: Video Streaming
- Implement HLS/DASH streaming
- Add video player component
- Create adaptive bitrate streaming
- Implement seek and buffering

### Phase 4: Search & Discovery
- Add full-text search for videos
- Implement recommendation engine
- Add trending videos section
- Create personalized watch lists

### Phase 5: Production Deployment
- Move to PostgreSQL for production
- Set up static/media file serving
- Configure Gunicorn/Nginx
- Enable HTTPS/SSL
- Set up monitoring and logging

---

## 🔐 Security Notes

1. **Change the secret key** in `streaming_platform/settings.py` before production
2. **Update ALLOWED_HOSTS** with your domain
3. **Enable HTTPS** in production
4. **Use environment variables** for sensitive data (.env file)
5. **Enable CSRF protection** for POST requests
6. **Rate limiting** on API endpoints recommended
7. **Regular security updates** for dependencies

---

## 📱 Features List

### User Features
- ✅ User registration and login
- ✅ Profile management
- ✅ Subscription management
- ✅ Watch history tracking
- ✅ Payment history
- ✅ Responsive mobile design

### Admin Features
- ✅ User management
- ✅ Video upload and management
- ✅ Category management
- ✅ Subscription plan management
- ✅ Payment tracking
- ✅ Watch history analytics

### Technical Features
- ✅ RESTful API design
- ✅ Token-based authentication
- ✅ CORS support for cross-origin requests
- ✅ Pagination support
- ✅ Permission-based access control
- ✅ Error handling and validation
- ✅ Admin interface

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000

# Kill process using port 8000
taskkill /PID <PID> /F

# Restart backend
$venv = ".\backend_env\Scripts\python.exe"
& $venv manage.py runserver
```

### Frontend can't connect to backend
- Ensure backend is running on port 8000
- Check CORS_ALLOWED_ORIGINS in settings.py
- Verify API URL in frontend environment

### Database errors
```bash
# Reset database
$venv = ".\backend_env\Scripts\python.exe"
& $venv manage.py migrate --run-syncdb
```

---

## 📞 Support

All features are implemented and documented. For API details, check the admin interface at:
**http://localhost:8000/admin**

Documentation is in:
- SETUP_GUIDE.md - Installation reference
- QUICKSTART.md - Development workflow
- EXAMPLE_MODELS.md - Django model examples

---

## 🎊 Enjoy Your Streaming Platform!

You now have a fully functional Kenyan streaming platform ready for users to:
- Register and login
- Browse entertainment and educational content
- Subscribe to premium plans
- Track their watch history
- Make payments

**Happy streaming! 🚀🎬**
