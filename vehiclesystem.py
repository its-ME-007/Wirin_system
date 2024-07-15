from flask import Flask, jsonify, request
import threading

app = Flask(__name__)

# Define individual status variables for each component
door_status = "Closed"
boot_door_status = "Closed"
roof_door_status = "Closed"
car_mode = "ENTERTAINMENT_MODE"
steering_status = "Open"
acc_brake_pedal_status = "Open"
tv_state_level = "State1"
tv_status = "Moving Up"

# Define threading functions for each component
def vehicle_doors_thread():
    @app.route('/vehicledoors/door/open', methods=['POST'])
    def open_door():
        global door_status
        door_status = "Open"
        return f"DoorStatus is now Open", 200

    @app.route('/vehicledoors/door/close', methods=['POST'])
    def close_door():
        global door_status
        door_status = "Close"
        return f"DoorStatus is now Close", 200

    @app.route('/vehicledoors/door/opening', methods=['POST'])
    def opening_door():
        global door_status
        door_status = "Opening"
        return f"DoorStatus is now Opening", 200

    @app.route('/vehicledoors/door/closing', methods=['POST'])
    def closing_door():
        global door_status
        door_status = "Closing"
        return f"DoorStatus is now Closing", 200

    @app.route('/vehicledoors/door/error', methods=['POST'])
    def error_door():
        global door_status
        door_status = "Error"
        return f"DoorStatus is now Error", 200

    @app.route('/vehicledoors/door', methods=['GET'])
    def get_door_status():
        return door_status, 200

    @app.route('/vehicledoors/bootdoor/open', methods=['POST'])
    def open_boot_door():
        global boot_door_status
        boot_door_status = "Open"
        return f"BootDoorStatus is now Open", 200

    @app.route('/vehicledoors/bootdoor/close', methods=['POST'])
    def close_boot_door():
        global boot_door_status
        boot_door_status = "Close"
        return f"BootDoorStatus is now Close", 200

    @app.route('/vehicledoors/bootdoor/opening', methods=['POST'])
    def opening_boot_door():
        global boot_door_status
        boot_door_status = "Opening"
        return f"BootDoorStatus is now Opening", 200

    @app.route('/vehicledoors/bootdoor/closing', methods=['POST'])
    def closing_boot_door():
        global boot_door_status
        boot_door_status = "Closing"
        return f"BootDoorStatus is now Closing", 200

    @app.route('/vehicledoors/bootdoor/error', methods=['POST'])
    def error_boot_door():
        global boot_door_status
        boot_door_status = "Error"
        return f"BootDoorStatus is now Error", 200

    @app.route('/vehicledoors/bootdoor', methods=['GET'])
    def get_boot_door_status():
        return boot_door_status, 200

    @app.route('/vehicledoors/roofdoor/open', methods=['POST'])
    def open_roof_door():
        global roof_door_status
        roof_door_status = "Open"
        return f"RoofDoorStatus is now Open", 200

    @app.route('/vehicledoors/roofdoor/close', methods=['POST'])
    def close_roof_door():
        global roof_door_status
        roof_door_status = "Close"
        return f"RoofDoorStatus is now Close", 200

    @app.route('/vehicledoors/roofdoor/opening', methods=['POST'])
    def opening_roof_door():
        global roof_door_status
        roof_door_status = "Opening"
        return f"RoofDoorStatus is now Opening", 200

    @app.route('/vehicledoors/roofdoor/closing', methods=['POST'])
    def closing_roof_door():
        global roof_door_status
        roof_door_status = "Closing"
        return f"RoofDoorStatus is now Closing", 200

    @app.route('/vehicledoors/roofdoor/error', methods=['POST'])
    def error_roof_door():
        global roof_door_status
        roof_door_status = "Error"
        return f"RoofDoorStatus is now Error", 200

    @app.route('/vehicledoors/roofdoor', methods=['GET'])
    def get_roof_door_status():
        return roof_door_status, 200

def car_mode_thread():
    @app.route('/carmode/entertainment', methods=['POST'])
    def entertainment_mode():
        global car_mode
        car_mode = "ENTERTAINMENT_MODE"
        return f"Car mode is now ENTERTAINMENT_MODE", 200
    
    @app.route('/carmode/ambient', methods=['POST'])
    def ambient_mode():
        global car_mode
        car_mode = "AMBIENT_MODE"
        return f"Car mode is now AMBIENT_MODE", 200
    
    @app.route('/carmode/focus', methods=['POST'])
    def focus_mode():
        global car_mode
        car_mode = "FOCUS_MODE"
        return f"Car mode is now FOCUS_MODE", 200
    
    @app.route('/carmode/night', methods=['POST'])
    def night_mode():
        global car_mode
        car_mode = "NIGHT_MODE"
        return f"Car mode is now NIGHT_MODE", 200
    
    @app.route('/carmode/ride', methods=['POST'])
    def ride_mode():
        global car_mode
        car_mode = "RIDE_MODE"
        return f"Car mode is now RIDE_MODE", 200

    @app.route('/carmode', methods=['GET'])
    def get_car_mode():
        return car_mode, 200

def by_wire_system_thread():
    @app.route('/bywiresystem/steering/open', methods=['POST'])
    def open_steering():
        global steering_status
        steering_status = "Open"
        return f"SteeringStatus is now Open", 200

    @app.route('/bywiresystem/steering/close', methods=['POST'])
    def close_steering():
        global steering_status
        steering_status = "Close"
        return f"SteeringStatus is now Close", 200

    @app.route('/bywiresystem/steering/opening', methods=['POST'])
    def opening_steering():
        global steering_status
        steering_status = "Opening"
        return f"SteeringStatus is now Opening", 200

    @app.route('/bywiresystem/steering/closing', methods=['POST'])
    def closing_steering():
        global steering_status
        steering_status = "Closing"
        return f"SteeringStatus is now Closing", 200

    @app.route('/bywiresystem/steering/error', methods=['POST'])
    def error_steering():
        global steering_status
        steering_status = "Error"
        return f"SteeringStatus is now Error", 200

    @app.route('/bywiresystem/steering', methods=['GET'])
    def get_steering_status():
        return steering_status, 200

    @app.route('/bywiresystem/accbrake/open', methods=['POST'])
    def open_acc_brake():
        global acc_brake_pedal_status
        acc_brake_pedal_status = "Open"
        return f"AccBrakePedalStatus is now Open", 200

    @app.route('/bywiresystem/accbrake/close', methods=['POST'])
    def close_acc_brake():
        global acc_brake_pedal_status
        acc_brake_pedal_status = "Close"
        return f"AccBrakePedalStatus is now Close", 200

    @app.route('/bywiresystem/accbrake/opening', methods=['POST'])
    def opening_acc_brake():
        global acc_brake_pedal_status
        acc_brake_pedal_status = "Opening"
        return f"AccBrakePedalStatus is now Opening", 200

    @app.route('/bywiresystem/accbrake/closing', methods=['POST'])
    def closing_acc_brake():
        global acc_brake_pedal_status
        acc_brake_pedal_status = "Closing"
        return f"AccBrakePedalStatus is now Closing", 200

    @app.route('/bywiresystem/accbrake/error', methods=['POST'])
    def error_acc_brake():
        global acc_brake_pedal_status
        acc_brake_pedal_status = "Error"
        return f"AccBrakePedalStatus is now Error", 200

    @app.route('/bywiresystem/accbrake', methods=['GET'])
    def get_acc_brake_pedal_status():
        return acc_brake_pedal_status, 200

def tv_thread():
    @app.route('/tv/statelevel/state1', methods=['POST'])
    def state1_level():
        global tv_state_level
        tv_state_level = "State1"
        return f"TV state level is now State1", 200

    @app.route('/tv/statelevel/state2', methods=['POST'])
    def state2_level():
        global tv_state_level
        tv_state_level = "State2"
        return f"TV state level is now State2", 200

    @app.route('/tv/statelevel/state3', methods=['POST'])
    def state3_level():
        global tv_state_level
        tv_state_level = "State3"
        return f"TV state level is now State3", 200

    @app.route('/tv/statelevel', methods=['GET'])
    def get_tv_state_level():
        return tv_state_level, 200

    @app.route('/tv/status/movingup', methods=['POST'])
    def movingup_tv_status():
        global tv_status
        tv_status = "Moving Up"
        return f"TV status is now Moving Up", 200

    @app.route('/tv/status/movingdown', methods=['POST'])
    def movingdown_tv_status():
        global tv_status
        tv_status = "Moving Down"
        return f"TV status is now Moving Down", 200

    @app.route('/tv/status/state1', methods=['POST'])
    def state1_tv_status():
        global tv_status
        tv_status = "State1"
        return f"TV status is now State1", 200

    @app.route('/tv/status/state2', methods=['POST'])
    def state2_tv_status():
        global tv_status
        tv_status = "State2"
        return f"TV status is now State2", 200

    @app.route('/tv/status/state3', methods=['POST'])
    def state3_tv_status():
        global tv_status
        tv_status = "State3"
        return f"TV status is now State3", 200

    @app.route('/tv/status/error', methods=['POST'])
    def error_tv_status():
        global tv_status
        tv_status = "Error"
        return f"TV status is now Error", 200

    @app.route('/tv/status', methods=['GET'])
    def get_tv_status():
        return tv_status, 200

# Start the threads
thread_vehicle_doors = threading.Thread(target=vehicle_doors_thread)
thread_car_mode = threading.Thread(target=car_mode_thread)
thread_by_wire_system = threading.Thread(target=by_wire_system_thread)
thread_tv = threading.Thread(target=tv_thread)

thread_vehicle_doors.start()
thread_car_mode.start()
thread_by_wire_system.start()
thread_tv.start()

if __name__ == '__main__':
    app.run(debug=True)
