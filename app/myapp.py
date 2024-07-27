from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecret'
    
    @app.route('/auth/register', methods=['POST'])
    def register():
        return "User registered", 200
    
    @app.route('/auth/login', methods=['POST'])
    def login():
        return "User logged in", 200
    
    return app
