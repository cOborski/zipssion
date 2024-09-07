from typer import Typer
import identify_file_type

app = Typer()
VERSION = "0.1.0-alpha"

app.add_typer(identify_file_type.app, name="identify_file_type")
