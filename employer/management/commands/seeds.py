from django.core.management.base import BaseCommand
from employer.models import Employer
from django.utils import timezone
import random
import faker
import random


class Command(BaseCommand):
    help = 'Seed database with 50,000 records'

    def handle(self, *args, **kwargs):
        Employer.objects.all().delete()
        # # Создание 50,000 записей
        # fake = faker.Faker('ru_RU')  # Создание экземпляра Faker для русского языка
        # for _ in range(50000):
        #     # Генерация данных для каждой записи
        #
        #     date_employment = fake.date_between(start_date='-10y',
        #                                         end_date='today')  # Случайная дата за последние 10 лет
        #
        #     # Создание записи в базе данных
        #     Employer.objects.create(
        #         f_name=fake.first_name(),
        #         m_name=fake.last_name(),
        #         l_name=fake.middle_name(),
        #         position=fake.job(),
        #         date_employment=date_employment,
        #         salary=random.randint(20000, 200000),
        #         parent_id=random.randint(50007, 50010)
        #
        #     )
