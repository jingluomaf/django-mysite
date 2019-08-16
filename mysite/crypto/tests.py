from django.test import TestCase
import datetime
# Create your tests here.
s = '10 jun 2016'
print(datetime.strptime(s, "%d %b %Y").date())
