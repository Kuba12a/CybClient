import threading
import Console
import WebSockets.WebSocket as webSocket

if __name__ == '__main__':
    #code = cybServerGateway.generate_first_code_for_agent(cybServerGateway.GenerateFirstCodeForAgentInputType(
        #ip_address='192.168.1.50'))
    server = threading.Thread(target=webSocket.between_callback, daemon=True)
    server.start()

    Console.options()
    Console.menu()
    #time.sleep(200)
    #cybServerGateway.download_file_from_agent(cybServerGateway.DownloadFileFromAgentInputType(ip_address='192.168.1.50',
    #                                                                                          file_path='/etc/passwd'))
    #time.sleep(20)

    #cybServerGateway.list_files_from_agent(cybServerGateway.ListFilesFromAgentInputType(ip_address='192.168.1.50',
    #                                                                                          dir_path='/etc'))
    #time.sleep(20)
