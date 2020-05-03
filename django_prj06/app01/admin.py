from django.contrib import admin
from . import models

admin.site.register( models.Book )
admin.site.register( models.BookNumber )
admin.site.register( models.BookCharacters )
admin.site.register( models.Authers )

