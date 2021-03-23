import requests


# petition get
def generate_request_get(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()


# petition put
def generate_request_put(url, data):
    response = requests.put(url, data=data)

    if response.status_code == 200:
        return response.json()


# petition delete
def generate_request_delete(url):
    response = requests.delete(url)

    if response.status_code == 200:
        return response.json()


# petition post
def generate_request_post(url, data):
    response = requests.post(url, data=data)

    if response.status_code == 200:
        return response.json()


# get json clients
def get_clients(params={}):
    response = generate_request_get('http://127.0.0.1:8000/api/v1/client', params)
    if response:
        clients = response.get('results')
        return clients

    return ""


# delete request credit
def delete_request(pk=None):
    response = generate_request_delete(f'http://127.0.0.1:8000/api/v1/request/{pk}')
    if response:
        request = response.get('message')
        return request

    return ""


# put request credit
def put_request(pk=None, data={}):
    response = generate_request_put(f'http://127.0.0.1:8000/api/v1/request/{pk}', data)

    if response:
        request = response.get('results')
        return request

    return ""


# post request credit
def post_request(pk=None, data={}):
    response = generate_request_post(f'http://127.0.0.1:8000/api/v1/request/{pk}', data)

    if response:
        request = response.get('results')
        return request

    return ""
