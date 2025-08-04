from flask import Flask, request, jsonify, render_template
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')
    
    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2
        elif operation == "modulus":
            result = num1 % num2
        elif operation == "percentage":
            result = (num1 / num2) * 100
        elif operation == "square":
            result = num1 ** 2
        elif operation == "squareroot":
            result = math.sqrt(num1)
        elif operation == "cube":
            result = num1 ** 3
        elif operation == "cuberoot":
            result = num1 ** (1/3)
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
