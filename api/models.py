from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("kids", "Kids"),
        ("mens", "Mens"),
        ("electronics", "Electronics"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="mens")
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title