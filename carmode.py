from flask import Blueprint, jsonify, request

carmode_bp = Blueprint('carmode', __name__)

# Assuming you have a way to store the current car mode
car_mode = "ENTERTAINMENT_MODE"

@carmode_bp.route('/carmode/set', methods=['POST'])
def set_car_mode():
    global car_mode
    data = request.json
    mode = data.get('mode')
    if mode not in ["ENTERTAINMENT_MODE", "AMBIENT_MODE", "FOCUS_MODE", "NIGHT_MODE", "RIDE_MODE"]:
        return jsonify({"error": "Invalid mode"}), 400
    car_mode = mode
    result = f"Setting car mode to {mode}"
    return jsonify({"result": result})

@carmode_bp.route('/carmode/get', methods=['GET'])
def get_car_mode():
    global car_mode
    result = f"Current car mode is {car_mode}"
    return jsonify({"result": result})
