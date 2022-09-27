import requests
import json
import logging
import os
from typing import Dict, Optional
from libs.python.helperJson import getJsonFromFile

log = logging.getLogger(__name__)


class Constant:
    content_type = 'Content-Type'
    content_type_value = 'application/x-www-form-urlencoded'
    http_success_codes = [200, 201, 204]


class APITest:
    @staticmethod
    def get_oauth_token(oauthurl: str, username: str, password: str) -> str:
        """Returns oauth token for given details

        Args:
            oauthurl (str): Authentication URL
            username (str): Username or Client id for the oauth URL
            password (str): Password or Client secret

        Returns:
            str: OAuth Token
        """
        client_id = username
        client_secret = password
        payload = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }

        headers = {Constant.content_type: Constant.content_type_value}

        if oauthurl.endswith('/oauth/token') or oauthurl.endswith(
                '/oauth/token?grant_type=client_credentials'):
            url = oauthurl
        elif oauthurl.endswith('auth/request'):
            url = oauthurl
            payload = json.dumps({"apiKey": client_id, "secret": client_secret})
            headers = {'Content-Type': 'application/json'}
        else:
            url = f"{oauthurl}/oauth/token"

        try:
            response = requests.post(url, headers=headers, data=payload)
            data = response.json()
            response.raise_for_status()

            if response.status_code == 200:
                if data.get("access_token", False):
                    access_token = data['access_token']
                    return access_token
                else:
                    access_token = data['accessToken']
                    return access_token

        except requests.exceptions.HTTPError as errh:
            log.exception(errh)
        except requests.exceptions.RequestException as err:
            log.exception(err)

    @staticmethod
    def get_api_req(uri: str, **kwargs: Dict) -> None:
        """Validate successful API test

        Args:
            uri (str): Base URL
            kwargs: username, password, access_token
            username (str) : username for basic authentication
            password (str): password for basic authentication
            access_token (str): access token for OAuth
        """

        if not uri.startswith('https://'):
            uri = 'https://' + uri
        log.info(f"The API request URL: {uri}")

        if "access_token" in kwargs:
            params = {
                "headers": {
                    'Authorization': 'Bearer ' + kwargs["access_token"],
                }
            }
        else:
            params = {
                "auth": (kwargs["username"], kwargs["password"])
            }

        try:
            response = requests.get(uri, **params)
            response.raise_for_status()

            if response.status_code in Constant.http_success_codes:
                log.info("GET request API call is successful!")

        except requests.exceptions.HTTPError as errh:
            log.error("Failed the API request call")
            log.exception(errh)
        except requests.exceptions.RequestException as err:
            log.exception(err)

    @staticmethod
    def get_key_items(binding: Dict, pathKey: str) -> str:
        """
        Get key items for passed dict
        :param binding: Service key object
        :param pathKey: Key to be looking for
        :return: Value for the key in binding
        """
        for key in pathKey.split("."):
            if key.isnumeric():
                key = int(key)
                binding = binding[key]
                continue

            binding = binding.get(key, False)

            if not binding:
                break
        return binding

    def __call__(self, btp_usecase):
        self.btp_usecase = btp_usecase

        params = getJsonFromFile(self.btp_usecase.usecasefile)

        for _index, _service in enumerate(params["services"]):
            if "api_resource_uri" not in list(_service.keys()):
                continue

            api_resource_data = _service["api_resource_uri"]

            if api_resource_data["authMethod"] == "basic":
                del api_resource_data["oauthurlPathkey"]

            for _key, _value in api_resource_data.items():
                if api_resource_data[_key] in [None, '', ' ']:
                    log.error(
                        f"Please provide the value for '{_key}' for '{_service['name']}' service"
                    )
                    raise ValueError(f"Please provide the value for '{_key}' for '{_service['name']}' service")

            log.info(f"###### API TEST {_index} #######")
            log.info(
                f"API test for {_service['name']} service of plan {_service['plan']}. Service ID: {api_resource_data['serviceID']}"
            )

            if api_resource_data["APITest"] == "no":
                continue

            servicename = _service['name']
            plan = _service['plan']
            testapi = api_resource_data['testapi']

            if testapi == '/':
                testapi = ''

            api_base_url_path_key = api_resource_data['apiBaseUrlPathKey']
            client_id_basic_un_path_key = api_resource_data['clientId_basicUN_PathKey']
            client_secret_basic_pw_path_key = api_resource_data['clientSecret_basicPW_PathKey']

            path = f"/home/user/logs/k8s/bindings/{servicename}-{plan}.json"
            file_exists = os.path.exists(path)
            if not file_exists:
                continue
            binding = getJsonFromFile(path)

            if api_resource_data['authMethod'] == "oauth":
                oauthurlPathkey = api_resource_data['oauthurlPathkey']
                oauthurl = self.get_key_items(binding, oauthurlPathkey)
                uri = self.get_key_items(binding, api_base_url_path_key)
                username = self.get_key_items(binding, client_id_basic_un_path_key)
                password = self.get_key_items(binding, client_secret_basic_pw_path_key)
                uri = f"{uri}{testapi}"
                access_token = self.get_oauth_token(oauthurl, username, password)
                self.get_api_req(uri, access_token=access_token)
            else:
                uri = self.get_key_items(binding, api_base_url_path_key)
                username = self.get_key_items(binding, client_id_basic_un_path_key)
                password = self.get_key_items(binding, client_secret_basic_pw_path_key)
                uri = f"{uri}{testapi}"
                self.get_api_req(uri, username=username, password=password)
