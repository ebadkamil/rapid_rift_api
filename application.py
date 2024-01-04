from pathlib import Path
import typer

from src.connectors.connection import Connector
from src.connectors.constants import DbTypes


app = typer.Typer()


@app.command()
def get_table_names(db_type: str, authentication: Path = typer.Argument(..., exists=True, file_okay=True, readable=True)):
    conn = Connector(DbTypes.ORACLE, authentication)
    print(conn.get_table_names())


if __name__ == "__main__":
    app()