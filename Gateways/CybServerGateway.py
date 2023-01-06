from pydantic import BaseModel
import json
import requests
import Console

HTTP_PREFIX = "http://"
HOST = "192.168.1.51:80/internal"


class DownloadFileFromAgentInputType(BaseModel):
    ip_address: str
    file_path: str


class ListFilesFromAgentInputType(BaseModel):
    ip_address: str
    dir_path: str


class MonitorClipboardOnAgentInputType(BaseModel):
    ip_address: str
    duration: int


class GenerateFirstCodeForAgentInputType(BaseModel):
    ip_address: str


class DisconnectAgentInputType(BaseModel):
    ip_address: str


def download_file_from_agent(input: DownloadFileFromAgentInputType):

    data = json.dumps(input.__dict__)

    response = requests.post(url=HTTP_PREFIX+HOST+"/downloadFile", data=data)

    if response.status_code != 200:
        Console.console.print(f"Could not schedule downloading file from agent {input.ip_address}", style="error")
        Console.console.print(response.json()['detail'], style="error")
    else:
        Console.console.print(f'Task for downloading file from an agent scheduled successfully with id:'
                              f' {response.json()["command_id"]}', style="success")

    return response.json()


def list_files_from_agent(input: ListFilesFromAgentInputType):

    data = json.dumps(input.__dict__)

    response = requests.post(url=HTTP_PREFIX+HOST+"/listFiles", data=data)

    if response.status_code != 200:
        Console.console.print(f"Could not schedule listing files from agent {input.ip_address}", style="error")
        Console.console.print(response.json()['detail'], style="error")
    else:
        Console.console.print(f'Task for listing files from an agent scheduled successfully with id:'
                              f' {response.json()["command_id"]}',
                              style="success")

    return response.json()


def monitor_clipboard_on_agent(input: MonitorClipboardOnAgentInputType):

    data = json.dumps(input.__dict__)

    response = requests.post(url=HTTP_PREFIX+HOST+"/monitorClipboard", data=data)

    if response.status_code != 200:
        Console.console.print(f"Could not schedule monitoring clipboard on agent {input.ip_address}", style="error")
        Console.console.print(response.json()['detail'], style="error")
    else:
        Console.console.print(f'Task for monitoring clipboard on agent scheduled successfully with id:'
                              f' {response.json()["command_id"]}',
                              style="success")

    return response.json()


def generate_first_code_for_agent(input: GenerateFirstCodeForAgentInputType):

    data = json.dumps(input.__dict__)

    response = requests.post(url=HTTP_PREFIX+HOST+"/generateAgentCode", data=data)

    if response.status_code == 200:
        Console.console.print('Code generated successfully', style="success")

    return response.json()['code']


def disconnect_agent(input: DisconnectAgentInputType):

    data = json.dumps(input.__dict__)

    response = requests.post(url=HTTP_PREFIX+HOST+"/disconnectAgent", data=data)

    if response.status_code != 200:
        Console.console.print(f"Could not schedule disconnecting agent {input.ip_address}", style="error")
        Console.console.print(response.json()['detail'], style="error")
    else:
        Console.console.print(f'Task for disconnecting agent scheduled successfully with id:'
                              f' {response.json()["command_id"]}',
                              style="success")

    return response.json()


def list_agents():

    response = requests.get(url=HTTP_PREFIX+HOST+"/agents")

    if response.status_code == 200:
        return response.json()['agents']

    return None
