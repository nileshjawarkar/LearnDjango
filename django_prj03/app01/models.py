from django.db import models

class Building( models.Model ) :
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) :
        return self.name

class Flat( models.Model ) :
    building = models.ForeignKey(Building, on_delete=models.CASCADE )
    no = models.IntegerField()
    owner = models.CharField(max_length=150)

    def __str__(self) :
        return self.building.name + str(self.no)

