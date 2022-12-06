import asyncio

import websockets


async def handler(websocket, path):
    data = await websocket.recv()
    reply = f"Data recieved as:  {data}!"

    await websocket.send(reply)


def between_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    ws_server = websockets.serve(handler, 'localhost', 8899)

    loop.run_until_complete(ws_server)
    loop.run_forever()
    loop.close()