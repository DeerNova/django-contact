from contacts.models import Contact
from faker import Faker
from faker.providers import internet, address


def fake_data():
  fake = Faker()
  fake.add_provider(internet)
  for i in range(100):
    Contact.objects.create(
      name = fake.name(),
      age = fake.random_int(min=15,max=60),
      email= fake.email(),
      phone = fake.phone_number()
    )

  
