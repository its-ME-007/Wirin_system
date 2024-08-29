from flask import Flask, jsonify, request

app = Flask(__name__)

# Define initial status dictionary
status = {
    "TableStat": {
        "tableheight": 0,
        "tablestatus": "Closed",
        "tablelamp": 0,
        "tablelampbrightness": 0
    }
}

# Function to check if a value is within the specified limits
def check_limits(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        return jsonify({"Error": f"{name} value {value} is out of range ({min_val} to {max_val})"}), 400
    return None

# Endpoint to set table height
@app.route('/Tablestatus/tableheight/post', methods=['POST'])
def table_height_post():
    data = request.json
    height = data.get("tableheight")
    if height is None:
        return jsonify({"Error": "tableheight not provided"}), 400
    error = check_limits(height, 0, 100, "tableheight")
    if error:
        return error
    status["TableStat"]["tableheight"] = height
    return jsonify({"tableheight": height}), 200

# Endpoint to get table height
@app.route('/Tablestatus/tableheight/get', methods=['GET'])
def table_height_get():
    return jsonify({"tableheight": status["TableStat"]["tableheight"]}), 200

# Endpoint to set table status
@app.route('/Tablestatus/table/post', methods=['POST'])
def table_post():
    data = request.json
    tablestatus = data.get("tablestatus")
    if tablestatus is None:
        return jsonify({"Error": "tablestatus not provided"}), 400
    if tablestatus not in ["Open", "Closed", "Opening", "Closing", "Error"]:
        return jsonify({"Error": "Invalid tablestatus value"}), 400
    status["TableStat"]["tablestatus"] = tablestatus
    return jsonify({"tablestatus": tablestatus}), 200

# Endpoint to get table status
@app.route('/Tablestatus/table/get', methods=['GET'])
def table_get():
    return jsonify({"tablestatus": status["TableStat"]["tablestatus"]}), 200

# Endpoint to set table lamp status
@app.route('/Tablestatus/tablelamp/post', methods=['POST'])
def table_lamp_post():
    data = request.json
    tablelamp = data.get("tablelamp")
    if tablelamp is None:
        return jsonify({"Error": "tablelamp not provided"}), 400
    if tablelamp not in [0, 1]:
        return jsonify({"Error": "Invalid tablelamp value, must be 0 (off) or 1 (on)"}), 400
    status["TableStat"]["tablelamp"] = tablelamp
    tablelamp_status = "on" if tablelamp == 1 else "off"
    return jsonify({"tablelamp": tablelamp, "tablelamp_status": tablelamp_status}), 200

# Endpoint to get table lamp status
@app.route('/Tablestatus/tablelamp/get', methods=['GET'])
def table_lamp_get():
    tablelamp_status = "on" if status["TableStat"]["tablelamp"] == 1 else "off"
    return jsonify({"tablelamp": status["TableStat"]["tablelamp"], "tablelamp_status": tablelamp_status}), 200

# Endpoint to set table lamp brightness
@app.route('/Tablestatus/tablelampbrightness/post', methods=['POST'])
def table_lamp_brightness_post():
    data = request.json
    brightness = data.get("tablelampbrightness")
    if brightness is None:
        return jsonify({"Error": "tablelampbrightness not provided"}), 400
    error = check_limits(brightness, 0, 100, "tablelampbrightness")
    if error:
        return error
    status["TableStat"]["tablelampbrightness"] = brightness
    return jsonify({"tablelampbrightness": brightness}), 200

# Endpoint to get table lamp brightness
@app.route('/Tablestatus/tablelampbrightness/get', methods=['GET'])
def table_lamp_brightness_get():
    return jsonify({"tablelampbrightness": status["TableStat"]["tablelampbrightness"]}), 200

if __name__ == '__main__':
    app.run(debug=True)
