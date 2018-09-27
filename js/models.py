from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.name
