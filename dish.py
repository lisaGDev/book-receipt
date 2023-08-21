import sqlite3
import flask


class Dish:
    def __init__(self, dish_name):
        """Initialize db class variables"""
        self.connection = sqlite3.connect("Cookie.db")
        self.cur = self.connection.cursor()
        self.dish_name = dish_name

    def get_all(self):
        """get_all - displays all recipes in the table."""
        res = self.cur.execute("SELECT * FROM Dish")
        return res.fetchall()

    def insert_dish(self, name, quantity, price):
        """insert_dish – adds a recipe to the table."""
        self.cur.execute("INSERT INTO Dish (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
        self.connection.commit()  # Remember to commit the transaction after executing INSERT.

    def update_dish(self, price, id_dish):
        """update_dish – updates the price of a dish by name."""
        self.cur.execute("UPDATE Dish SET price = (?) WHERE id_dish = (?)", (price, id_dish))
        self.connection.commit()

    def delete_dish(self, id_dish):
        """delete_dish – deletes the recipe from the database by ID."""
        sql_delete_query = "DELETE FROM Dish WHERE id_dish = %s" % id_dish
        self.cur.execute(sql_delete_query)
        self.connection.commit()  # Remember to commit the transaction after executing DELETE.

    def end(self):
        """close sqlite3 connection."""
        self.connection.commit()
        self.connection.close()
