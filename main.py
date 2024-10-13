from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='./new-client/dist', static_url_path='')
CORS(app)

# Serve the React index.html file for the root path
@app.route('/')
def serve():
    return app.send_static_file('index.html')

# Example API route
@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from Flask!"})

# Handle 404 errors and return index.html
@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
