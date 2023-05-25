# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************
from flask import Flask
# ******************************OWN LIBRARIES*********************************
from routes import blp as CalculatorBlueprint
# ****************************************************************************


def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(CalculatorBlueprint)
    return app