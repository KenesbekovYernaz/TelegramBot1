import sqlite3
import json

class DataBase:
	def __init__(self, connection):
		self.connection = connection

		with sqlite3.connect(connection) as db:
			cursor = db.cursor()

			cursor.execute("""CREATE TABLE IF NOT EXISTS users(
				user_id INTEGER PRIMARY KEY, 
				first_name VARCHAR, 
				username VARCHAR
			)""")

	def get_user(self, user_id):
		with sqlite3.connect(self.connection) as db:
			cursor = db.cursor()

			cursor.execute("SELECT user_id FROM users WHERE user_id = ?", [user_id])
			if cursor.fetchone() == None:
				return 0
			elif cursor.fetchone() != None:
				return 1


	def add_user(self, user_id, first_name, username):
		with sqlite3.connect(self.connection) as db:
			cursor = db.cursor()

			cursor.execute("INSERT INTO users(user_id, first_name, username) VALUES(?, ?, ?)", [user_id, first_name, username])
			

	def get_users(self, filename):
		with sqlite3.connect(self.connection) as db:
			cursor = db.cursor()

			file_json = open(filename, "w", encoding="utf-8")

			for name, id_, usern in cursor.execute("SELECT first_name, user_id, username FROM users"):

				data = {"user": {"first_name": name, "username": usern,"ID": id_}}


				json.dump(data, file_json, indent=2)

			file_json.close()
			