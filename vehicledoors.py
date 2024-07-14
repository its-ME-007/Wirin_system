from flask import Blueprint, jsonify, request

vehicledoor_bp = Blueprint('vehicledoor', __name__)

# Assuming you have a way to store the current door status
door_status = "Closed"

@vehicledoor_bp.route('/vehicledoor/set', methods=['POST'])
def set_door_status():
    global door_status
    data = request.json
    action = data.get('action')
    if action not in ["Open", "Close", "Opening", "Closing", "Error"]:
        return jsonify({"error": "Invalid action"}), 400
    door_status = action
    result = f"Setting door status to {action}"
    return jsonify({"result": result})

@vehicledoor_bp.route('/vehicledoor/get', methods=['GET'])
def get_door_status():
    global door_status
    result = f"Current door status is {door_status}"
    return jsonify({"result": result})
