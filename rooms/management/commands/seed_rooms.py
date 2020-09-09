import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This commands create many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_user = user_models.User.objects.all()
        seeder.add_entity(room_models.Room, number,{
            "host": lambda x: random.choice(all_user)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created"))
