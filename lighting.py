from flask import Flask, jsonify, request
import threading
from datetime import datetime
import time

app = Flask(__name__)

status = {
    "Lighting": {
        "Internal": {
            "RoofLight": {"Status": 0, "Brightness": 0},
            "DoorPuddleLights": {"Status": 0, "Brightness": 0},
            "FloorLights": {"Status": 0, "Brightness": 0},
            "DashboardLights": {"Status": 0, "Brightness": 0},
            "BootLights": {"Status": 0}
        },
        "External": {
            "Headlights": {"Status": 0},
            "TailLights": {"Status": 0},
            "BrakeLights": {"Status": 0},
            "TurnSignals": {"Status": 0},
            "FogLights": {"Status": 0}
        }
    },
    "CarData": {
        "cardata1": {
            "SpeedL": 0,
            "SpeedR": 0,
            "SteeringAngle": 0,
            "BrakeLevel": 0,
            "Gear": "Neutral",
            "FootSwitch": "ON",
            "MotorBrake": "ON",
            "KellyLStatus": 0,
            "KellyRStatus": 0,
            "VehicleError": 0,
        },
        "cardata2": {
            "ihumidity": 0,
            "itemperature": 0,
        },
        "cardata3": {
            "CAN1Stat": "Active",
            "CAN2Stat": "Active",
            "CAN3Stat": "Active",
            "Internet": "Active",
            "Ethernet": "Active"
        },
        "cardata4": {
            "Globalclock": "",
            "Distance_to_empty": 100,
            "DistTravelled": 0,
            "DriveMode": "PARKED"
        }
    },
    "OBC": {
        "AC_Voltage": 0,
        "AC_Current": 0,
        "AC_Power": 0,
        "Charging_Time": 0,
        "DC_Voltage": 0,
        "DC_Current": 0,
        "OBC_Temperature": 0,
        "OBC_Status": 0
    }
}


# Internal lights
def internal_thread(): 
    @app.route('/internal/rooflight/status/post', methods=['POST'])
    def set_internal_rooflight_status():
        light_status = request.json["Status"]
        if light_status not in [0, 1]:
            return jsonify({"Error": "Invalid Status"}), 400
        status["Lighting"]["Internal"]["RoofLight"]["Status"] = light_status
        return jsonify({"RoofLightStatus": status["Lighting"]["Internal"]["RoofLight"]["Status"]})

    @app.route('/internal/rooflight/status/get', methods=['GET'])
    def get_internal_rooflight_status():
        return jsonify({"RoofLightStatus": status["Lighting"]["Internal"]["RoofLight"]["Status"]})

    @app.route('/internal/rooflight/brightness/post', methods=['POST'])
    def set_internal_rooflight_brightness():
        brightness = request.json["Brightness"]
        if not 0 <= brightness <= 100:
            return jsonify({"Error": "Invalid Brightness"}), 400
        status["Lighting"]["Internal"]["RoofLight"]["Brightness"] = brightness
        return jsonify({"RoofLightBrightness": status["Lighting"]["Internal"]["RoofLight"]["Brightness"]})

    @app.route('/internal/rooflight/brightness/get', methods=['GET'])
    def get_internal_rooflight_brightness():
        return jsonify({"RoofLightBrightness": status["Lighting"]["Internal"]["RoofLight"]["Brightness"]})
    
    @app.route('/internal/doorpuddlelights/status/post', methods=['POST'])
    def set_internal_doorpuddlelights_status():
        light_status = request.json["Status"]
        if light_status not in [0, 1]:
            return jsonify({"Error": "Invalid Status"}), 400
        status["Lighting"]["Internal"]["DoorPuddleLights"]["Status"] = light_status
        return jsonify({"DoorPuddleLightsStatus": status["Lighting"]["Internal"]["DoorPuddleLights"]["Status"]})

    @app.route('/internal/doorpuddlelights/status/get', methods=['GET'])
    def get_internal_doorpuddlelights_status():
        return jsonify({"DoorPuddleLightsStatus": status["Lighting"]["Internal"]["DoorPuddleLights"]["Status"]})

    @app.route('/internal/doorpuddlelights/brightness/post', methods=['POST'])
    def set_internal_doorpuddlelights_brightness():
        brightness = request.json["Brightness"]
        if not 0 <= brightness <= 100:
            return jsonify({"Error": "Invalid Brightness"}), 400
        status["Lighting"]["Internal"]["DoorPuddleLights"]["Brightness"] = brightness
        return jsonify({"DoorPuddleLightsBrightness": status["Lighting"]["Internal"]["DoorPuddleLights"]["Brightness"]})

    @app.route('/internal/doorpuddlelights/brightness/get', methods=['GET'])
    def get_internal_doorpuddlelights_brightness():
        return jsonify({"DoorPuddleLightsBrightness": status["Lighting"]["Internal"]["DoorPuddleLights"]["Brightness"]})

    # Similar functions for FloorLights
    @app.route('/internal/floorlights/status/post', methods=['POST'])
    def set_internal_floorlights_status():
        light_status = request.json["Status"]
        if light_status not in [0, 1]:
            return jsonify({"Error": "Invalid Status"}), 400
        status["Lighting"]["Internal"]["FloorLights"]["Status"] = light_status
        return jsonify({"FloorLightsStatus": status["Lighting"]["Internal"]["FloorLights"]["Status"]})

    @app.route('/internal/floorlights/status/get', methods=['GET'])
    def get_internal_floorlights_status():
        return jsonify({"FloorLightsStatus": status["Lighting"]["Internal"]["FloorLights"]["Status"]})

    @app.route('/internal/floorlights/brightness/post', methods=['POST'])
    def set_internal_floorlights_brightness():
        brightness = request.json["Brightness"]
        if not 0 <= brightness <= 100:
            return jsonify({"Error": "Invalid Brightness"}), 400
        status["Lighting"]["Internal"]["FloorLights"]["Brightness"] = brightness
        return jsonify({"FloorLightsBrightness": status["Lighting"]["Internal"]["FloorLights"]["Brightness"]})

    @app.route('/internal/floorlights/brightness/get', methods=['GET'])
    def get_internal_floorlights_brightness():
        return jsonify({"FloorLightsBrightness": status["Lighting"]["Internal"]["FloorLights"]["Brightness"]})

    # Similar functions for DashboardLights
    @app.route('/internal/dashboardlights/status/post', methods=['POST'])
    def set_internal_dashboardlights_status():
        light_status = request.json["Status"]
        if light_status not in [0, 1]:
            return jsonify({"Error": "Invalid Status"}), 400
        status["Lighting"]["Internal"]["DashboardLights"]["Status"] = light_status
        return jsonify({"DashboardLightsStatus": status["Lighting"]["Internal"]["DashboardLights"]["Status"]})

    @app.route('/internal/dashboardlights/status/get', methods=['GET'])
    def get_internal_dashboardlights_status():
        return jsonify({"DashboardLightsStatus": status["Lighting"]["Internal"]["DashboardLights"]["Status"]})

    @app.route('/internal/dashboardlights/brightness/post', methods=['POST'])
    def set_internal_dashboardlights_brightness():
        brightness = request.json["Brightness"]
        if not 0 <= brightness <= 100:
            return jsonify({"Error": "Invalid Brightness"}), 400
        status["Lighting"]["Internal"]["DashboardLights"]["Brightness"] = brightness
        return jsonify({"DashboardLightsBrightness": status["Lighting"]["Internal"]["DashboardLights"]["Brightness"]})

    @app.route('/internal/dashboardlights/brightness/get', methods=['GET'])
    def get_internal_dashboardlights_brightness():
        return jsonify({"DashboardLightsBrightness": status["Lighting"]["Internal"]["DashboardLights"]["Brightness"]})

    # Similar functions for BootLights
    @app.route('/internal/bootlights/status/post', methods=['POST'])
    def set_internal_bootlights_status():
        light_status = request.json["Status"]
        if light_status not in [0, 1]:
            return jsonify({"Error": "Invalid Status"}), 400
        status["Lighting"]["Internal"]["BootLights"]["Status"] = light_status
        return jsonify({"BootLightsStatus": status["Lighting"]["Internal"]["BootLights"]["Status"]})

    @app.route('/internal/bootlights/status/get', methods=['GET'])
    def get_internal_bootlights_status():
        return jsonify({"BootLightsStatus": status["Lighting"]["Internal"]["BootLights"]["Status"]})

# Repeat similar functions for DoorPuddleLights, FloorLights, DashboardLights, BootLights

# External lights
def external_thread(): 
    @app.route('/external/headlights/status/post', methods=['POST'])
    def set_external_headlights_status():
        light_status = request.json["Status"]
        if light_status not in [0, 1]:
            return jsonify({"Error": "Invalid Status"}), 400
        status["Lighting"]["External"]["Headlights"]["Status"] = light_status
        return jsonify({"HeadlightsStatus": status["Lighting"]["External"]["Headlights"]["Status"]})

    @app.route('/external/headlights/status/get', methods=['GET'])
    def get_external_headlights_status():
        return jsonify({"HeadlightsStatus": status["Lighting"]["External"]["Headlights"]["Status"]})
    
    @app.route('/external/taillights/status/post', methods=['POST'])
    def set_external_taillights_status():
        light_status = request.json["Status"]
        if light_status not in [0, 1]:
            return jsonify({"Error": "Invalid Status"}), 400
        status["Lighting"]["External"]["TailLights"]["Status"] = light_status
        return jsonify({"TailLightsStatus": status["Lighting"]["External"]["TailLights"]["Status"]})

    @app.route('/external/taillights/status/get', methods=['GET'])
    def get_external_taillights_status():
        return jsonify({"TailLightsStatus": status["Lighting"]["External"]["TailLights"]["Status"]})
    
    
    @app.route('/external/brakelights/status/post', methods=['POST'])
    def set_external_brakelights_status():
        light_status = request.json["Status"]
        if light_status not in [0, 1]:
            return jsonify({"Error": "Invalid Status"}), 400
        status["Lighting"]["External"]["BrakeLights"]["Status"] = light_status
        return jsonify({"BrakeLightsStatus": status["Lighting"]["External"]["BrakeLights"]["Status"]})

    @app.route('/external/brakelights/status/get', methods=['GET'])
    def get_external_brakelights_status():
        return jsonify({"BrakeLightsStatus": status["Lighting"]["External"]["BrakeLights"]["Status"]})

    @app.route('/external/turnsignals/status/post', methods=['POST'])
    def set_external_turnsignals_status():
        light_status = request.json["Status"]
        if light_status not in [0, 1]:
            return jsonify({"Error": "Invalid Status"}), 400
        status["Lighting"]["External"]["TurnSignals"]["Status"] = light_status
        return jsonify({"TurnSignalsStatus": status["Lighting"]["External"]["TurnSignals"]["Status"]})

    @app.route('/external/turnsignals/status/get', methods=['GET'])
    def get_external_turnsignals_status():
        return jsonify({"TurnSignalsStatus": status["Lighting"]["External"]["TurnSignals"]["Status"]})

    @app.route('/external/foglights/status/post', methods=['POST'])
    def set_external_foglights_status():
        light_status = request.json["Status"]
        if light_status not in [0, 1]:
            return jsonify({"Error": "Invalid Status"}), 400
        status["Lighting"]["External"]["FogLights"]["Status"] = light_status
        return jsonify({"FogLightsStatus": status["Lighting"]["External"]["FogLights"]["Status"]})

    @app.route('/external/foglights/status/get', methods=['GET'])
    def get_external_foglights_status():
        return jsonify({"FogLightsStatus": status["Lighting"]["External"]["FogLights"]["Status"]})
    
    









