from flask import Flask
import mysql.connector
#import os				#os ja dotenv antaa hakea .env tiedostosta salaiset asiat
#from dotenv import load_dotenv

app = Flask(__name__)
@app.route('/')

#load_dotenv()
#PASSWD = os.getenv('MYSQLPASS')
def home():
	conn = mysql.connector.connect(
		host="localhost",
		user="exampleuser",
		password='Salas4n@',
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
				<p>Streamlit app <a href="/data-analysis">linkki</a></p>
				<p>MQTT chat <a href="/chat/">linkki</a></p>
				<p>Minikube <a href="/kube/">linkki</a><p/>
			</div>
		</body>
	</html>
	"""


	return html

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
