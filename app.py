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
	mysql_message = cursor.fetchone()[0]

	cursor.execute("SELECT CURTIME()")
	mysql_time = cursor.fetchone()[0]

	cursor.close()
	conn.close()

	html =  f"""
	<html>
		<head>
			<title>Linux Administration LEMP sivu</title>
		</head>
		<body>
			<h1>Linux Administration LEMP sivu</h1>
			<p>{mysql_message}</p>
			<p>MySQL server time {mysql_time}</p>
			<p>Streamlit app <a href="/data-analysis">linkki</a> mutta jokin ei toimi</p>
		</body>
	</html>
	"""


	return html

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
