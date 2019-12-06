"""Errors from the WMATA API
"""
class WMATAError:
    """An error from the WMATA API
    """
    message: str

    def __init__(self, message: str):
        self.message = message
