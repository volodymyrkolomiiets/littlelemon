from django.db import models

# Create your models here.
class BookingModel(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    number_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return self.name
    
    
class MenuModel(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.title
    
