from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'iantelovazquez@gmail.com', 'borntowin1')
        print("Superuser created successfully.")
    else:
        print("Superuser already exists.")

if __name__ == "__main__":
    create_superuser()