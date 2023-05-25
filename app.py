# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************
from flask import Flask
# ******************************OWN LIBRARIES*********************************
from routes import blp as CalculatorBlueprint
# ****************************************************************************


def create_app():
    # Framework's instance
    app = Flask(__name__)
    
    # Blueprints registration
    app.register_blueprint(CalculatorBlueprint)
    
    return app