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
    return jsonify({"status": "running", "message": "Flask API on Vercel"})

@app.route('/vehicle/<vehicle_no>', methods=['GET'])
def vehicle(vehicle_no):
    payload = {"URL": "GetVaahanDetailsByVehicleNo", "Props": [vehicle_no], "Token": "awnish"}
    r = requests.post(EXTERNAL_URL, data=json.dumps(payload), headers=HEADERS)
    return jsonify(r.json())
