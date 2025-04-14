# from django.db import models
# from django.template.defaultfilters import slugify
# # Create your models here.


# from django.contrib.auth.models import User
# from PhoneReview.models import Model  # Import Model from PhoneReview app

# class PhoneReview(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     review_article = models.TextField()
#     date_published = models.DateField(auto_now_add=True)
#     models = models.ManyToManyField(Model)

#     def __str__(self):
#         return f"Review by {self.user.username} on {self.date_published}"
