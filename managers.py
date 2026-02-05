from logging_config import get_logger

logger = get_logger(__name__)

class FileManager:
    def __init__(self, path: str, mode: str, encoding: str = "utf-8"):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.path, self.mode, encoding=self.encoding)
            return self.file
        except FileNotFoundError as e:
            logger.error(f"File not found: {self.path}")
            raise  
        except Exception as e:
            logger.exception("Failed to open file!")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.error(f"Error inside with-block: {exc_val}")

        if self.file:
            self.file.close()

        return False
