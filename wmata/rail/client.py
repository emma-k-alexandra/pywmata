"""For interacting with MetroRail endpoints
"""

class MetroRail:
    """Main object for interacting with MetroRail API methods
    """
    key: str

    def __init__(self, key: str):
        self.key = key
