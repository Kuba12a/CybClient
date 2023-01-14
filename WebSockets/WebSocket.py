import asyncio
import websockets
import Console
import config


async def handler(websocket, path):
    data = await websocket.recv()
    Console.console.print('\n'+data)
    Console.console.print('>', end='')


def between_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    ws_server = websockets.serve(handler, config.web_socket_ip, config.web_socket_port)

    loop.run_until_complete(ws_server)
    loop.run_forever()
    loop.close()
