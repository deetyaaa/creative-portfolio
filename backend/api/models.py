from django.db import models

# Create your models here.
from django.db import models

CREATIVE_CHOICES = [
    ("photography", "Photography"),
    ("fashion", "Fashion Design"),
    ("cinema", "Cinematography"),
    ("music", "Music"),
    ("graphic", "Graphic Design"),
]

class Creator(models.Model):
    name           = models.CharField(max_length=80)
    profile_pic    = models.ImageField(upload_to="profiles/")
    bio            = models.TextField(blank=True)
    creative_fields= models.JSONField()         # list of strings
    portfolio_1    = models.URLField(blank=True)
    portfolio_2    = models.URLField(blank=True)
    portfolio_3    = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.name
