from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(webs: WebSocket):
      await webs.accept() 
    while True:
      raw_text = await webs.receive_text() 
      await webs.send_text(f'received data {raw_text}')
      
      
  # To test the code use, ws://localhost:8000/ws 
  #in postman