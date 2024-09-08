from typer import Typer
from log import create_rich_logger
import identify_file_type

app = Typer()
VERSION = "0.1.0-alpha"
logger = create_rich_logger()

app.add_typer(identify_file_type.app, name="identify_file_type")

if __name__ == "__main__":
    app()