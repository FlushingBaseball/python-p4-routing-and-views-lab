#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)



@app.route("/")
def index():
    return('<h1>Python Operations with Flask Routing and Views</h1>')

@app.route('/print/<string:test>')
def print_parameter(test):
    print(f'{test}')
    return(f'{test}')


@app.route("/count/<int:num>")
def count(num):
    count = f""
    for number in range(num):
        count +=f'{number}\n'
    return  count
    # apples = [print(x) for x in range(num)]
    # return apples 


@app.route("/math/<int:number1>/<string:operation>/<int:number2>")
def math(number1, operation, number2):
    if operation == "+":
        return str(number1 + number2)
    elif operation == "-":
        return str(number1 - number2)
    elif operation == "*":
        return str(number1 * number2)
    elif operation == "div":
        return str(number1 / number2)
    elif operation == "%":
        return str(number1 % number2)
    else:
        return (f"Invalid operation: {operation}")
    
