from flask import Flask, request, jsonify
import requests, json

app = Flask(__name__)

EXTERNAL_URL = "https://www.smcinsurance.com/central/centralcall/CallReqWithHeader"
HEADERS = {
    'User-Agent': "Mozilla/5.0",
    'Content-Type': "application/json",
    'origin': "https://www.smcinsurance.com",
    'referer': "https://www.smcinsurance.com/"
}

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "running"})

# GET route
@app.route('/vehicle/<vehicle_no>', methods=['GET'])
def vehicle_get(vehicle_no):
    payload = {"URL": "GetVaahanDetailsByVehicleNo", "Props": [vehicle_no], "Token": "awnish"}
    r = requests.post(EXTERNAL_URL, data=json.dumps(payload), headers=HEADERS)
    return jsonify(r.json())

# POST route
@app.route('/vehicle', methods=['POST'])
def vehicle_post():
    data = request.get_json()
    payload = {"URL": "GetVaahanDetailsByVehicleNo", "Props": [data.get("vehicle_no")], "Token": data.get("token","awnish")}
    r = requests.post(EXTERNAL_URL, data=json.dumps(payload), headers=HEADERS)
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
