from flask import Flask, jsonify
app = Flask(__name__)

class CustomError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {'message': self.message}

@app.errorhandler(CustomError)
def handle_custom_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.errorhandler(500)
def internal_error(error):
    response = jsonify({'message': 'Internal server error'})
    response.status_code = 500
    return response

@app.route('/example')
def example_route():
    try:
        # Your code here
        pass
    except ValueError as e:
        raise CustomError(f'Value error occurred: {str(e)}', 400)
    except Exception as e:
        raise CustomError(f'An unexpected error occurred: {str(e)}', 500)

