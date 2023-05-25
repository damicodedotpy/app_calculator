# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************
from flask import (request, render_template, Blueprint)
# ******************************OWN LIBRARIES*********************************
from functions import operatorConversor, numToWords
# ****************************************************************************

# Blueprint for the calculator functionalities
blp = Blueprint("calculator", __name__, template_folder="/templates/calculator.html")

# Temporal variables
num_list = []
historial = []
operator = ""
string_number = ""
screen_result = ""
spanish_number = ""
english_number = ""

@blp.route("/calculator", methods=["GET", "POST"])
def calculate():
    # I made the temporal variables 'goblal'
    # in order to access to them from the 
    # method and be able to modify them.
    global num_list, operator, string_number, screen_result, spanish_number, english_number, historial
    
    # Aritmetic operator receiver and coversor
    entered_operator = operatorConversor(request.args.get("operator"))
    # Number receiver
    entered_number = request.args.get("number")
    
    # Artimetic operator's logic
    if entered_operator:
        
        # For the case the user press 'C' for reset
        if entered_operator["name"] == "reset":
            num_list = []
            historial = []
            operator = ""
            string_number = ""
            screen_result = ""
            spanish_number = ""
            english_number = ""
            
        # For the case the user wants to calculate
        # something but there is no formula typed
        elif entered_operator["name"] == "equal" and string_number == "":
            screen_result = ""
            
        # For the case the user wants to calculate
        # something and there is formula typed
        elif entered_operator["name"] == "equal":
            
            # The formula is resolved and delivered
            try:
                equation = string_number
                calc = eval(string_number)
                string_number = str(calc)
                screen_result = string_number
                
                spanish_number = numToWords(string_number, "es")
                english_number = numToWords(string_number, "en")
                historial.append((equation, calc))
                
            # For the case the formula is a zero
            # dividing zero operation
            except ZeroDivisionError:
                screen_result = "\ (T o T) / Boom!"
                
            # For the case the formula do not 
            # represents a valid aritmetic operation
            # or number, for example '8.1.1'
            except SyntaxError:
                screen_result = "X_x Bad syntax!"
                
            # For the case the formula has invalid
            # characters
            except TypeError:
                screen_result = "o_- WTF was that!"
                
            # For the case the translation process
            # of number to text fails due to the 
            # size
            except OverflowError:
                english_number = "\ (T o T) / \t HOLLY SH@#$ are you kiddin' me? I can not eve read it!!"
                spanish_number = "\ (T o T) / \t OSTIAAAS!! Nisiquiera lo puedo leer"
        
        # For the case the user's first choice is a dot
        elif entered_operator["name"] == "dot" and string_number == "":
            string_number += "0."
            screen_result = string_number
            
        # For the case the user's first choice is any 
        # other aritmetic operator different than dot
        elif entered_operator["name"] != "dot" and string_number =="":
            screen_result = string_number
            
        # For the case we already have a formula and
        # the user input an aritmetic operator
        elif entered_operator["name"]:
            string_number += entered_operator["symbol"]
            screen_result = string_number
            
            # For the case the user tries to input two
            # or more aritmetic operators consecutively.
            if string_number[-1] in ["+", "-", "*", "/", "%", "()", ",", ".", "="] and string_number[-2] in ["+", "-", "*", "/", "%", "()", ",", ".", "="]:
                string_number = string_number[:-2]
                string_number = f"{string_number}{entered_operator['symbol']}"
                screen_result = string_number
                
    # Number input logic
    if entered_number:
        string_number += entered_number
        screen_result = string_number
        
    # Render information processed to the 
    # 'calculator.html' template
    return render_template("calculator.html", 
                            screen_result=screen_result, 
                            spanish_number=spanish_number, 
                            english_number=english_number, 
                            historial=historial)
