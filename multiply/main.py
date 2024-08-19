import functions_framework
from flask import jsonify, Response


@functions_framework.http
def multiply(request):
    request_json = request.get_json()
    value = int(request_json['input'])
    if value == 100:
        return jsonify("Gateway timeout hit"), 504
        
    output = {"multiplied": 2 * value}
    return jsonify(output)