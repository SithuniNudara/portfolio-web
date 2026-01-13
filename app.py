from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    
    print("\n=== New Contact Form Submission ===")
    print(f"Name: {data.get('name')}")
    print(f"Email: {data.get('email')}")
    print(f"Message: {data.get('message')}")
    print("===================================\n")
    
    return jsonify({
        'status': 'success',
        'message': 'Thank you for your message! I will get back to you soon.'
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)