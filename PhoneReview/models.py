from django.db import models
from django.contrib.auth.models import User
"""
    ### **Explanation of the Schema**
    1. **Brand (`Brand`):** Stores information about phone brands such as name, country of origin, and manufacturing year.
    2. **Model (`Model`):** Stores details about specific models of phones, linked to a brand (one brand can have multiple models) and includes launch date and platform information.
    3. **Review (`Review`):** Stores detailed reviews of phones, including the review's content and publication date. Each review can relate to multiple models (many-to-many relationship).

"""

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    origin = models.CharField(max_length=200)
    manufacturing_since = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    launch_date = models.DateField()
    platform = models.CharField(max_length=100)
    image = models.ImageField(upload_to='phones/', null=True, blank=True)  # Add image field
    def __str__(self):
        return f"{self.brand.name} {self.name}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Add user field
    review_article = models.TextField()
    date_published = models.DateField()
    models = models.ManyToManyField(Model)

    def __str__(self):
        username = self.user.username if self.user else "Anonymous"
        return f"Review by {username} on {self.date_published}"