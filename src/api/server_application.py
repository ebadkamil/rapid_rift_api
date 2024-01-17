from fastapi import FastAPI

server = FastAPI()


@server.get("/")
async def root():
    return {"message": "Hello World"}
