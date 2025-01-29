import requests

def header_request(url,**headers):
    try:
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        raise Exception('Connection Error')

