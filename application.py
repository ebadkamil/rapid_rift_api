from pathlib import Path
import typer

from src.connectors.connection import Connector
from src.connectors.constants import DbTypes


app = typer.Typer()


@app.callback()
def main(ctx: typer.Context, db_type: str, authentication: Path = typer.Argument(..., exists=True, file_okay=True, readable=True)):
    ctx.obj = Connector(DbTypes[db_type.upper()], authentication)


@app.command()
def get_table_names(ctx: typer.Context):
    print(ctx.obj.get_table_names())


if __name__ == "__main__":
    app()