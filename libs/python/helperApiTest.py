import requests
import json
import logging
import sys
import os
from os.path import exists

log = logging.getLogger(__name__)

if not os.path.exists("./log"):
    os.mkdir("./log")

file_handler = logging.FileHandler(filename='./log/crossconsumption.log', mode='w')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s',
    handlers=handlers
)

def read_json_file(filepath):
    try:
        with open(filepath) as f:
            return json.load(f)
    except Exception as e:
        logging.exception(e)

def get_oauth_token(oauthurl, username, password):
    client_id = username
    client_secret = password
    payload = {
        "client_id": client_id, "client_secret": client_secret, "grant_type": "client_credentials"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    if oauthurl.endswith('/oauth/token') or oauthurl.endswith('/oauth/token?grant_type=client_credentials'):
        url = oauthurl
    elif oauthurl.endswith('auth/request'):
        url = oauthurl
        payload = json.dumps({
            "apiKey": client_id, "secret": client_secret
        })
        headers = {
            'Content-Type': 'application/json'
        }
    else:
        url = f"{oauthurl}/oauth/token"
    try:
        response = requests.post(url, headers=headers, data=payload)
        data = response.json()
        response.raise_for_status()
        if(response.status_code == 200):
            if data.get("access_token", False):
                access_token = data['access_token']
                return access_token
            else:
                access_token = data['accessToken']
                return access_token
    except requests.exceptions.HTTPError as errh:
        logging.exception(errh)
    except requests.exceptions.RequestException as err:
        logging.exception(err)

def get_api_req(uri, access_token):
    if not uri.startswith('https://'):
        uri = 'https://' + uri
    logging.info(f"The API request URL: {uri}")
    headers = {
        'Authorization': 'Bearer ' + access_token,
    }
    try:
        response = requests.get(uri, headers=headers)
        response.raise_for_status()
        if response.status_code in [200, 201, 204]:
            logging.info("GET request API call is successful!")
    except requests.exceptions.HTTPError as errh:
        logging.error("Failed the API request call")
        logging.exception(errh)
    except requests.exceptions.RequestException as err:
        logging.exception(err)

def get_api_req_basic(uri, username, password):
    if not uri.startswith('https://'):
        uri = 'https://' + uri
    logging.info(f"The API request URL: {uri}")
    try:
        response = requests.get(uri, auth=(username, password))
        response.raise_for_status()
        if response.status_code in [200, 201, 204]:
            logging.info("GET request API call is successful!")
    except requests.exceptions.HTTPError as errh:
        logging.exception(errh)
        logging.error("Failed the API request call")
    except requests.exceptions.RequestException as err:
        logging.exception(err)

def get_key_values(binding, pathKey):
    for key in pathKey.split("."):
        if key.isnumeric():
            key = int(key)
            binding = binding[key]
            continue
        binding = binding.get(key, False)
        if not binding:
            break
    return binding

def main():
    params = read_json_file('/home/user/usecases/inDevelopment/cross_consumption.json')
    data = params["api_resource_uri"]
    for i, d in enumerate(data):
        flag = True
        if d["authMethod"] == "basic":
            del d["oauthurlPathkey"]
        for k, v in d.items():
            if d[k] in [None, '', ' ']:
                logging.error(f"Please provide the value for '{k}' for '{d['servicename']}' service")
                flag = False
                break
        if flag:
            continue
        else:
            break
    if flag:
        for i, d in enumerate(data):
            logging.info("###### API TEST " + str(i) + " #######")
            logging.info(f"API test for {d['servicename']} service of plan {d['plan']}. Service ID: {d['serviceID']}")
            if d["APITest"] == "no":
                continue
            servicename = d['servicename']
            plan = d['plan']
            testapi = d['testapi']
            if testapi == '/':
                testapi = ''
            apiBaseUrlPathKey = d['apiBaseUrlPathKey']
            clientId_basicUN_PathKey = d['clientId_basicUN_PathKey']
            clientSecret_basicPW_PathKey = d['clientSecret_basicPW_PathKey']
            path = f"/home/user/logs/k8s/bindings/{servicename}-{plan}.json"
            file_exists = exists(path)
            if not file_exists:
                continue
            binding = read_json_file(path)
            if d['authMethod'] == "oauth":
                oauthurlPathkey = d['oauthurlPathkey']
                oauthurl = get_key_values(binding, oauthurlPathkey)
                uri = get_key_values(binding, apiBaseUrlPathKey)
                username = get_key_values(binding, clientId_basicUN_PathKey)
                password = get_key_values(binding, clientSecret_basicPW_PathKey)
                uri = f"{uri}{testapi}"
                access_token = get_oauth_token(oauthurl, username, password)
                get_api_req(uri, access_token)
            else:
                uri = get_key_values(binding, apiBaseUrlPathKey)
                username = get_key_values(binding, clientId_basicUN_PathKey)
                password = get_key_values(binding, clientSecret_basicPW_PathKey)
                uri = f"{uri}{testapi}"
                get_api_req_basic(uri, username, password)
    file_exists = exists("failedService.txt")
    if file_exists:
        file1 = open('failedService.txt', 'r')
        Lines = file1.readlines()
        for line in Lines:
            val = line.split(":")
            for d in data:
                if val[0] == d['servicename']:
                    serviceID = d['serviceID']
                    logging.error(f"{str(val[0])} service is not crossconsumable. Status : {str(val[1])} ServiceId : {serviceID}")


main()
