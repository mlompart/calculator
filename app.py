"""
A simple Flask application to perform basic arithmetic operations
based on URL query parameters.
"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/calculate')

def calculate():
    """calculation of two arguments"""

    # Get query parameters
    operation = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    # Perform the requested operation
    if operation == 'sum':
        result = arg1 + arg2
        return f'{arg1} + {arg2} = {result}'

    return f'unknown operation: {operation}'

if __name__ == '__main__':
    app.run()
