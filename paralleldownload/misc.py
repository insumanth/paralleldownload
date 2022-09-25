
from .__init__ import VERSION, CORE_COUNT

info = """
 
    Info
    -----
        Name    : Parallel Downloader
        Version : 0.1.0 
 
    """

version_info = f"""
 
 Parallel Downloader Version : {VERSION}
 
"""

simple_example = f"""
 
    Simple Example
    --------------
    $ paralleldownload input_url_file.txt 
   
   * It downloads the files using the urls in the file. Each url in a line.
   * Uses number of process equal to number of CPU Cores in the machine [You have {CORE_COUNT} CPU Cores]
 
"""

detailed_example = f"""
{simple_example}
"""
