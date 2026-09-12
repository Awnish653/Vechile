from fastapi import FastAPI
import requests, json

app = FastAPI()

EXTERNAL_URL = "https://www.smcinsurance.com/central/centralcall/CallReqWithHeader"
HEADERS = {
    'User-Agent': "Mozilla/5.0",
    'Content-Type': "application/json",
    'origin': "https://www.smcinsurance.com",
    'referer': "https://www.smcinsurance.com/"
}

@app.get("/")
def home():
    return {"status": "running", "message": "FastAPI on Vercel"}

@app.get("/vehicle/{vehicle_no}")
def vehicle(vehicle_no: str):
    payload = {"URL": "GetVaahanDetailsByVehicleNo", "Props": [vehicle_no], "Token": "awnish"}
    r = requests.post(EXTERNAL_URL, data=json.dumps(payload), headers=HEADERS)
    return r.json()
