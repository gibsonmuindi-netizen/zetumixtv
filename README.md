# ZETUMIX
A Streaming platform for Kenyan/African Entertainment content to the world

## Overview
ZETUMIX is a full-stack Kenyan streaming platform built with Django and Next.js. It includes:

- User registration, login, and token-based authentication
- Video management and categories
- Subscription plans and payment processing
- Watch history tracking
- Backend API with Django REST Framework
- Frontend UI with Next.js, TypeScript, and Tailwind CSS

## Docs Included
- `DEPLOYMENT_GUIDE.md` — Deployment and production setup
- `SETUP_GUIDE.md` — Local installation and configuration
- `QUICKSTART.md` — Developer workflow and commands
- `EXAMPLE_MODELS.md` — Sample Django model implementations

## Run Locally
### Backend
```powershell
cd "C:\Users\Hp\Desktop\G\Microsoft VS Code\streaming-platform"
.\backend_env\Scripts\activate.ps1
python manage.py runserver
```

### Frontend
```powershell
cd "C:\Users\Hp\Desktop\G\Microsoft VS Code\streaming-platform\frontend"
npm install
npm run dev
```

## Key Features
- Authentication and user profiles
- Video library with categories
- Subscription plan management
- Payment and watch history endpoints
- Admin interface for content management

## Tech Stack
**Backend:** Django 6.0.5, Django REST Framework, Django CORS Headers, Gunicorn

**Frontend:** Next.js 16.2.5, React 19.2.4, TypeScript, Tailwind CSS

## Notes
- The project root contains `manage.py` and `requirements.txt`
- Use `.env` for environment variables in production
- `Root Directory` on Render should be `.` or left blank

## Ready for Deployment
Your ZETUMIX codebase is now synchronized and ready to push. Once the branch is clean, deploy to Render using the repo root.

Happy coding! 🚀
