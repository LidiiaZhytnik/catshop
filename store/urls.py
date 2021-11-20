from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_animals, name='all_animals'),
]
