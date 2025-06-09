import requests


#
def get_devices(api_key, access_token):
    url = "https://api.manage.trellix.com/epo/v2/devices"
    headers = {
        "Content-Type": "application/vnd.api+json",
        "x-api-key": api_key,
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


#
def create_investigation_edr(api_key, access_token, case_name, hostname):
    url = "https://api.manage.trellix.com/edr/v2/investigations"
    headers = {
        "Content-Type": "application/vnd.api+json",
        "x-api-key": api_key,
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "data": {
            "type": "investigations",
                "attributes": {
                "caseType": "Malware",
                "caseName": f"{case_name}",
                "caseHint": "hostname",
                "casePriority": "High",
                "evidenceType": "Device",
                "name": f"{hostname}",
                "hostName": f"{hostname}",
                }
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
