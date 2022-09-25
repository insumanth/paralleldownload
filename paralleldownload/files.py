from uuid import uuid4
import string
import itertools


# File Names

def get_uuid_filename(size: int, extension: str) -> list:
    return [f"{uuid4()}{extension or ''}" for val in range(size)]


def get_numeric_filename(size: int, extension: str) -> list:
    format_length = len(f"{size}")
    file_names = [f"{val:0{format_length}}{extension or ''}" for val in range(size)]
    return file_names


def get_alphabetic_filename(size: int, extension: str) -> list:
    repeat_value = None
    for exp in range(100):
        if size <= 26 ** exp:
            repeat_value = exp
            break
    print(f"Using : {repeat_value}")
    alphabet_tuple = itertools.product(string.ascii_lowercase, repeat=repeat_value)
    file_names = [f"{''.join(val)}{extension or ''}" for val in list(itertools.islice(alphabet_tuple, size))]
    return file_names


def get_filename_from_url(url_list: list) -> list:
    file_list = []
    for url in url_list:
        file_name = url.split("?")[0].split("/")[-1]
        file_list.append((file_name, url))
    return file_list


# Reading Files


def get_urls(file_path: str) -> list:
    url_list = []

    with open(file_path, "r") as fp:
        for url in fp:  # type: str
            url_list.append(url.strip())

    return url_list
