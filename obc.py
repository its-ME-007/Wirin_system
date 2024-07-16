from flask import Flask, jsonify, request
import threading
from datetime import datetime
import time
import Blueprint

app = Flask(__name__)

obc_bp = Blueprint('obc', __name__)
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


def obc_thread():
    @obc_bp.route('/obc/ac_voltage/get', methods=['GET'])
    def get_ac_voltage():
        return jsonify({"AC_Voltage": status["OBC"]["AC_Voltage"]})

    @obc_bp.route('/obc/ac_current/get', methods=['GET'])
    def get_ac_current():
        return jsonify({"AC_Current": status["OBC"]["AC_Current"]})

    @obc_bp.route('/obc/ac_power/get', methods=['GET'])
    def get_ac_power():
        return jsonify({"AC_Power": status["OBC"]["AC_Power"]})

    @obc_bp.route('/obc/charging_time/get', methods=['GET'])
    def get_charging_time():
        return jsonify({"Charging_Time": status["OBC"]["Charging_Time"]})

    @obc_bp.route('/obc/dc_voltage/get', methods=['GET'])
    def get_dc_voltage():
        return jsonify({"DC_Voltage": status["OBC"]["DC_Voltage"]})

    @obc_bp.route('/obc/dc_current/get', methods=['GET'])
    def get_dc_current():
        return jsonify({"DC_Current": status["OBC"]["DC_Current"]})

    @obc_bp.route('/obc/obc_temperature/get', methods=['GET'])
    def get_obc_temperature():
        return jsonify({"OBC_Temperature": status["OBC"]["OBC_Temperature"]})

    @obc_bp.route('/obc/obc_status/get', methods=['GET'])
    def get_obc_status():
        return jsonify({"OBC_Status": status["OBC"]["OBC_Status"]})