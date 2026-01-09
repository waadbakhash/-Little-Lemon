from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    booking_date = models.DateField()

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    inventory = models.IntegerField()

    def __str__(self):
        return self.title 
    def get_item(self):
        return f"{self.title} : {str(self.price)}"  