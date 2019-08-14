import os

from flask import Flask  # Import the Flask class
from .config import Config

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')
    app.config.from_object(Config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # from cdp import views
    # app.register_blueprint(views.bp)

    # app.add_url_rule('/', endpoint='compare')

    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    
    return app

app = create_app()
