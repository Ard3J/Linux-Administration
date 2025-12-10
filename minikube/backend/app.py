from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
	return mysql.connector.connect(
		host=os.getenv('DB_HOST', 'mysql'),
		user=os.getenv('DB_USER', 'appuser'),
		password=os.getenv('DB_PASSWORD', 'apppassword123'),
	database=os.getenv('DB_NAME', 'appdb')
	)

@app.route('/api/health')
def health():
	return jsonify({"status": "healthy"})

@app.route('/api/users')
def get_users():
	try:
		conn = get_db_connection()
		cursor = conn.cursor(dictionary=True)
		cursor.execute("SELECT * FROM users")
		users = cursor.fetchall()
		cursor.close()
		conn.close()
		return jsonify(users)
	except Exception as e:
		return jsonify({"error": str(e)}), 500

@app.route('/api/user-count')
def count_users():
	try:
		conn = get_db_connection()
		cursor = conn.cursor()
		cursor.execute("SELECT COUNT(*) FROM users")
		#COUNT palauttaa tuplen niin pitää hieman muotoilla paremmaksi
		count_tuple = cursor.fetchone()	
		user_count = count_tuple[0]
		cursor.close()
		conn.close()
		return jsonify(user_count)
	except Exception as e:
		return jsonify({"error": str(e)}), 500

@app.route('/api/add-user', methods=['POST'])
def add_user():
	try:
		#Haetaan frontendistä
		data = request.get_json()
		name = data['name']
		email = data['email']

		if not name or  not email:
			return jsonify({"error": "Missing name or email"}), 400
		#Rajoitetaan pituus ettei tule database erroreita
		if len(name) > 100 or len(email) > 100:
			return jsonify({"error": "Name and email must be  100 characters or less"}), 400
		conn = get_db_connection()
		cursor = conn.cursor()
		#Välivaihe että saadaan cursor.executelle oikeassa muodossa muuttujia sisältävä lause
		insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
		cursor.execute(insert_query, (name, email))
		conn.commit()
		new_id = cursor.lastrowid
		cursor.close()
		conn.close()
		return jsonify({"message":"User added succesfully", "id": new_id, "name": name,"email":email}),201
	except Exception as e:
		return jsonify({"error": str(e)}), 500

@app.route('/api/init-db')
def init_db():
	try:
		conn = get_db_connection()
		cursor = conn.cursor()
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS users (
		id INT AUTO_INCREMENT PRIMARY KEY,
		name VARCHAR(100),
		email VARCHAR(100)
		)
		""")
		cursor.execute("""
		INSERT INTO users (name, email) VALUES
		('John Doe', 'john@example.com'),
		('Jane Smith', 'jane@example.com')
		""")
		conn.commit()
		cursor.close()
		conn.close()
		return jsonify({"message": "Database initialized"})
	except Exception as e:
		return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
