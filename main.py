from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse

app = FastAPI()

clients = []

@app.get("/")
async def root():
    return JSONResponse({"message": "Servidor FastAPI funcionando!"})

@app.post("/post")
async def post_endpoint():
    return JSONResponse({"message": "funcionando"})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)  # type: ignore
    print("Cliente conectado")
    try:
        #testando
        while True:
            data = await websocket.receive_text()
            print(f"Recebido: {data}")
            await websocket.send_text(f"Servidor recebeu: {data}")
    except WebSocketDisconnect:
        clients.remove(websocket)  # type: ignore
        print("Cliente desconectado")
