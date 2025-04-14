from flask import Flask
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# db = SQLAlchemy()
# migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from app.routes import blueprint
    CORS(blueprint, supports_credentials=True, resources={r"/api/v1/*": {"origins": "*"}}) # Change this
    app.register_blueprint(blueprint, url_prefix='/api/v1')

    return app
