import requests

# GERA O TOKEN COM BASE NO SCOPO
def get_token(client_id, client_secret, scope):
    credentials = (client_id,client_secret)

    url = "https://auth.trellix.com/auth/realms/IAM/protocol/openid-connect/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "client_credentials",
        "scope": scope
    }

    response = requests.post(url, headers=headers, data=data, auth=credentials)

    if response.status_code == 200:
        # return response.json().get("access_token")
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"


# PEGAR ALERTAS HELIX
def get_alerts(helix_id,token):
    access_token = token['access_token']
    scope = token['scope']
    
    url = f'https://apps.fireeye.com/helix/id/{helix_id}/api/v1/alerts/'

    headers = {
        "accept": "application/json",
        "x-trellix-api-token": f'Bearer {access_token}'
    }

    res = requests.get(url,headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        return res.json()
    

