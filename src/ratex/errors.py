from dataclasses import dataclass
import logging

logging.basicConfig(
    format = '%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt = '%Y-%m-%d:%H:%M:%S',
    level = logging.DEBUG
)

@dataclass
class Errors:
    def warning(msg: str) -> str:
        logging.warning(msg)
        return msg

    def critical(msg: str) -> str:
        logging.warning(msg)
        return msg