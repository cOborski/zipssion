import argparse
import pathlib
import shutil
import tempfile
import zipfile
from pprint import pprint

import magic
from rich import console, print
from typer import Argument, Typer

app = Typer()


@app.command()
def identify(files: list[str] = Argument(..., help="File paths to identify")):
    """
    Identifies the file type of provided files with incorrect extensions

    A bit longer description.

    Args:
        files (list[str]): A list of file paths to identify

    Returns:
        type: description

    Raises:
        FileNotFoundError: the file does not exist

    """

    for file_path in files:
        try:
            with open(file_path, "rb") as f:
                file_type = magic.from_buffer(f.read(2048))

            if file_type.startswith("ZIP archive"):
                with zipfile.ZipFile(file_path, "r") as z:
                    print(f"{file_path}: ZIP archive containing:")
                    for member in z.namelist():
                        Text.print(f"  - {member}")
            elif file_type.startswith("TAR archive"):
                with tarfile.open(file_path, "r") as tar:
                    print(f"{file_path}: TAR archive containing:")
                    for member in tar.getmembers():
                        print(f"  - {member.name}")
            else:
                print(
                    f"[bold green]Identified file type: {file_type}[/bold green]"
                )

        except FileNotFoundError:
            log.error(f"Error: File not found: {file_path}")

    # todo: return
