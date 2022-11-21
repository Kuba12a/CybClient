from pydantic import BaseModel
import json
import requests

HTTP_PREFIX = "http://"


class DownloadFileFromAgentInputType(BaseModel):
    host: str
    file_path: str


def download_file_from_agent(input: DownloadFileFromAgentInputType):

    data = json.dumps(input.__dict__)

    response = requests.post(url=HTTP_PREFIX+input.host, data=data)

    status_code = response.status_code
    return status_code
