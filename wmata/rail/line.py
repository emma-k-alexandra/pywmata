"""MetroRail Line related structures
"""
from typing import Optional, Union
from enum import Enum
from ..error import WMATAError
import responses
from urls import URLs
import requests
import requests.exceptions

class Line(Enum):
    """A MetroRail Line
    """
    Red = "RD"
    Blue = "BL"
    Yellow = "YL"
    YellowLineRushPlus = "YLRP"
    Orange = "OR"
    Green = "GR"
    Silver = "SV"

class RequiresLine:
    """Methods that require a Line to function
    """
    def stations_on(self, line: Optional[Line], api_key: str) -> Union[responses.Stations, WMATAError]:
        """Stations on the given line
        
        Arguments:
            line {Optional[Line]} -- Optional Line to get stations along
            api_key {str} -- API Key to make this request with
        
        Returns:
            Union[responses.Stations, WMATAError] -- Response from WMATA API, either {}
        """
        params = {}

        if line:
            params["line"] = line.name

        try:
            response = requests.get(
                URLs.Stations,
                params=params,
                headers={
                    "api_key": api_key
                }
            )
        except requests.exceptions.RequestException:
            return WMATAError("Error while making request")

        try:
            response_json = response.json()

        except ValueError:
            return WMATAError("Invalid JSON")

        try:
            return responses.Stations(response_json)

        except: # TODO: Yeah
            return WMATAError("Could not parse response json into object")

        
