import asyncio
import threading
import time

import Gateways.CybServerGateway as cybServerGateway
import WebSockets.WebSocket as webSocket

if __name__ == '__main__':
    code = cybServerGateway.generate_first_code_for_agent(cybServerGateway.GenerateFirstCodeForAgentInputType(
        ip_address='192.168.1.50'))
    server = threading.Thread(target=webSocket.between_callback, daemon=True)
    server.start()

    time.sleep(200)
    #cybServerGateway.download_file_from_agent(cybServerGateway.DownloadFileFromAgentInputType(ip_address='192.168.1.50',
    #                                                                                          file_path='/etc/passwd'))
