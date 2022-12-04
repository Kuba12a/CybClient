import Gateways.CybServerGateway as cybServerGateway

if __name__ == '__main__':
    code = cybServerGateway.generate_first_code_for_agent(cybServerGateway.GenerateFirstCodeForAgentInputType(
        ip_address='192.168.1.50'))
    print(code)
    #cybServerGateway.download_file_from_agent(cybServerGateway.DownloadFileFromAgentInputType(ip_address='192.168.1.50',
    #                                                                                          file_path='/etc/passwd'))
