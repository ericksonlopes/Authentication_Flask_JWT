from flask_jwt_extended import set_access_cookies, create_access_token, unset_jwt_cookies, jwt_required
from flask import Blueprint, request, render_template, redirect
from datetime import datetime

# Criando blueprint das rotas de autenticação da api
app_auth_site = Blueprint('auth_site', __name__)

# dados para teste
user = {
    "id": 1, "username": "admin", "password": "123", "created_at": datetime.now().date().strftime('%d/%m/%Y %H:%M:%S')
}


@app_auth_site.route('/login', methods=["GET", "POST"])
def login_site():
    if request.method == "GET":
        return render_template('auth/login.html')

    if request.method == "POST":
        # Pega os dados enviados no form
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        # verifica se exite o usuario
        if username == user['username'] and password == user['password']:
            response = redirect('/site/resource/details-jwt')
            # Cria o token
            access_token = create_access_token(identity=user)
            # adiciona o token dentro dos cookies
            set_access_cookies(response, access_token)
            return response


@app_auth_site.route('/logout', methods=["GET"])
@jwt_required(locations="cookies")
def logout_site():
    response = redirect('/site/auth/login')
    # remove o token do cookie, e invalida ele
    unset_jwt_cookies(response)
    return response
