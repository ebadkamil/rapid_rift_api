from pathlib import Path

import typer

from src.connectors.connection import Connector
from src.connectors.constants import DbTypes


app = typer.Typer()


@app.callback()
def set_context_object(
    ctx: typer.Context,
    db_type: DbTypes,
    authentication: Path = typer.Argument(
        ..., exists=True, file_okay=True, readable=True
    ),
):
    ctx.obj = Connector(db_type, authentication)


@app.command()
def get_table_names(ctx: typer.Context):
    print(ctx.obj.get_table_names())


@app.command()
def create_tables_from_data_models(ctx: typer.Context):
    from sqlmodel import SQLModel
    from src.db_models import tables

    SQLModel.metadata.create_all(ctx.obj.engine)


if __name__ == "__main__":
    app()