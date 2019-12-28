from typing import Dict, Any
from .utils import to_snake_case

class Response:
    def __init__(self, json: Dict[str, Any]):
      for key, value in json.items():
            setattr(self, to_snake_case(key), value)  
