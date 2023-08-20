import sqlite3
import flask

conn = sqlite3.connect('Cookie.db')
c = conn.cursor()

conn.close()