from dish import Dish

dish_1 = Dish('Pasta Carbanara')
r = dish_1.get_all()
print("======")
print(r)

dish_1.insert_dish('salt', '2', 2)
t = dish_1.get_all()
print('======')
print('INSERT')
print("======")
print(t)

dish_1.update_dish('red pepper', 9)
y = dish_1.get_all()
print('======')
print('UPDATE')
print("======")
print(y)

dish_1.delete_dish(7)
u = dish_1.get_all()
print('======')
print("DELETE")
print("======")
print(u)

dish_1.end()
