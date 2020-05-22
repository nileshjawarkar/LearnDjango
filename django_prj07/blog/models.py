from django.db import models
from django.utils import timezone

class Post( models.Model ) :
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE )
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateField( timezone.now() )
    published_date = models.DateField(null=True, blank=True)

    def publish( self ) :
        self.published_date = timezone.now()
        self.save()

    def get_approved_comments( self ) :
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title


class Comment( models.Model ) :
    post = models.ForeignKey("blog.Post" , on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateField(timezone.now())
    approved_comment = models.BooleanField(False)

    def approve( self ) :
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text
