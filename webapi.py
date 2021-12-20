from flask import Flask, send_from_directory
from flask_restful import Api, Resource, request
from main import generate_app, add_request

app = Flask(__name__)


@app.route('/generateApp')
def generateApp():
    generate_app()
    return ''


@app.route('/addRequest', methods=['POST'])
def addRequst():
    if request.method == 'POST':
        request_data = request.get_json()
        fun = request_data["function_name"]
        rt = request_data["request_type"]
        url = request_data["url"]
        add_request(fun, rt, url)
        return ''


if __name__ == "__main__":
    app.run(debug=True)
