import logging

logging.getLogger("httpx").setLevel(logging.WARNING)

logging.basicConfig(
    level=logging.INFO,
    format=(
        "\n"
        "Time: %(asctime)s\n"
        "Module: %(name)s\n"
        "Level: %(levelname)s\n"
        "Message: %(message)s\n"
    ),
)

app_logger = logging.getLogger("app")
