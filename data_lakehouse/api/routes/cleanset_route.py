from flask import Blueprint, jsonify

cleansed_bp = Blueprint('cleansed', __name__, url_prefix='/cleansed')

@cleansed_bp.route('/', methods=['GET'])
def clean_dataset():
    return jsonify({'code': 200, 'message': 'Dataset cleaned'}), 200
