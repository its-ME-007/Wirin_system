from threading import Thread
from flask import Flask, jsonify
from intlight import int_lighting_bp
from obc import obc_bp
from extlight import ext_lighting_bp  # Import the external lighting blueprint
from tablestat import table_bp  # Import the table status blueprint

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

def create_int_lighting_app():
    app = Flask(__name__)
    app.register_blueprint(int_lighting_bp)
    return app

def create_obc_app():
    app = Flask(__name__)
    app.register_blueprint(obc_bp)
    return app

def create_ext_lighting_app():
    app = Flask(__name__)
    app.register_blueprint(ext_lighting_bp)
    return app

def create_table_app():
    app = Flask(__name__)
    app.register_blueprint(table_bp)
    return app

def run_service(app, port):
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main_app = create_main_app()
    int_lighting_app = create_int_lighting_app()
    obc_app = create_obc_app()
    ext_lighting_app = create_ext_lighting_app()
    table_app = create_table_app()

    main_thread = Thread(target=run_service, args=(main_app, 5000))
    int_lighting_thread = Thread(target=run_service, args=(int_lighting_app, 5001))
    obc_thread = Thread(target=run_service, args=(obc_app, 5002))
    ext_lighting_thread = Thread(target=run_service, args=(ext_lighting_app, 5003))
    table_thread = Thread(target=run_service, args=(table_app, 5004))  # Added table service

    main_thread.start()
    int_lighting_thread.start()
    obc_thread.start()
    ext_lighting_thread.start()
    table_thread.start()  # Start the table service thread

    main_thread.join()
    int_lighting_thread.join()
    obc_thread.join()
    ext_lighting_thread.join()
    table_thread.join()  # Ensure the table service thread finishes
