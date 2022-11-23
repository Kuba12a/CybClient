import Gateways.CybServerGateway as cybServerGateway

if __name__ == '__main__':
    cybServerGateway.download_file_from_agent(cybServerGateway.DownloadFileFromAgentInputType(host='192.168.1.50',
                                                                                              file_path='/etc/passwd'))
