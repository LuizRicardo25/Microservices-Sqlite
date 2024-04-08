from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/notify/<int:user_id>', methods=['POST'])
def notify_user(user_id):
    # Obtem informações do usuário do Microserviço de Usuários
    user_info = requests.get(f'http://localhost:5000/users/{user_id}')
    if user_info.status_code == 200:
        # Lógica fictícia para enviar notificação
        return jsonify({'message': f'Notificação enviada para {user_info.json()["name"]}!'}), 200
    else:
        return jsonify({'message': 'Usuário não encontrado.'}), 404

if __name__ == '__main__':
    app.run(port=5001, debug=True)
