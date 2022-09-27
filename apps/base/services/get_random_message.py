from faker import Faker

faker = Faker()


def get_random_message():
    return f"Hi, I am {faker.first_name()}"
