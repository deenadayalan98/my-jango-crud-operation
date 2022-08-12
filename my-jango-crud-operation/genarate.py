import os
os.environ.setdefault('DJANGO_SETTINGS-MODULE','myapp.settings')
import django
django.setup()

from myapp.models import *
from faker import faker
from random import *
faker = faker()

def genarate(n):
    for i in range(n):
        fsno = randint(1001,1050)
        fsname = faker.name()
        fsclass = randint(1,8)
        fsaddress = faker.city()
        stud_record = Student.objects.get_or_create(sno=fsno, sname=fsname,sclass=fsclass,saddress=fsaddress )
    
genarate(10 )