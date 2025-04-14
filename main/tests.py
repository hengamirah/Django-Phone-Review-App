
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Review, Brand, Model
User = get_user_model()
class MainViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.brand = Brand.objects.create(name='BrandA', origin='CountryA', manufacturing_since=2000)
        self.model = Model.objects.create(brand=self.brand, name='ModelA', launch_date='2023-01-01', platform='PlatformA')
        self.review = Review.objects.create(review_article='Great phone!', date_published='2023-01-01')
        self.review.models.add(self.model)
    def test_homepage_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the main page for Phone Radar website")
    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword'
        })
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='newuser').username, 'newuser')
    def test_user_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
    def test_add_review(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_review'), {
            'review_article': 'Amazing phone!',
            'date_published': '2023-01-02',
            'models': [self.model.id]
        })
        self.assertEqual(response.status_code, 302)  # Redirect after adding review
        self.assertEqual(Review.objects.count(), 2)  # Check if review count increased
    def test_add_phone_model(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_model'), {
            'brand': self.brand.id,
            'name': 'ModelB',
            'launch_date': '2023-02-01',
            'platform': 'PlatformB'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after adding model
        self.assertEqual(Model.objects.count(), 2)  # Check if model count increased