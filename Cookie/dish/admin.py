from django.contrib import admin
from .models import Dish


# Register your models here.
class DishAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "quantity", "price",)


admin.site.register(Dish, DishAdmin)
