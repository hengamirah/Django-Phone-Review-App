from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Review
from .models import Model

def review_list(request):
    reviews = Review.objects.all()  # Fetch all reviews from the database
    return render(request, "PhoneReview/review_list.html", {"reviews": reviews})


@login_required
def add_review(request):
    models = Model.objects.all()  # Fetch all phone models
    if request.method == "POST":
        review_article = request.POST.get('review_article')
        models_selected = request.POST.getlist('models')  # List of selected model IDs
        review = Review.objects.create(
            user=request.user,  # Associate the review with the current user
            review_article=review_article,
            date_published=request.POST.get('date_published'),
        )
        review.models.set(models_selected)  # Associate the selected models
        review.save()
        return redirect('index')  # Redirect to homepage instead
    return render(request, "add_review.html", {"models": models})