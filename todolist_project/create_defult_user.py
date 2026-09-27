from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create default user'

    def handle(self, *args, **kwargs):
        username = 'admin'
        password = 'Admin@12345'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS('Default user created')
            )
        else:
            self.stdout.write(
                self.style.WARNING('User already exists')
            )