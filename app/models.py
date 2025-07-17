from django.db import models

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Car(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.FloatField()
    image = models.ImageField(upload_to='cars')
    year = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
