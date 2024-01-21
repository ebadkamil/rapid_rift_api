from pathlib import Path

import typer

from src.app.db.connection import Connector
from src.app.db.constants import DbTypes

app = typer.Typer()


@app.callback()
def set_context_object(
    ctx: typer.Context,
    db_type: DbTypes,
):
    ctx.obj = Connector(db_type)


@app.command()
def get_table_names(ctx: typer.Context):
    print(ctx.obj.get_table_names())


@app.command()
def create_tables_from_data_models(ctx: typer.Context):
    from sqlmodel import SQLModel

    from src.db_models import tables

    SQLModel.metadata.create_all(ctx.obj.engine)


@app.command()
def start_server(
    host: str = typer.Option(default="127.0.0.1", help="hostname"),
    port: int = typer.Option(default=8000, help="port number"),
):
    import uvicorn

    uvicorn.run("src.api.server_application:server", host=host, port=port, reload=True)


if __name__ == "__main__":
    app()
