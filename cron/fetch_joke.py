#!/usr/bin/env python3
import requests
import mysql.connector
import os					#os ja dotenv antaa hakea .env tiedostosta salaiset asiat
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

USER = os.getenv('MYSQLUSER')
PASSWD = os.getenv('MYSQLPASS')

URL = f'https://official-joke-api.appspot.com/random_joke'
conn = mysql.connector.connect(host='localhost', user=USER, password=PASSWD, database='jokes')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS jokes_data (id INT AUTO_INCREMENT PRIMARY KEY, setup VARCHAR(100), punchline VARCHAR(100), timestamp DATETIME)''')
response = requests.get(URL)
data = response.json()
setup = data['setup']
punchline = data['punchline']
timestamp = datetime.now() + timedelta(hours=2)		#Laitetaan suomen aikaan
cursor.execute('INSERT INTO jokes_data (setup, punchline, timestamp) VALUES (%s, %s, %s)', (setup, punchline, timestamp))
conn.commit()
cursor.close()
conn.close()
print(f'Data tallennettu: {setup} {punchline} {timestamp}')
