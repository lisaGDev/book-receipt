from dish import Dish
from ingredients import Ingredients
import django

dish_1 = Dish('Pasta Carbanara')
ingredient_1 = Ingredients()

r = dish_1.get_all()
# print("===========")
# print("Recipe List")
# print("===========")
# print(r)
# print("===========")
# print("End List")
# print("===========")

# dish_1.insert_dish('fish', '3', 5)
# t = dish_1.get_all()
# print('======')
# print('INSERT')
# print("======")
# print(t)

# dish_1.update_dish(3, 13)
# y = dish_1.get_all()
# print('======')
# print('UPDATE')
# print("======")
# print(y)

# dish_1.delete_dish(13)
# u = dish_1.get_all()
# print('======')
# print("DELETE")
# print("======")
# print(u)

o = ingredient_1.get()
# print("===========")
# print("Ingredient List")
# print("===========")
# print(o)
# print("===========")
# print("End List")
# print("===========")

# ingredient_1.insert('pepper', 3, 6.55)
# i = ingredient_1.get()
# print("=================")
# print("Ingredient Insert")
# print("=================")
# print(i)
# print("===============")
# print("End Insert List")
# print("===============")

# ingredient_1.update(4.55, 1)
# p = ingredient_1.get()
# print('=================')
# print('UPDATE Ingredient')
# print("=================")
# print(p)
# print("===================")
# print("End Update Ingredient")
# print("===================")

# ingredient_1.delete(2)
# a = ingredient_1.get()
# print('=================')
# print("DELETE Ingredient")
# print("=================")
# print(a)
# print("===================")
# print("End Delete Ingredient")
# print("===================")

# q = dish_1.get_ingredients_by_dish('goat')
# print("===================")
# print("Ingredients By dish")
# print("===================")
# print(q)
# print("====================")
# print("End Ingredients dish")
# print("====================")

w = dish_1.price_ingredients_for_dish('goat')
print("=========================")
print("Price Ingredients By dish")
print("=========================")
print(w)
# print("==========================")
# print("Price End Ingredients dish")
# print("==========================")

e = dish_1.order_price()
print("===================")
print("Order Price")
print("===================")
print(e)
# print("====================")
# print("End O Price")
# print("====================")
