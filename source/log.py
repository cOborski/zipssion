import logging

import rich_cli
from rich.logging import RichHandler


def create_rich_logger():
    """
    Create a logger that can be formatted using rich

    See https://rich.readthedocs.io/en/latest/logging.html?highlight=logging for
    more information on logging using rich or
    https://rich.readthedocs.io/en/latest/reference/logging.html#logging for
    for the rich.logging class definision

    Args:
        variable (type): description

    Returns:
        logger: a logger that can be formatted using rich

    Raises:
        Exception: description

    """

    # Create a formatter
    format = "%(asctime)s \n %(name)s \n %(levelname)s \n %(message)s"

    # Configure the logger to use the RichHandler
    logging.basicConfig(
        level=logging.DEBUG,
        format=format,
        handlers=[RichHandler()],
    )

    logger = logging.getLogger(__name__)

    logger.colors = {
        # todo: change to something colorblind safe
        "debug": "blue",
        "info": "green",
        "warning": "yellow",
        "error": "red",
        "critical": "bold red",
    }

    logger.debug(
        "[bold red]The rich logger has been created.[/]",
        extra={"markup": True},
    )
    logger.info("The rich logger has been created.")

    return logger
