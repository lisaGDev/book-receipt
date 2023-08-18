from dish import Dish

dish_1 = Dish('Pasta Carbanara')
r = dish_1.get_all()
print('======')
print(r)

dish_1.insert_dish('cream','2',2)
t = dish_1.get_all()
print('======')
print(t)

dish_1.update_dish('cheese', 3)
y = dish_1.get_all()
print('======')
print(y)

dish_1.delete_dish(3)
u = dish_1.get_all()
print('======')
print(u)