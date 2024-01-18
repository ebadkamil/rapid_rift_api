from fastapi import FastAPI

from src.db_models.constants import Status

server = FastAPI()


@server.get("/")
async def root():
    return {"message": "Production Line Overview"}


@server.get("/production_line/{line_number}")
async def get_status(line_number: int):
    return {"line_number": line_number}


@server.get("/status/{status}")
async def get_status(status: Status):
    return {"status": status}
