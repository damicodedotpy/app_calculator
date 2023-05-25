# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************
from num2words import num2words
# ******************************OWN LIBRARIES*********************************

# ****************************************************************************

def operatorConversor(operator):
    '''This functions helps to
    map an specific 'operator name'
    to its symbol, wich will be the
    real character to show in the
    screen.'''
    
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
    '''This function turns a string 
    number into the textual writting 
    form of that number
    
    We use the library 'num2words'
    which receives as parameter a 
    float or int number, so the first
    step is to convert our string
    number to one of them.
    '''
    
    # Transform the string into a float
    # if there is a dot in it
    if "." in number:
        casted_number = float(number)
    # Transform the string into an int
    # if there is no dots in it
    else:
        casted_number = int(number)
    
    # Translate the number to text in English
    if language == "en":
        english_string = num2words(casted_number, lang="en")
        return english_string
    
    # Translate the number to text in Spanish
    if language == "es":
        spanish_string = num2words(casted_number, lang="es")
        return spanish_string
        