from django.db import models

class BookNumber( models.Model ) :
    isbn = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=13)

    def __str__(self):
        if len( self.isbn ) > 0 :
            return self.isbn
        elif len( self.isbn13 ) > 0 :
            return self.isbn13
        else :
            return self


class Book( models.Model ) :
    title = models.CharField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=250, blank=True)
    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE )

    def __str__(self):
        return self.title


class BookCharacters( models.Model ) :
    name = models.CharField(max_length=50)
    book = models.ForeignKey(Book, related_name="characters", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Authers( models.Model ) :
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name="authers" )

    def __str__(self):
        return self.firstname + " " + self.lastname
