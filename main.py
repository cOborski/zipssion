"""Zipssion

Usage:
  zipssion.py <file> [--quiet | --verbose] [--path=<path>] [--zip | --7zip | --tar.gz]
  zipssion.py <file> [--quiet | --verbose] [--path=<path>] [--json | --text]
  zipssion.py (-h | --help)
  zipssion.py --version
  zipssion.py --quiet
  zipssion.py --verbose

Options:
  -h --help      show help text
  --version      show version
  --quiet        print less text
  --verbose      print more text
  --path=<path>  path to folder containing file [default: '/']

"""
from docopt import docopt
from pprint import pprint
import logging
import argparse
import pathlib
import shutil
import tempfile
import zipfile

def config_log():
    # Configure logging
    logging.basicConfig(level=logging.DEBUG)

    # Create a StreamHandler and set its log level to DEBUG
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter and attach it to the handler
    formatter = logging.Formatter('%(asctime)s \n %(name)s \n %(levelname)s \n %(message)s')
    console_handler.setFormatter(formatter)

    # Create a logger and add the console handler
    logger = logging.getLogger(__name__)
    logger.addHandler(console_handler)

    return logger

def view_files_content(filename):

    path = pathlib.Path(filename)
    logger.debug('Path:' + str(path))
    zip_path = path.stem + '.zip'
    logger.debug('Zip Path:' + str(zip_path))

    if (path.exists() and path.is_file()):
        shutil.copy(path, zip_path)

        logger.debug('Is the path a file?:' + 'true')
        file = zipfile.ZipFile(zip_path)
        file.printdir()

if __name__ == '__main__':
    VERSION = '0.1.0-alpha'

    logger = config_log()
    arguments = docopt(__doc__, version=VERSION)
    filename = arguments['--path'] + arguments['<file>']


    logger.debug('Filename:' + filename)
    view_files_content(filename)

    logger.debug(arguments)
