import os
import random

from django.core.management.base import BaseCommand
from django_seed import Seed
from movies.models import Movie, Review
from accounts.models import User

class Command(BaseCommand):
    help = "테스트 리뷰 생성"
    
    def add_arguments(self, parser): 
        parser.add_argument( 
            '--number', default=2, type=int, help="몇 개의 리뷰를 만드나") 
            
    def handle(self, *args, **options): 
        number = options.get('number') 
        seeder = Seed.seeder()
        # fake = Faker('ko_KR')

        users = User.objects.all()
        movies = Movie.objects.all()

        seeder.add_entity(Review, number, {
            "content": lambda x: seeder.faker.paragraph(nb_sentences=1),
            "rating": lambda x: random.randint(1, 5),
            "created_at": lambda x:  seeder.faker.date(),
            "updated_at": lambda x:  seeder.faker.date(),
            "user": lambda x:  random.choice(users),
            "movie": lambda x:  random.choice(movies),
        })

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number}개의 리뷰가 작성되었습니다."))