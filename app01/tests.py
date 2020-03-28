from django.test import TestCase

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BMS.settings")# project_name 项目名称
django.setup()

# Create your tests here.
from app01.models import *
from app01.forms import BookForm
# for i in range(1,500):
#     Book.objects.create(title="book%s"%i,pub_date="2020-03-16 00:00:00.000000",price=100,publish_id=1)


from app01 import models
# kant_id = models.Kanter.objects.filter(name="张可可").first()
# company_obj = models.Company.objects.filter(kans__name="张可可").values_list()
# print(company_obj)

# company_obj = models.Company.objects.filter(title="管理部")
# print(company_obj)
# for i in company_obj:
#     print(i.title)

# company_obj = models.Company.objects.filter(kprice_end__in=5)

a = '2020-05'

# print(a.split('-')[1].split('0')[1])

# year = a.split('-')[0]
# print(year)
#
# month = a.split('-')[1]
# print(month)
# if month.startswith('0'):
#     print(month.split('0')[1])
# else:
#     print(month)
#
# a = models.ComDepart.objects.all()
# print(a)

company_obj = models.Company.objects.filter(nid=1).first()
print(company_obj.title)