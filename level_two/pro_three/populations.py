import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pro_three.settings")

import django
django.setup()

from first_app.models import UserDetail
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_age = fakegen.random_number(digits=2)
        fake_address = fakegen.address()
        fake_email = fakegen.email()

        usr_dtl = UserDetail.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, 
                                                    age=fake_age, address=fake_address, email=fake_email)[0]

if __name__ == "__main__":
    populate(10)




