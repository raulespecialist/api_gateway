import requests
import sys
import time
from abc import ABC
from socket import socket


class BaseConnector(ABC):
    """
    Interface to connect to source_data API
    """
    def __init__(self, params):
        self.base_url = str('http://127.0.0.1:8001/api/v1/')
        self.params = params
        super().__init__()

    def url(self):
        return self.base_url

    def ip(self):
        return socket.gethostbyname(self.url())