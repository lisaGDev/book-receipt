import sqlite3
# import flask


class Ingredients:
    def __init__(self):
        """Initialize db class variables"""
        self.connection = sqlite3.connect("Cookie.db")
        self.cur = self.connection.cursor()

    def get(self):
        """get_all - displays all recipes in the table."""
        res = self.cur.execute("SELECT * FROM Ingredients")
        return res.fetchall()

    def insert(self, name, count, price):
        self.cur.execute("INSERT INTO Ingredients (name, count, price) VALUES (?, ?, ?)", (name, count, price))
        self.connection.commit()  # Remember to commit the transaction after executing INSERT.

    def update(self, price, id_ingredient):
        self.cur.execute("UPDATE Ingredients SET price = (?) WHERE id_ingredient = (?)", (price, id_ingredient))
        self.connection.commit()

    def delete(self, id_ingredient):
        sql_delete_query = "DELETE FROM Ingredients WHERE id_ingredient = %s" % id_ingredient
        self.cur.execute(sql_delete_query)
        self.connection.commit()  # Remember to commit the transaction after executing DELETE.
