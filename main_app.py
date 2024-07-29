from threading import Thread
from flask import Flask, jsonify
from intlight import int_lighting_bp
from obc import obc_bp
from extlight import ext_lighting_bp
from cardata1 import cardata1_bp
from cardata2 import cardata2_bp
from cardata3 import cardata3_bp
from cardata4 import cardata4_bp, update_globalclock
from tablestat import table_bp
from llc import control_settings_bp
from pidstatus import pid_status_bp
from masterpid import master_pid_values_bp

def create_main_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to the Modular Request Resolver API",
            "endpoints": [
                "Prototype"
            ]
        })

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"error": "Page not found"}), 404

    return app

def create_lighting_app():
    app = Flask(__name__)
    app.register_blueprint(int_lighting_bp)
    app.register_blueprint(ext_lighting_bp)
    return app

def create_obc_app():
    app = Flask(__name__)
    app.register_blueprint(obc_bp)
    return app

def create_cardata_app():
    app = Flask(__name__)
    app.register_blueprint(cardata1_bp)
    app.register_blueprint(cardata2_bp)
    app.register_blueprint(cardata3_bp)
    app.register_blueprint(cardata4_bp)
    return app

def create_controlsettings_app():
    app = Flask(__name__)
    app.register_blueprint(control_settings_bp)
    app.register_blueprint(master_pid_values_bp)
    app.register_blueprint(pid_status_bp)

def create_table_app():
    app = Flask(__name__)
    app.register_blueprint(table_bp)
    return app

def run_service(app, port):
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    # Create all the Flask applications
    main_app = create_main_app()
    lighting_app = create_lighting_app()  # Combined lighting application
    obc_app = create_obc_app()
    cardata_app = create_cardata_app()
    table_app = create_table_app()
    control_setting_app = create_controlsettings_app()

    # Start services on specific ports
    main_thread = Thread(target=run_service, args=(main_app, 5000))        # Main app on port 5000
    lighting_thread = Thread(target=run_service, args=(lighting_app, 5001))  # Combined lighting on port 5001
    obc_thread = Thread(target=run_service, args=(obc_app, 5002))          # OBC on port 5002
    cardata_thread = Thread(target=run_service, args=(cardata_app, 5003)) # Cardata1 on port 5003
    table_thread = Thread(target=run_service, args=(table_app, 5004))      # Table statistics on port 5007
    control_thread = Thread(target=run_service, args = (control_setting_app, 5005))
    globalclock_thread = Thread(target=update_globalclock)                # Global clock (no port)

    # Start all threads
    main_thread.start()
    lighting_thread.start()
    obc_thread.start()
    cardata_thread.start()
    table_thread.start()
    control_thread.start()
    globalclock_thread.start()

    # Ensure all threads finish
    main_thread.join()
    lighting_thread.join()
    obc_thread.join()
    cardata_thread.join()
    table_thread.join()
    globalclock_thread.join()
    control_thread.join()
