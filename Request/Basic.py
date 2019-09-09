import requests
import unittest

class Basic(unittest.TestCase):
    header=None
    def __init__(self,header=None):
        Basic.header=header

    def get(self,url):
        try:
            response = requests.get(url,headers=Basic.header)
            return response
        except Exception as e:
            self.fail(response.status_code+e)

    def post(self, url, body):
        try:
            response = requests.post(url, headers=None, json=body)
            return response.json()
        except Exception as e:
            self.fail(response.status_code+e)



    def post_without_header_body(self, url):
        try:
            response = requests.post(url)
            return response.json()
        except Exception as e:
            self.fail(response.status_code+response.status_code+e)



