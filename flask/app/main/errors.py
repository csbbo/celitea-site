from flask import make_response,jsonify
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({"error":"Not found"}),404)


@main.app_errorhandler(500)
def internal_server_error(e):
    return make_response(jsonify({"error":"Server Error"}),500)
