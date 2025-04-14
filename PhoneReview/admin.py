from django.contrib import admin
from .models import Brand, Model, Review

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin', 'manufacturing_since')
    search_fields = ('name',)
    list_filter = ('origin', 'manufacturing_since')

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'launch_date', 'platform')
    search_fields = ('name', 'platform')
    list_filter = ('brand', 'launch_date')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('get_reviewer', 'date_published')
    search_fields = ('review_article',)
    list_filter = ('date_published', 'user')
    filter_horizontal = ('models',)  # Easier editing for many-to-many fields
    
    def get_reviewer(self, obj):
        return obj.user.username if obj.user else "Anonymous"
    get_reviewer.short_description = 'Reviewer'

"""### **Key Features in the Admin Panel**
#### 1. **`list_display`:**
- Displays specific fields in the list view of each model in the admin panel for ease of managing data.
- Example: For `Brand`, users will see the `name`, `origin`, and `manufacturing_since` fields listed.

#### 2. **`search_fields`:**
- Adds a search bar to make it easier for admins to find entries.
- Example: For `Model`, users can search by `name` or `platform`.

#### 3. **`list_filter`:**
- Adds filtering options in the admin interface.
- Example: For `Brand`, admins can filter brands by `origin` or `manufacturing_since`.

#### 4. **`filter_horizontal`:**
- Specifically for the many-to-many relationship in the `Review` model, this makes it easier to associate multiple models with a single review by showing a horizontal multi-select widget.
"""
