from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to="cars/", null=True, blank=True)

    def __str__(self):
        return self.brand + " " + self.model