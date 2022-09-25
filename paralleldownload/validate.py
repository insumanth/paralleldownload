import os
from pathlib import Path


def validate_input_file(path: str) -> tuple:
    file_path = Path(path)
    file_exists = False
    file_readable = False
    if file_path.exists() and file_path.is_file():
        file_exists = True

    if os.access(path, os.R_OK):
        file_readable = True

    return file_exists, file_readable


def validate_save_directory(path: str) -> tuple:
    directory_path = Path(path)
    directory_exists = False
    directory_writeable = False
    if directory_path.exists() and directory_path.is_dir():
        directory_exists = True

    if os.access(path, os.W_OK | os.X_OK):
        directory_writeable = True

    return directory_exists, directory_writeable


def validate_process(process: int) -> bool:
    if 0 < process < 120:
        return True
    else:
        return False


def get_valid_extension(extension: str) -> str:
    if extension:
        # Taking only first 20 characters of the extension string.
        extension = extension[:20].strip()
        if extension[0] != ".":
            valid_extension = f".{extension}"
        else:
            valid_extension = extension
    else:
        valid_extension = None

    return valid_extension


def divide_into_nested_list(total_list: list, split_count: int) -> list:
    k = split_count
    n = len(total_list)
    nested_list = [total_list[i * (n // k) + min(i, n % k):(i + 1) * (n // k) + min(i + 1, n % k)] for i in range(k)]
    return nested_list



status_code_desc = {
        "1xx": "Informational",
        "100": "Continue",
        "101": "Switching Protocols",
        "102": "Processing (WebDAV)",
        "2xx": "Success",
        "200": "OK",
        "201": "Created",
        "202": "Accepted",
        "203": "Non-Authoritative Information",
        "204": "No Content",
        "205": "Reset Content",
        "206": "Partial Content",
        "207": "Multi-Status (WebDAV)",
        "208": "Already Reported (WebDAV)",
        "226": "IM Used",
        "3xx": "Redirection",
        "300": "Multiple Choices",
        "301": "Moved Permanently",
        "302": "Found",
        "303": "See Other",
        "304": "Not Modified",
        "305": "Use Proxy",
        "306": "(Unused)",
        "307": "Temporary Redirect",
        "308": "Permanent Redirect (experimental)",
        "4xx": "Client Error",
        "400": "Bad Request",
        "401": "Unauthorized",
        "402": "Payment Required",
        "403": "Forbidden",
        "404": "Not Found",
        "405": "Method Not Allowed",
        "406": "Not Acceptable",
        "407": "Proxy Authentication Required",
        "408": "Request Timeout",
        "409": "Conflict",
        "410": "Gone",
        "411": "Length Required",
        "412": "Precondition Failed",
        "413": "Request Entity Too Large",
        "414": "Request-URI Too Long",
        "415": "Unsupported Media Type",
        "416": "Requested Range Not Satisfiable",
        "417": "Expectation Failed",
        "418": "I'm a teapot (RFC 2324)",
        "420": "Enhance Your Calm (Twitter)",
        "422": "Unprocessable Entity (WebDAV)",
        "423": "Locked (WebDAV)",
        "424": "Failed Dependency (WebDAV)",
        "425": "Reserved for WebDAV",
        "426": "Upgrade Required",
        "428": "Precondition Required",
        "429": "Too Many Requests",
        "431": "Request Header Fields Too Large",
        "444": "No Response (Nginx)",
        "449": "Retry With (Microsoft)",
        "450": "Blocked by Windows Parental Controls (Microsoft)",
        "451": "Unavailable For Legal Reasons",
        "499": "Client Closed Request (Nginx)",
        "5xx": "Server Error",
        "500": "Internal Server Error",
        "501": "Not Implemented",
        "502": "Bad Gateway",
        "503": "Service Unavailable",
        "504": "Gateway Timeout",
        "505": "HTTP Version Not Supported",
        "506": "Variant Also Negotiates (Experimental)",
        "507": "Insufficient Storage (WebDAV)",
        "508": "Loop Detected (WebDAV)",
        "509": "Bandwidth Limit Exceeded (Apache)",
        "510": "Not Extended",
        "511": "Network Authentication Required",
        "598": "Network read timeout error",
        "599": "Network connect timeout error",
    }

