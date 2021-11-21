from django.urls import path
from . import views
from .views import CreateAnimal, DeleteAnimal, UpdateAnimal

app_name = 'store'

urlpatterns = [
    path('', views.all_animals, name='all_animals'),
    path('item/<slug:slug>/', views.animal_detail, name='animal_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    path('create/animal', CreateAnimal.as_view(),  name='create_animal'),
    path('delete/<slug:slug>/', DeleteAnimal.as_view(),  name='delete_animal'),
    path('update/<slug:slug>/', UpdateAnimal.as_view(),  name='update_animal'),
    ]