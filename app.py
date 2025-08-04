
from flask import Flask, request, jsonify
from math import sqrt

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = float(data.get('num1', 0))
    num2 = float(data.get('num2', 0))
    operation = data.get('operation', '')

    result = None
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Error: Divide by zero'
        elif operation == 'modulus':
            result = num1 % num2
        elif operation == 'percentage':
            result = (num1 / num2) * 100 if num2 != 0 else 'Error: Divide by zero'
        elif operation == 'square':
            result = num1 ** 2
        elif operation == 'squareroot':
            result = sqrt(num1)
        elif operation == 'cube':
            result = num1 ** 3
        elif operation == 'cuberoot':
            result = num1 ** (1/3)
        else:
            result = 'Invalid operation'
    except Exception as e:
        result = str(e)

    return jsonify({'result': result})
