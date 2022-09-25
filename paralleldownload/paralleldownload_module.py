from .validate import validate_input_file, validate_save_directory, validate_process, get_valid_extension, \
    divide_into_nested_list, status_code_desc
from .files import get_urls, get_uuid_filename, get_numeric_filename, get_alphabetic_filename

from pathlib import Path
from multiprocessing import Pool
import requests
import json


def parallel_download(args):
    url_file = args.url_file
    save_directory = args.save_directory
    process = args.process
    uuid = args.uuid
    number = args.number
    alphabet = args.alphabet
    silent = args.silent
    debug = args.debug

    if debug:
        print_args(args)

    print("Checking options")

    extension = get_valid_extension(args.extension)

    file_exists, file_readable = validate_input_file(url_file)
    dir_exists, dir_writeable = validate_save_directory(save_directory)
    process_ok = validate_process(process)

    status = None

    if not all([file_exists, file_readable, dir_exists, dir_writeable, process_ok]):
        print("Options invalid")
        print_errors(args,
                     file_exists=file_exists, file_readable=file_readable,
                     dir_exists=dir_exists, dir_writeable=dir_writeable,
                     process_ok=process_ok
                     )
    else:
        print("Options are valid")
        print("Preparing download")
        url_list = get_urls(url_file)
        save_path = Path(save_directory).absolute().as_posix()
        rename_if_possible = True
        download_nodes = []

        if not url_list:
            print_errors(args, file_empty=bool(url_list))
        else:

            urls_size = len(url_list)
            file_name_list = []
            if uuid:
                file_name_list = get_uuid_filename(urls_size, extension)
                rename_if_possible = False
            elif number:
                file_name_list = get_numeric_filename(urls_size, extension)
                rename_if_possible = False
            elif alphabet:
                file_name_list = get_alphabetic_filename(urls_size, extension)
                rename_if_possible = False
            else:
                file_name_list = get_uuid_filename(urls_size, extension)

            for url, file in zip(url_list, file_name_list):
                download_nodes.append({
                    "url": url,
                    "file": file,
                    "dir": save_path,
                    "flags": (rename_if_possible, silent, debug),
                })

            args_list = divide_into_nested_list(download_nodes, process)

            print(f"Distributing work to {process} Process")
            status = download_using_multiprocessing(args_list)
            print_failed_urls(status)

    return status


def print_args(args):
    try:
        args_dict = args.__dict__
        print(json.dumps(args_dict, indent=2))
    except:
        print(args_dict)


def print_failed_urls(failed_nested_list):
    for process_list in failed_nested_list:  # type: list
        for failed_node in process_list:  # type: dict

            url = failed_node['url']
            rename, silent, debug = failed_node['flags']

            status_code = f"{failed_node.get('status_code', 'Unknown')}"
            status_code_category = status_code_desc.get(f"{status_code[:1]}xx", "Unknown")
            status_code_detail = status_code_desc.get(status_code, "Unknown")
            status_code_description = f"The URL {url} failed due to {status_code_category}, The Status code is {status_code} - {status_code_detail}"

            failed_node.pop('file', '')
            failed_node.pop('dir', '')
            failed_node.pop('flags', '')

            if debug:
                try:
                    failed_node['header'] = dict(failed_node['header'])
                    failed_node['body'] = failed_node['body'].decode()
                    failed_node['status_code_description'] = status_code_description
                    print(json.dumps(failed_node, indent=2))
                except:
                    print(status_code_description, failed_node)

            else:
                print(status_code_description)


def print_errors(args, **kwargs):
    print(args, kwargs)

    error_message = {
        "file_exists": f"The File ({args.url_file}) does not exists. Please provide a valid file name / file path",
        "file_readable": f"The File ({args.url_file}) is not readable. Please provide a valid permission before using",
        "dir_exists": f"The Directory / Folder ({args.url_file}) does not exists. Please provide a valid path",
        "dir_writeable": f"The Directory / Folder ({args.url_file}) is not writeable. Please provide a valid permission before using",
        "process_ok": f"The Process mentioned ({args.process}) does not fall in the range 0 < process < 120",
        "file_empty": f"The File ({args.url_file}) is Empty"
    }

    for key, val in kwargs.items():
        if not val:
            print(error_message.get(key))


def download_using_multiprocessing(args_list: list):
    status_list = []
    process_count = len(args_list)
    with Pool(process_count) as process:
        dist_work = process.imap_unordered(download, args_list)
        for status in dist_work:
            status_list.append(status)
    return status_list





def download(download_nodes: list) -> list:
    failed_nodes = []
    # directory remains same for all urls.
    directory = download_nodes[0]['dir']
    for nodes in download_nodes:

        url, file_name = nodes['url'], nodes['file']
        rename, silent, debug = nodes['flags']

        response = requests.get(url, allow_redirects=True, stream=True)

        if response and response.status_code == 200:
            if rename:
                file_name = f"{file_name}"

            full_file_path = f"{directory}/{file_name}"

            with open(full_file_path, "wb") as fp:
                fp.write(response.content)

            if not silent:
                print(f"Download Successful for : {file_name}")
        else:
            nodes['status_code'] = response.status_code

            if debug:
                nodes['header'] = response.headers
                nodes['body'] = response.content

            failed_nodes.append(nodes)
        # end if

    return failed_nodes


def get_file_name_from_response(name):
    pass
