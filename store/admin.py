from django.contrib import admin

from .models import Category, Animal

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Animal)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'animal_name', 'age', 'created_by', 'slug', 'price', 'created', 'updated', 'is_active']
    list_filter = ['category', 'is_active', 'fur_pattern', 'fur_color', 'fur_length', 'sex', 'location']
    list_editable = ['price', 'is_active']
    prepopulated_fields = {'slug': ('animal_name',)}
