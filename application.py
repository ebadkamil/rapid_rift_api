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


if __name__ == "__main__":
    app()
