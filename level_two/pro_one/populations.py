import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pro_one.settings")

import django
django.setup()

import random
from app_one.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ["Social","Games","Entertainment","News"]

def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    
    for entry in range(N):
        top = add_topics()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        wbpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        accrec = AccessRecord.objects.get_or_create(name=wbpg,  date=fake_date)[0] 

if __name__ == "__main__":
    print("populating the script")
    populate(10)
    print("population completed")
