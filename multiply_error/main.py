import functions_framework
from flask import jsonify


@functions_framework.http
def multiply(request):
    request_json = request.get_json()
    output = {"multiplied": 2 * int(request_json['input'])}
    return jsonify(output)