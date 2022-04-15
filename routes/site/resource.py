from flask_jwt_extended import jwt_required, get_jwt
from flask import Blueprint, render_template

# Criando blueprint
app_resource_site = Blueprint('resource_site', __name__)


@app_resource_site.route('/', methods=["GET"])
@jwt_required()
def details_jwt():
    # pega a chave sub dos claims do jwt, que contem os dados do usuario
    claims = get_jwt()
    # renderiza o template
    return render_template('resource/details_jwt.html', claims=claims)
