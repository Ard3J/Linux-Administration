from flask import Flask, jsonify
import os
import mysql.connector
from datetime import datetime, timezone    #Aikavyöhykettä käsittelemään

#flask app instance update joo
app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

@app.get('/api/health')
def health():
    return jsonify(message={'status': 'ok'})

@app.get('/api/time')
def time():
    # Placeholder for actual time fetching logic
    #get server time from db
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
    cur = conn.cursor()
    cur.execute("SELECT NOW()")
    row = cur.fetchone()
    cur.close(); conn.close()
    #Standardisoi aikaformaatin,. niin frontend pitäisi laittaa paikalliseen aikaan 
    server_time_dt = row[0]
    if server_time_dt.tzinfo is None:
        # Asettaa aikavyöhykkeen oletetuksi UTC:ksi
        utc_dt = server_time_dt.replace(tzinfo=timezone.utc)
    else:
        # Jos tzinfo on jo olemassa
        utc_dt = server_time_dt.astimezone(timezone.utc)
    iso_time_str = utc_dt.isoformat()
    return jsonify(message={'time': iso_time_str})

@app.get('/api/')
def index():
    """Simple endpoint that greets from DB."""
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
    cur = conn.cursor()
    cur.execute("SELECT 'Hello from MySQL via Testi!'")
    row = cur.fetchone()
    cur.close(); conn.close()
    return jsonify(message=row[0])

@app.get('/')
def root_check():
    """Returns a simple JSON status for the root path."""
    return jsonify(status='Backend is running', version='1.0')

if __name__ == '__main__':
    # Dev-only fallback
    app.run(host='0.0.0.0', port=8000, debug=True)
