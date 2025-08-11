import asyncio
import websockets

async def hello():
    uri = "wss://echo.websocket.org"  # echo server
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello WebSocket!")
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(hello())
