from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket) # type: ignore
    print("Cliente conectado")
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Recebido: {data}")
            await websocket.send_text(f"Servidor recebeu: {data}")
    except WebSocketDisconnect:
        clients.remove(websocket) # type: ignore
        print("Cliente desconectado")
