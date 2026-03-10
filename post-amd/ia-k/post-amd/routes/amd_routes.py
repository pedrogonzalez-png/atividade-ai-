from flask import Blueprint, request
from controllers.amd_controllers import create_amd

amd_routes = Blueprint('amd_routes', __name__)

@amd_routes.route('/amd', methods=['POST'])
def amd_post():

    amd_data = request.json
    return create_amd(amd_data)