from django.core.management.base import BaseCommand
from django_seed import Seed
from accounts.models import User

class Command(BaseCommand):
    help = '유저 생성'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=1, type=int, help='How many users do you want to create?'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        user_seeder = Seed.seeder()
        user_seeder.add_entity(User, number, {
            'is_staff': False,
            'is_superuser': False,
            "username": lambda x: user_seeder.faker.name(),
            "email": lambda x: user_seeder.faker.email(),
        })
        user_seeder.execute()