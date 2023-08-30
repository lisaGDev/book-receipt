from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('dish', views.dish, name='dish'),
    path('get_dish_by_id/<int:id>', views.get_dish_by_id, name='get_dish_by_id'),
    path('add_dish', views.add_dish),
    path('testing', views.testing, name='testing')
]
