from flask import Blueprint, jsonify, request

bywiresystem_bp = Blueprint('bywiresystem', __name__)

# Assuming you have a way to store the current by-wire system statuses
steering_status = "Open"
acc_brake_pedal_status = "Open"

@bywiresystem_bp.route('/bywiresystem/steering/set', methods=['POST'])
def set_steering_status():
    global steering_status
    data = request.json
    action = data.get('action')
    if action not in ["Open", "Close", "Opening", "Closing", "Error"]:
        return jsonify({"error": "Invalid action"}), 400
    steering_status = action
    result = f"Setting steering status to {action}"
    return jsonify({"result": result})

@bywiresystem_bp.route('/bywiresystem/steering/get', methods=['GET'])
def get_steering_status():
    global steering_status
    result = f"Current steering status is {steering_status}"
    return jsonify({"result": result})

@bywiresystem_bp.route('/bywiresystem/accbrake/set', methods=['POST'])
def set_acc_brake_pedal_status():
    global acc_brake_pedal_status
    data = request.json
    action = data.get('action')
    if action not in ["Open", "Close", "Opening", "Closing", "Error"]:
        return jsonify({"error": "Invalid action"}), 400
    acc_brake_pedal_status = action
    result = f"Setting accelerator/brake pedal status to {action}"
    return jsonify({"result": result})

@bywiresystem_bp.route('/bywiresystem/accbrake/get', methods=['GET'])
def get_acc_brake_pedal_status():
    global acc_brake_pedal_status
    result = f"Current accelerator/brake pedal status is {acc_brake_pedal_status}"
    return jsonify({"result": result})
