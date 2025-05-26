from flask import Flask
from flask_cors import CORS
from config import Config
from apps.app1 import app_bp

test_app = Flask(__name__)

# Definimos CORS
CORS(test_app)

# Registramos blueprints
test_app.register_blueprint(app_bp, url_prefix='/testapp')

@test_app.route('/')
def home():
    return 'Server CSAToolbox working...'

if __name__ == '__main__':
    test_app.run(debug=True)