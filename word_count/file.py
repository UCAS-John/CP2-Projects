from timestamp import get_time

def word_count(data: str) -> int:
    return len(data.split())

def load(path: str) -> str:
    data = ""
    try:
        with open(path, "r") as file:
            data = file.read()
    except FileNotFoundError:
        print("File doesn't exists")

    return data

def insert_word_count(path: str) -> None:
    pass