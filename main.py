import csv
from exceptions import InvalidAgeError
from managers import FileManager
from logging_config import get_logger

logger = get_logger(__name__)


def read_csv(path: str) -> list[dict]:
    try:
        with FileManager(path, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        if not rows:
            raise ValueError("CSV file is empty")

        return rows

    except FileNotFoundError as e:
        logger.error(f"CSV file not found: {path} | {e}")
        raise
    except PermissionError as e:
        logger.error(f"No permission to read: {path} | {e}")
        raise


def validate_rows(path: str) -> list[dict]:
    rows = read_csv(path)
    out: list[dict] = []

    for i, row in enumerate(rows, start=1):
        try:
            # name check
            name = (row.get("name") or "").strip()
            if not name:
                raise ValueError(f"name is empty (row={i})")

            # id and age int
            row_id = int(row.get("id"))
            age = int(row.get("age"))

            if age < 0:
                raise InvalidAgeError(f"Age cannot be negative (row={i}, age={age})")

            city = (row.get("city") or "").strip()

            cleaned = {
                "id": row_id,
                "name": name,
                "age": age,
                "city": city,
            }
            out.append(cleaned)

            logger.info(f"Valid row={i} name={name} age={age}")

        except (ValueError, TypeError) as e:
            logger.warning(f"Invalid row={i}: {e} | raw={row}")
        except InvalidAgeError as e:
            logger.error(f"{e} | raw={row}")
            

    return out


validate_rows("data/users.csv")


    
    






