import csv
from exceptions import InvalidAgeError
from managers import FileManager
from logging_config import get_logger

logger = get_logger(__name__)

# read csv

def read_csv(path) -> list[dict]:
    try:
        with FileManager("data/users.csv","r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            return rows
    except ValueError("CSV file is empty") as e:
        logger.exception(f"{e}")
    
# 
    






