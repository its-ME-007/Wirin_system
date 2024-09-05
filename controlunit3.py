from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the status dictionary to keep track of the states
status = {
    "ControlUnitStatus": {
        "LEVEL1_CU": {
            "ECU2-ICU": {"Heartbeat": 0, "Status": "N/A"},
            "ECU6-VHMS": {"Heartbeat": 0, "Status": "N/A"},
            "17- Monitor and Processor": {"Heartbeat": "N/A", "Status": "ACTIVE/PROCESSING/BUSY"},
            "MPU - Motion Planner": {"Heartbeat": "N/A", "Status": "PROCESSING/ACTIVE/BUSY/OVERLOAD"}
        },
        "LEVEL2_CU": {
            "ECU1-VCU": {"Heartbeat": 0, "ActiveSoul": "MAIN/SHADOW"},
            "ECUX-FCU": {"Heartbeat": 0, "Status": "N/A"},
            "ECU3-DoorECU": {"Heartbeat": 0, "ActiveSoul": "MAIN/SHADOW"},
            "ECU4-RPi-OUT": {"Heartbeat": 0, "Status": "N/A"},
            "ECU5-RPi-IN": {"Heartbeat": 0, "Status": "N/A"},
            "ECU7-HVAC": {"Heartbeat": 0, "Status": "N/A"},
            "ECU8-USU": {"Heartbeat": 0, "Status": "N/A"},
            "ECU9-LCU": {"Heartbeat": 0, "Status": "N/A"},
            "ECU10-DashboardECU": {"Heartbeat": 0, "Status": "N/A"},
            "ECU11-TableECU": {"Heartbeat": 0, "Status": "N/A"}
        }
    }
}

# Function to validate if the level and ECU exist
def validate_level_and_ecu(level, ecu):
    if level not in status["ControlUnitStatus"]:
        return False, "Invalid level"
    if ecu not in status["ControlUnitStatus"][level]:
        return False, "Invalid ECU"
    return True, None

# Define endpoints for setting and getting ECU status
@app.route('/controlunitstatus/<level>/<ecu>/<attribute>/<value>', methods=['POST'])
def set_ecu_status(level, ecu, attribute, value):
    valid, error_message = validate_level_and_ecu(level, ecu)
    if not valid:
        return jsonify({"error": error_message}), 400

    if attribute in status["ControlUnitStatus"][level][ecu]:
        if attribute == "Heartbeat":
            if value not in ["1", "0"]:
                return jsonify({"error": "Invalid heartbeat value, must be '1' or '0'"}), 400
            status["ControlUnitStatus"][level][ecu][attribute] = int(value)
        else:
            status["ControlUnitStatus"][level][ecu][attribute] = value
        return jsonify({"status": f"{ecu} {attribute} is now {value}"}), 200

    return jsonify({"error": "Invalid attribute"}), 400

@app.route('/controlunitstatus/<level>/<ecu>/<attribute>', methods=['GET'])
def get_ecu_status(level, ecu, attribute):
    valid, error_message = validate_level_and_ecu(level, ecu)
    if not valid:
        return jsonify({"error": error_message}), 400

    if attribute in status["ControlUnitStatus"][level][ecu]:
        return jsonify({attribute: status["ControlUnitStatus"][level][ecu][attribute]}), 200
    
    return jsonify({"error": "Invalid attribute"}), 400

# Define endpoint for retrieving the overall control unit status
@app.route('/status/controlunitstatus', methods=['GET'])
def get_control_unit_status():
    return jsonify({"ControlUnitStatus": status["ControlUnitStatus"]}), 200

if __name__ == '__main__':
    app.run(debug=True)
