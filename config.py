from flask import Flask, render_template
import os


def create_app() -> Flask:
    """
    Configurações do flask
    :return retorna a instancia flask com nossas configurações :
    """
    app = Flask(__name__)

    # Passando rota do template
    app.template_folder = os.path.dirname(os.path.realpath(__file__)) + '\\templates'

    # configurando chave secreta do jwt
    app.config["JWT_SECRET_KEY"] = "guardarsenhaemlocalseguro"

    # Definindo por onde o token pode ser passado
    app.config['JWT_TOKEN_LOCATION'] = ['cookies', 'headers']

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app
