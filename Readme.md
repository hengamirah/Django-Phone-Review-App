Phone Radar App
A comprehensive mobile phone review platform built with Django that allows users to explore phone models, read reviews, and contribute their own reviews and phone information.

# 📱 Features
Browse Phones: Explore a catalog of smartphones organized by brand, with details like launch date and platform
Read Reviews: See what other users think about various phone models
User Authentication: Register, login, and maintain your profile
Add Phone Models: Contribute new phones to the database with detailed information
Add Brands: Create new brands if they don't exist in the system
Write Reviews: Share your experience with specific phone models
Responsive Design: Enjoy a consistent experience across different devices

# 🛠️ Technologies Used
Backend: Django 5.x
Database: SQLite (default)
Frontend: HTML, CSS, JavaScript
Authentication: Django's built-in authentication system
Media Handling: Django's media management

# 📦 Installation
Clone the repository

# 📋 Usage
For Users
Register an account to access all features
Browse phones to see specifications and reviews
Read reviews from other users about phone models
Write reviews to share your experience with specific models
Add new phones to contribute to the database
For Administrators
Access the admin panel at http://127.0.0.1:8000/admin/
Manage users, brands, phone models, and reviews
Moderate content and maintain the platform

# 🗂️ Project Structure

phoneradar/
├── main/                  # Main app with core functionality
│   ├── views.py           # Core views (homepage, add_phone, add_review)
│   ├── urls.py            # URL patterns for main app
│   └── models.py          # Data models
├── PhoneReview/           # App for review functionality
│   ├── views.py           # Views for reviews
│   ├── urls.py            # URL patterns for review app
│   └── models.py          # Data models (Brand, Model, Review)
├── templates/             # HTML templates
│   ├── index.html         # Homepage template
│   ├── explore_phones.html # Phone listing template
│   ├── reviews.html       # Reviews listing template
│   ├── add_phone.html     # Form to add a new phone
│   ├── add_review.html    # Form to add a new review
│   └── registration/      # Authentication templates
│       ├── login.html     # Login form
│       ├── register.html  # Registration form
│       └── logout.html    # Logout confirmation
├── static/                # Static files (CSS, JS, images)
│   └── css/               # CSS stylesheets
│       └── styles.css     # Main stylesheet
├── media/                 # User-uploaded content
│   └── phones/            # Phone images
├── phoneradar/            # Project settings
│   ├── settings.py        # Django configuration
│   ├── urls.py            # Project-level URL configuration
│   └── wsgi.py            # WSGI configuration
└── manage.py              # Django management script


# 🔧 Additional Configuration
Media Files
For production, configure proper storage for media files:
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

📧 Contact
For any questions or feedback, please reach out to hengamirah@gmail.com
