from flask_jwt_extended import create_access_token
from flask import Blueprint, request, jsonify
from datetime import datetime

# Criando blueprint das rotas de autenticação da api
app_auth_api = Blueprint('auth_api', __name__)

# Dados para teste
user = {
    "id": 1, "username": "admin", "password": "123", "created_at": datetime.now().date().strftime('%d/%m/%Y %H:%M:%S')
}


@app_auth_api.route('/login', methods=['POST'])
def login():
    """
    Rota que autentica e gera um token
    :return:
    """
    # Captura o json recebido
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # valida as credenciais
    if username == user['username'] and password == user['password']:
        # cria o token
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token), 201
    else:
        return jsonify("Usuario ou senha invalidos"), 401
