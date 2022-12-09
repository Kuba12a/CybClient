from pydantic import BaseModel
import json
import requests

HTTP_PREFIX = "http://"
HOST = "192.168.1.51:80/internal"


class DownloadFileFromAgentInputType(BaseModel):
    ip_address: str
    file_path: str


class ListFilesFromAgentInputType(BaseModel):
    ip_address: str
    dir_path: str


class GenerateFirstCodeForAgentInputType(BaseModel):
    ip_address: str


def download_file_from_agent(input: DownloadFileFromAgentInputType):

    data = json.dumps(input.__dict__)

    response = requests.post(url=HTTP_PREFIX+HOST+"/downloadFile", data=data)

    return response.json()


def list_files_from_agent(input: ListFilesFromAgentInputType):

    data = json.dumps(input.__dict__)

    response = requests.post(url=HTTP_PREFIX+HOST+"/listFiles", data=data)

    return response.json()


def generate_first_code_for_agent(input: GenerateFirstCodeForAgentInputType):

    data = json.dumps(input.__dict__)

    response = requests.post(url=HTTP_PREFIX+HOST+"/generateAgentCode", data=data)

    return response.json()['code']
