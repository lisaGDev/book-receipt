import sqlite3
# import flask


class Dish:
    def __init__(self, dish_name):
        """Initialize db class variables"""
        self.connection = sqlite3.connect("Cookie.db")
        self.cur = self.connection.cursor()
        self.dish_name = dish_name

    def get_all(self):
        """get_all - displays all recipes in the table."""
        res = self.cur.execute("SELECT * FROM dish")
        return res.fetchall()

    def insert_dish(self, name, quantity, price):
        """insert_dish – adds a recipe to the table."""
        self.cur.execute("INSERT INTO dish (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
        self.connection.commit()  # Remember to commit the transaction after executing INSERT.

    def update_dish(self, price, id_dish):
        """update_dish – updates the price of a dish by name."""
        self.cur.execute("UPDATE dish SET price = (?) WHERE id_dish = (?)", (price, id_dish))
        self.connection.commit()

    def delete_dish(self, id_dish):
        """delete_dish – deletes the recipe from the database by ID."""
        sql_delete_query = "DELETE FROM dish WHERE id_dish = %s" % id_dish
        self.cur.execute(sql_delete_query)
        self.connection.commit()  # Remember to commit the transaction after executing DELETE.

    def create_tuple_of_ingredients(self, dish_name):
        """get all the ingredients for the selected dish."""
        get_id_dish_by_name_res = self.cur.execute("SELECT id_dish FROM dish WHERE name = '%s'" % dish_name).fetchone()[0]
        get_composition_by_id_ingredient_res_tuple = tuple(i[0] for i in self.cur.execute("SELECT id_ingredients FROM Composition WHERE id_dish = %s" % get_id_dish_by_name_res).fetchall())

        return get_composition_by_id_ingredient_res_tuple

    def get_ingredients_by_dish(self, dish_name):
        get_composition_by_id_ingredient_res_tuple = self.create_tuple_of_ingredients(dish_name)
        get_ingredients_by_id_ingredient_res = self.cur.execute("SELECT * FROM Ingredients WHERE Ingredients.id_ingredient IN %s" % str(get_composition_by_id_ingredient_res_tuple)).fetchall()

        return get_ingredients_by_id_ingredient_res

    def price_ingredients_for_dish(self, dish_name):
        """get the price of a dish according to its ID."""
        get_composition_by_id_ingredient_res_tuple = self.create_tuple_of_ingredients(dish_name)
        get_price_by_dish = self.cur.execute("SELECT SUM(Ingredients.price) FROM Ingredients WHERE Ingredients.id_ingredient IN %s" % str(get_composition_by_id_ingredient_res_tuple)).fetchone()[0]

        return get_price_by_dish

    def order_price(self):
        """Create a request to sort by the price of the dish."""
        res = self.cur.execute("SELECT name from dish ORDER BY price")
        return res.fetchall()

    def end(self):
        """close sqlite3 connection."""
        self.connection.commit()
        self.connection.close()
