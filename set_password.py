from users.models import CustomUser

# Set admin password
try:
    u = CustomUser.objects.get(username='admin')
    u.set_password('admin123')
    u.save()
    print("Admin password set successfully")
except CustomUser.DoesNotExist:
    print("Admin user not found")