import os
import random
import faker

from django.core.management.base import BaseCommand
from django_seed import Seed
from movies.models import Movie, Review

class Command(BaseCommand):
    help = "movie 당 reviews 10개 생성"
    
    def handle(self, *args, **options):
        movies = Movie.objects.all()

        for movie in movies:
            review_seeder = Seed.seeder()
            review_seeder.add_entity(Review, 10, {
                'movie': movie,
            })
            review_seeder.execute()  # 실행하는 명령어