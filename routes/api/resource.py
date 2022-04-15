from flask_jwt_extended import jwt_required, get_jwt
from flask import Blueprint, jsonify

# Criando blueprint
app_resource_api = Blueprint('resource_api', __name__)


@app_resource_api.route('/details-jwt', methods=["GET"])
@jwt_required(locations='headers')
def details_jwt():
    # retorna os claims na request
    return jsonify(**get_jwt()), 200
