"""MetroRail Line related structures
"""
from typing import Optional
from enum import Enum

class RequiresLine:
    """Methods that require a Line to function
    """
    def stations_on(self, line: Optional[Line], api_key: str):
        pass


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