from flask import Blueprint, jsonify

health_check = Blueprint('health_check', __name__)

@health_check.route('/health-check')
def check():
  return jsonify(success=True)
