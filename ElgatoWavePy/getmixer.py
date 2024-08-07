# library.py

import asyncio
import websockets
import json

# Fonction asynchrone pour gérer la connexion WebSocket
async def async_set_volume_input(websocket_url="ws://127.0.0.1", port="1824"):
    url = f"{websocket_url}:{port}"
    async with websockets.connect(url) as ws:
        message = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "getInputs",
        }
        await ws.send(json.dumps(message))
        message = await ws.recv()
        response = json.loads(message)
        if "params" in response:
            if "MixerList" in response["params"]:
                mixer_list = response["params"]["MixerList"]
                print("Identifiers received:")
                for mixer in mixer_list:
                    print(f"- {mixer['identifier']}")

def dumpInputs(websocket_url="ws://127.0.0.1", port="1824"):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(async_set_volume_input(websocket_url, port))
    finally:
        loop.close()

