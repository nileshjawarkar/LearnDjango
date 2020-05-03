from django.db import models

class Book( models.Model ) :
    title = models.CharField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.title


