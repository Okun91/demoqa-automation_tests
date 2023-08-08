import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')


def generator_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(15, 40),
        department=faker_ru.job(),
        email=faker_ru.email(),
        salary=random.randint(1000, 10000),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )


def generated_file():
    path = rf'C:\Users\umber\PycharmProjects\demoqa-automation_tests\filetest{random.randint(1, 20)}.txt'
    with open(path, 'w+') as file:
        file.write(f'Hello World {random.randint(1, 20)}')
    return file.name, path
