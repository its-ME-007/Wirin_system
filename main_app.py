from threading import Thread
from flask import Flask, jsonify, Blueprint
from intlight import int_lighting_bp
from obc import obc_bp


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
    return app

def create_obc_app():
    app = Flask(__name__)
    app.register_blueprint(obc_bp)
    return app


def run_service(app, port):
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main_app = create_main_app()
    lighting_app = create_lighting_app()
    obc_bp = create_obc_app()

    main_thread = Thread(target=run_service, args=(main_app, 5000))
    int_lighting_thread = Thread(target=run_service, args=(lighting_app, 5001))
    obc_thread = Thread(target=run_service, args=(obc_bp, 5002))

    main_thread.start()
    int_lighting_thread.start()
    obc_thread.start()

    main_thread.join()
    int_lighting_thread.join()
    obc_thread.join()