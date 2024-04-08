from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Inicializa o banco de dados
def init_user_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# Adiciona um novo usuário
@app.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.json
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (data['name'], data['email']))
        conn.commit()
        return jsonify({'message': 'Usuário adicionado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    finally:
        conn.close()

# Lista todos os usuários
@app.route('/users', methods=['GET'])
def list_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    init_user_db()
    app.run(port=5000, debug=True)
