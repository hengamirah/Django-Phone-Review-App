from http.client import HTTPResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from PhoneReview.models import Review, Model, Brand
# Create your views here.

def index(request):
    reviews = Review.objects.all()
    latest_phones = Model.objects.all().order_by('-launch_date')[:3]
    return render(request, "index.html", {"reviews": reviews,
        "latest_phones": latest_phones})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def add_review(request):
    if request.method == "POST":
        review_article = request.POST.get('review_article')
        models_selected = request.POST.getlist('models')  # Assuming models are passed as a list of IDs
        review = Review.objects.create(
            user =request.user,  # Associate the review with the current user
            review_article=review_article,
            date_published=request.POST.get('date_published'),
        )
        review.models.set(models_selected)  # Associate the selected models
        review.save()
        return redirect('index')  # Redirect to the review list after adding
    models = Model.objects.all()  # Query all phone models
    return render(request, "add_review.html", {"models": models})  # Render the add review form

@login_required
def add_phone(request):
    brands = Brand.objects.all()
    if request.method == "POST":
        # Check if we're creating a new brand
        if 'new_brand_name' in request.POST and request.POST.get('new_brand_name'):
            # Create new brand first
            brand_name = request.POST.get('new_brand_name')
            brand_origin = request.POST.get('brand_origin')
            manufacturing_since = request.POST.get('manufacturing_since')
            
            # Create the brand
            brand = Brand.objects.create(
                name=brand_name,
                origin=brand_origin,
                manufacturing_since=manufacturing_since
            )
            brand_id = brand.id
        else:
            # Use existing brand
            brand_id = request.POST.get('brand')

        name = request.POST.get('name')
        launch_date = request.POST.get('launch_date')
        platform = request.POST.get('platform')
        
        Model.objects.create(
            brand_id=brand_id,
            name=name,
            launch_date=launch_date,
            platform=platform
        )
        return redirect('index')
    return render(request, "add_phone.html", {"brands": brands})
# Add this new function
def reviews_page(request):
    reviews = Review.objects.all().order_by('-date_published')
    return render(request, "reviews.html", {"reviews": reviews})

# Add this function to your views.py
from django.contrib.auth import logout
# Add this to your views.py if it's not already there
def explore_phones(request):
    phones = Model.objects.all().order_by('-launch_date')
    return render(request, "explore_phones.html", {"phones": phones})
def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')  # Use your logout.html template``