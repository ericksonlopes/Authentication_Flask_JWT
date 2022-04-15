from flask_jwt_extended import JWTManager
from config import create_app
from routes import *

app = create_app()
jwt = JWTManager(app)

# registra as rotas do pacote 'routes' com blueprints
app.register_blueprint(app_auth_api, url_prefix='/api/auth')
app.register_blueprint(app_resource_api, url_prefix='/api/resource')

app.register_blueprint(app_auth_site, url_prefix='/auth')
app.register_blueprint(app_resource_site, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
