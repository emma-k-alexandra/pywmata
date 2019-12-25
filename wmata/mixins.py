from typing import Dict, Any
import requests
import requests.exceptions
from .error import WMATAError

class Fetcher:
    def fetch(self, url: str, params: Dict[str, str], api_key: str, output_class: Any):
        try:
            response = requests.get(
                url,
                params=params,
                headers={"api_key": api_key}
            )

        except requests.exceptions.RequestException as error:
            return WMATAError("Error while making request. {}".format(error))

        try:
            response_json = response.json()

        except ValueError as error:
            return WMATAError("Invalid JSON. {}".format(error))

        try:
            return output_class(response_json)

        except Exception as error:
            return WMATAError("Could not parse response json into object. {}".format(error))
