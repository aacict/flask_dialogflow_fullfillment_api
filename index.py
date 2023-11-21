from flask import Flask, jsonify
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET'])
def studentInformation():
    student_info = { "student_number": "200573774","student_name": "Ashish Thapa", "student_email": "aacict@gmail.com" }
    return jsonify(student_info)

@app.route('/webhook', methods=['GET'])
def fullfillmentWebhook():
    return "Hello World!"

if __name__ == '__main__':
    serve(app, host="localhost", port=3000)
