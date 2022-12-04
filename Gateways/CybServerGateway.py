from pydantic import BaseModel
import json
import urllib.request
import urllib.parse

HTTP_PREFIX = "http://"
HOST = "192.168.1.51:80/internal"


class DownloadFileFromAgentInputType(BaseModel):
    ip_address: str
    file_path: str


class GenerateFirstCodeForAgentInputType(BaseModel):
    ip_address: str


def download_file_from_agent(input: DownloadFileFromAgentInputType):

    data = input.__dict__
    url = HTTP_PREFIX + HOST + "/downloadFile"

    request = urllib.request.Request(url, method='POST', data=urllib.parse.urlencode(data).encode())
    response = urllib.request.urlopen(request)

    response_data = response.read()

    return response_data


def generate_first_code_for_agent(input: GenerateFirstCodeForAgentInputType):

    data = input.__dict__
    url = HTTP_PREFIX + HOST + "/generateAgentCode"

    request = urllib.request.Request(url, method='POST',  data=urllib.parse.urlencode(data).encode())
    response = urllib.request.urlopen(request)

    response_data = response.read()

    return response_data
