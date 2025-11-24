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

		<style>
		  	body {{background-color: lightgray; text-align:center;padding-top: 70px}}
			.box {{background-color: powderblue; display: inline-block; padding: 30px 30px; border-radius: 10px; box-shadow: 5px 10px 5px grey}}
		</style>
		<body>
			<div class="box">
				<h1>Linux Administration LEMP sivu</h1>
				<p>{mysql_message}</p>
				<p>MySQL server time {mysql_time}</p>
				<p>Streamlit app <a href="http://86.50.22.177:8501/data-analysis">linkki</a> mutta jostain syystä portti pitää siinä olla</p>
			</div>
		</body>
	</html>
	"""


	return html

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
