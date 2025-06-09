from fastapi import FastAPI
from api.mvsion import *
from api.helix import *

app = FastAPI()


#
@app.get("/")
def about():
    return {
        "server": "MXDR - SECDEVOPS - API",
        "developer":"Diogo Caldas"
        }


#
@app.get("/token")
def token(client_id, client_secret, scope):
    return get_token(client_id, client_secret, scope)


#
@app.get("/alerts")
def alerts(helix_id,client_id, client_secret, scope):
    token = get_token(client_id, client_secret, scope)
    return get_alerts(helix_id,token)


#
@app.get("/devices")
def devices(api_key,client_id, client_secret, scope):
    token = get_token(client_id, client_secret, scope)
    return get_devices(api_key,token['access_token'])


#
@app.get("/investigation")
def create_investigation(api_key,client_id, client_secret, scope, case_name,hostname):
    token = get_token(client_id, client_secret, scope)
    return create_investigation_edr(api_key,token['access_token'],case_name,hostname)