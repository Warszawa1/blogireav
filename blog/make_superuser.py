from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Makes the specified user a superuser'

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username='ireav')
            user.is_staff = True
            user.is_superuser = True
            user.save()
            print(f"User 'ireav' is now a superuser and staff member.")
        except User.DoesNotExist:
            print(f"User 'ireav' does not exist.")