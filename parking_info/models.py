from django.db import models
import hashlib
# Create your models here.
class ParkingInformation(models.Model):
    ETD = models.DateTimeField(auto_now=False, auto_now_add=False, editable=True, null=True, blank=True)
    contracts = models.CharField(default='', null=False, blank=True, max_length=16)
    car_number = models.CharField(default='', null=False, blank=True, max_length=10)
    key = models.CharField(default='', null=False, blank=True, max_length=64)

    def get_set_key(self):
        car_number = self.car_number
        key = hashlib.sha256(car_number.encode()).hexdigest()
        self.key = key
        self.save()
