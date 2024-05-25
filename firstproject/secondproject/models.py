from django.db import models
from django.utils import timezone
# Create your models here.
class NewData(models.Model):
    Heading_type = [
        ("home", 'code with samir'),
        ("about", 'about us'),
        ("contactus", 'conatact us'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='imagedata/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=20 , choices=Heading_type)

    def __str__(self):
        return self.name

