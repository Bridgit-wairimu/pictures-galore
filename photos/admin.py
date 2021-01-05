from django.contrib import admin
from .models import Category,Location,Image

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal =('image',)

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)