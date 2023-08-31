from django.db import models
# Create your models here.


class Dish(models.Model):
    name = models.TextField()
    quantity = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
