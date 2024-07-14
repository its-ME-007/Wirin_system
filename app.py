from flask import Flask
from threading import Thread
import subprocess
from vehicledoors import vehicledoor_bp
from carmode import carmode_bp
from Tv import tv_bp
from bywiresystem import bywiresystem_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(vehicledoor_bp, url_prefix='/vehicledoor')
app.register_blueprint(carmode_bp, url_prefix='/carmode')
app.register_blueprint(tv_bp, url_prefix='/tv')
app.register_blueprint(bywiresystem_bp, url_prefix='/bywiresystem')

# Dummy global variables for demonstration
# Replace with actual implementations as per your application
door_status = "Closed"
car_mode = "ENTERTAINMENT_MODE"
tv_state_level = "State1"
tv_status = "Moving Up"
steering_status = "Open"
acc_brake_pedal_status = "Open"

# Dummy threading functions with subprocesses
def vehicledoor_thread():
    global door_status
    # Replace with actual subprocess logic as per your application
    subprocess.run(['python', 'vehicledoor_process.py'])

def carmode_thread():
    global car_mode
    # Replace with actual subprocess logic as per your application
    subprocess.run(['python', 'carmode_process.py'])

def tv_thread():
    global tv_state_level, tv_status
    # Replace with actual subprocess logic as per your application
    subprocess.run(['python', 'tv_process.py'])

def bywiresystem_thread():
    global steering_status, acc_brake_pedal_status
    # Replace with actual subprocess logic as per your application
    subprocess.run(['python', 'bywiresystem_process.py'])

# Start threads
threads = []
threads.append(Thread(target=vehicledoor_thread))
threads.append(Thread(target=carmode_thread))
threads.append(Thread(target=tv_thread))
threads.append(Thread(target=bywiresystem_thread))

for thread in threads:
    thread.start()

if __name__ == '__main__':
    app.run(debug=True)
    
