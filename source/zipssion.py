# to delete

import argparse
import pathlib
import shutil
import tempfile
import zipfile

parser = argparse.ArgumentParser()

parser.add_argument("filename")
args = parser.parse_args()

print(args.filename)

"""
def view_files_content(filename):

    path = pathlib.Path(filename)
    print(path)
    zip_path = path.stem + ".zip"
    print(zip_path)

    if path.exists() and path.is_file():
        shutil.copy(path, zip_path)

        print(path.is_file())
        file = zipfile.ZipFile(zip_path)
        file.printdir()


view_files_content(args.filename)
"""


def view_zip_files_content(filename):

    path = pathlib.Path(filename)
    logger.debug("Path:" + str(path))
    zip_path = path.stem + ".zip"
    logger.debug("Zip Path:" + str(zip_path))

    if path.exists() and path.is_file():
        shutil.copy(path, zip_path)

        logger.debug("Is the path a file?:" + "true")
        file = zipfile.ZipFile(zip_path)
        file.printdir()
    # ENDIF


# ENDDEF
