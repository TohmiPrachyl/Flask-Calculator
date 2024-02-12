from flask import Flask, render_template, request
from Calculator import simple_calculator    #imports my Calculator program

app = Flask(__name__)

@app.route('/')                             #grabs my index.html and renders it
def home():
    return render_template("index.html", error_message=None, result=None)

@app.route('/calculate', methods=['POST'])  # We want to post not get for security 
def calculate():                            # decribes what function is being preformed
    num1 = request.form['num1']             # its basiclly a summary of the simple_calculator function
    num2 = request.form['num2']
    operator = request.form['operator']
    
    try:
        result = simple_calculator(num1, num2, operator)
        return render_template('index.html', error_message=None, result=result)
    except Exception as e:
        return render_template('index.html', error_message=str(e), result=None)

if __name__ == "__main__":
    app.run(debug=True)
