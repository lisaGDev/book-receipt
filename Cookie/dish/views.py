from django.template import loader
from django.http import HttpResponse
from .models import Dish


def dish(request):
    dishes = Dish.objects.all().values()
    template = loader.get_template('all_dishes.html')
    context = {
        'dishes': dishes,
    }
    return HttpResponse(template.render(context, request))


def get_dish_by_id(request, id):
    dish_by_id = Dish.objects.get(id=id)
    template = loader.get_template('dish_by_id.html')
    context = {
        'dish_by_id': dish_by_id,
    }
    return HttpResponse(template.render(context, request))


def testing(request):
    dishdata = Dish.objects.all().order_by('name').values()
    template = loader.get_template('testing.html')
    context = {
        'dishdata': dishdata,
    }
    return HttpResponse(template.render(context, request))


def add_dish(request):
    name = request.POST['name']
    quantity = request.POST['quantity']
    price = request.POST['price']

    d = Dish(name=name, quantity=quantity, price=price)
    d.save()
    return dish(request)


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
