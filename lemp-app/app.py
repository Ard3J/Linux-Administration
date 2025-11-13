from flask import Flask
import mysql.connector

app = Flask(__name__)
@app.route('/')

def home():
	conn = mysql.connector.connect(
		host="localhost",
		user="exampleuser",
		password="Salas4n@",
		database="exampledb"
	)
	cursor = conn.cursor()
	cursor.execute("SELECT 'Hello from MySQL'")
	result = cursor.fetchone()

	cursor.close()
	conn.close()

	return f"<h1>{result[0]}</h1>"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
