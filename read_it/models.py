from django.db import models
from users.models import Profile

class Book(models.Model):
    title = models.CharField(max_length=100)
    GENRE_CHOICES = [
        ('childrens','childrens'),('classics','classics'),('business','business'),
        ('fantasy','fantasy'),('history','history'),('horror','horror'),('mystery','mystery'),
        ('nonfiction','nonfiction'),('romance','romance'),('sports','sports'),('science','science'),
        ('young Adult','youngadult')
    ]
    genre = models.CharField(max_length=11,choices=GENRE_CHOICES)
    author = models.CharField(max_length=100)
    cover_image_link = models.CharField(max_length=100)
    number_of_pages = models.IntegerField(null=True,default=True)
    audible_link = models.CharField(max_length=100)
    barnes_noble_link = models.CharField(max_length=100)
    amazon_link = models.CharField(max_length=100)
    google_link = models.CharField(max_length=100)
    rating = models.DecimalField(null=True,default=3.0,max_digits=3, decimal_places=2)
    synopsis = models.TextField()
    likes = models.ManyToManyField(Profile)

    def __str__(self):
        return self.title
