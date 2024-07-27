from flask import Flask, jsonify, request
import threading

app = Flask(__name__)

# Define the status dictionary to keep track of the states
status = {
    "OBC": {
        "ACVoltage": 0,
        "ACCurrent": 0,
        "ACPower": 0,
        "ChargingTime": 0,
        "DCVoltage": 0,
        "DCCurrent": 0,
        "OBCTemperature": 0,
        "OBCStatus": 0
    }
}

# Define a lock for thread safety
lock = threading.Lock()

# Define endpoints for setting the value of each component
@app.route('/obc/<component>/<int:value>', methods=['POST'])
def set_obc_value(component, value):
    with lock:
        if component in status["OBC"]:
            if component == "ACVoltage" and 0 <= value <= 300:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "ACCurrent" and 0 <= value <= 100:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "ACPower" and 0 <= value <= 4000:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "ChargingTime" and 0 <= value <= 999:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "DCVoltage" and 0 <= value <= 100:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "DCCurrent" and 0 <= value <= 100:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "OBCTemperature" and 0 <= value <= 150:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "OBCStatus" and 0 <= value <= 255:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
        return jsonify({"error": "Invalid component or value"}), 400

# Define endpoints for retrieving the value of each component
@app.route('/obc/<component>', methods=['GET'])
def get_obc_value(component):
    with lock:
        if component in status["OBC"]:
            return jsonify({component: status["OBC"][component]}), 200
        return jsonify({"error": "Invalid component"}), 400

# Define endpoints for retrieving the status of each component
@app.route('/status/obc', methods=['GET'])
def get_obc_status():
    with lock:
        return jsonify(status["OBC"]), 200

if __name__ == '__main__':
    app.run(debug=True)