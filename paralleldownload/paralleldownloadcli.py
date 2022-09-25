import argparse
from time import time
from .paralleldownload_module import parallel_download
from .misc import info, version_info, simple_example, detailed_example



from .__init__ import VERSION, CORE_COUNT


def start():
    parser = argparse.ArgumentParser(
        usage="%(prog)s url_file [save_directory] [options]",
        formatter_class=argparse.RawTextHelpFormatter,
        description="Parallel Fast Downloader",
        epilog=simple_example,
        add_help=False,
    )

    # TODO
    # https://docs.python.org/3/library/argparse.html#nargs
    parser.add_argument(
        "url_file",
        help="Text file containing the URLs of the files to be downloaded. One URL per file",
    )

    parser.add_argument(
        "save_directory",
        help="The directory to be used to save the downloaded files. [default: %(default)s (Current Directory)]",
        nargs="?",
        default="."
    )

    parser.add_argument(
        "-p",
        "--process",
        help=f"Parallel Process to use when downloading the files. [default: %(default)s (CPU Core count in the machine)]",
        type=int,
        default=CORE_COUNT
    )

    parser.add_argument(
        "-e",
        "--extension",
        help="Manually specify the Extension to use.",
    )

    file_name_group = parser.add_mutually_exclusive_group()

    file_name_group.add_argument(
        "-u",
        "--uuid",
        help="Use UUID string as the file name",
        action='store_true',
    )

    file_name_group.add_argument(
        "-n",
        "--number",
        help="Use sequential Numbers as the file name",
        action='store_true',
    )

    file_name_group.add_argument(
        "-a",
        "--alphabet",
        help="Use sequential Alphabets as the file name",
        action='store_true',
    )



    misc_parser = parser.add_argument_group('help', 'Help, Logs and Info Options')

    misc_parser.add_argument(
        "-s",
        "--silent",
        help="Don't print Verbose Logs. Print only essential information",
        action='store_true',
    )

    misc_parser.add_argument(
        "-d",
        "--debug",
        help="Print detailed information. Helpful when debugging issues.",
        action='store_true',
    )

    misc_parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="Show this help message and exit"
    )

    misc_parser.add_argument(
        "-v",
        "--version",
        help="Prints Version information of the Package",
        action="version",
        version=version_info,
    )

    misc_parser.add_argument(
        "-i",
        "--info",
        action='version',
        help="Prints Information about the Package",
        version=info,
    )

    misc_parser.add_argument(
        "-eg",
        "--example",
        action='version',
        help="Prints more Example which helps to use this tool",
        version=detailed_example,
    )

    print("Parsing arguments")
    args = parser.parse_args()


    start_time = time()
    status = parallel_download(args)
    end_time = time()

    print(f"The Operation completed in {end_time - start_time :.5f} Seconds.")

