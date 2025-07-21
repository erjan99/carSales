from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.IntegerField()
    image = models.ImageField()
    description = models.TextField()
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name
