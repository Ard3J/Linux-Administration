from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
	conn = mysql.connector.connect(
		host="localhost",
		user="exampleuser",
		password="Salasan@",
		database="exampledb"
	)
	cursor = conn.cursor()
	#cursor.execute("SELECT 'Minun sivu. Kello on: '") #  CURTIME()")
	cursor.execute("SELECT 'Minun sivu.'")
	result0 = cursor.fetchone()
	cursor.execute("SELECT 'MySQL-serverin kello on: '")
	result1 = cursor.fetchone()
	cursor.execute("SELECT  CURTIME()")
	result2 = cursor.fetchone()
	#result = cursor.fetchall()

	cursor.close()
	conn.close()

	return f"<h1>{result0[0]}</h1> <p>{result1[0]} {result2[0]}</p>"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
