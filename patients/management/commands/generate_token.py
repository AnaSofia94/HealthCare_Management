from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Generate a token for a given user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user')

    def handle(self, *args, **kwargs):
        username = kwargs['username']

        try:
            user = User.objects.get(username=username)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                self.stdout.write(f"Token created for user {username}: {token.key}")
            else:
                self.stdout.write(f"Token already exists for user {username}: {token.key}")
        except User.DoesNotExist:
            self.stderr.write(f"Error: User with username '{username}' does not exist")