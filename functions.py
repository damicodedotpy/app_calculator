# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************
from num2words import num2words
# ******************************OWN LIBRARIES*********************************

# ****************************************************************************

def operatorConversor(operator):
    if operator == "add":
        return {"name": "add", "symbol": "+"}
    elif operator == "substract":
        return {"name": "substract", "symbol": "-"}
    elif operator == "plus":
        return {"name": "plus", "symbol": "*"}
    elif operator == "divide":
        return {"name": "divide", "symbol": "/"}
    elif operator == "equal":
        return {"name": "equal", "symbol": "="}
    elif operator == "dot":
        return {"name": "dot", "symbol": "."}
    elif operator == "reset":
        return {"name": "reset", "symbol": "C"}
    elif operator == "percentage":
        return {"name": "percentage", "symbol": "%"}
    elif operator == "braces":
        return {"name": "braces", "symbol": "()"}
    elif operator == "comma":
        return {"name": "comma", "symbol": ","}
    
def numToWords(number, language):
    if "." in number:
        casted_number = float(number)
    else:
        casted_number = int(number)
    
    if language == "en":
        english_string = num2words(casted_number, lang="en")
        return english_string
    
    if language == "es":
        spanish_string = num2words(casted_number, lang="es")
        return spanish_string
        