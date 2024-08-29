from flask import Flask, jsonify, request
import threading

app = Flask(__name__)

# Define the status dictionary to keep track of the states
status = {
    "ControlSettings": {
        "LowLevelControlMode": "Manual Mode",
        "PIDStatus": {
            "MasterControl": "OFF",
            "SteeringRack": "OFF",
            "Brake": "OFF",
            "Motors": "OFF"
        },
        "MasterPIDValues": {
            "SteeringPIDOutput": 0,
            "BrakePIDOutput": 0,
            "MotorRPIDOutput": 0,
            "MotorLPIDOutput": 0,
            "MasterPIDCommandOutput": 0
        }
    }
}

# Define a lock for thread safety
lock = threading.Lock()

# Define a function to validate the Low Level Control Mode
def validate_low_level_control_mode(mode):
    valid_modes = ["Autonomous LEVEL 5", "Autonomous LEVEL 4", "Autonomous LEVEL 3", "Autonomous LEVEL 2", "Autonomous LEVEL 1", "Manual Mode", "Hardware Mode"]
    return mode in valid_modes

# Define a function to validate the PID status component
def validate_pid_component(component):
    return component in status["ControlSettings"]["PIDStatus"]

# Define a function to validate the Master PID value
def validate_master_pid_component(component, value):
    if component in ["SteeringPIDOutput", "BrakePIDOutput"]:
        return -1024 <= value <= 1024
    elif component in ["MotorRPIDOutput", "MotorLPIDOutput"]:
        return 0 <= value <= 5000
    elif component == "MasterPIDCommandOutput":
        return 0 <= value <= 1000
    return False

# Define endpoints for setting and getting Low Level Control Mode
@app.route('/controlsettings/lowlevelcontrolmode/<mode>', methods=['POST'])
def set_low_level_control_mode(mode):
    if validate_low_level_control_mode(mode):
        with lock:
            status["ControlSettings"]["LowLevelControlMode"] = mode
        return jsonify({"status": f"Low Level Control Mode is now {mode}"}), 200
    return jsonify({"error": "Invalid mode"}), 400

@app.route('/controlsettings/lowlevelcontrolmode', methods=['GET'])
def get_low_level_control_mode():
    return jsonify({"LowLevelControlMode": status["ControlSettings"]["LowLevelControlMode"]}), 200

# Define endpoints for setting and getting PID status
@app.route('/controlsettings/pidstatus/<component>/<action>', methods=['POST'])
def set_pid_status(component, action):
    if validate_pid_component(component) and action in ["ON", "OFF"]:
        with lock:
            status["ControlSettings"]["PIDStatus"][component] = action
        return jsonify({"status": f"{component} is now {action}"}), 200
    return jsonify({"error": "Invalid component or action"}), 400

@app.route('/controlsettings/pidstatus/<component>', methods=['GET'])
def get_pid_status(component):
    if validate_pid_component(component):
        return jsonify({component: status["ControlSettings"]["PIDStatus"][component]}), 200
    return jsonify({"error": "Invalid component"}), 400

# Define endpoints for setting and getting Master PID values
@app.route('/controlsettings/masterpidvalues/<component>/<int:value>', methods=['POST'])
def set_master_pid_values(component, value):
    if component in status["ControlSettings"]["MasterPIDValues"] and validate_master_pid_component(component, value):
        with lock:
            status["ControlSettings"]["MasterPIDValues"][component] = value
        return jsonify({"status": f"{component} is now {value}"}), 200
    return jsonify({"error": "Invalid component or value"}), 400

@app.route('/controlsettings/masterpidvalues/<component>', methods=['GET'])
def get_master_pid_values(component):
    if component in status["ControlSettings"]["MasterPIDValues"]:
        return jsonify({component: status["ControlSettings"]["MasterPIDValues"][component]}), 200
    return jsonify({"error": "Invalid component"}), 400

# Define endpoint for retrieving the status of each component
@app.route('/status/controlsettings', methods=['GET'])
def get_control_settings_status():
    return jsonify(status["ControlSettings"]), 200

if __name__ == '__main__':
    app.run(debug=True)
