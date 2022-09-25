# Paralleldownload
#### Download large number of files extremely fast.


A Python Package for Fast Parallel Download of Multiple Files.
It's Simple, easy and extremely fast since it uses, all the cores in your CPU to spin separate process for parallel download.
Paralleldownload uses `requests` as its only dependency, which is almost always present in all python environment.



![PyPI - Python Version](https://img.shields.io/pypi/pyversions/paralleldownload?style=for-the-badge)

### Python Package Index Badges

[![PyPI](https://img.shields.io/pypi/v/paralleldownload?style=for-the-badge&color=gree&logo=pypi)](https://pypi.org/project/batchimage/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/paralleldownload?label=Downloads&style=for-the-badge)
![PyPI - Status](https://img.shields.io/pypi/status/paralleldownload?label=Status&style=for-the-badge)
![PyPI - Format](https://img.shields.io/pypi/format/paralleldownload?label=Format&style=for-the-badge)


### Github Badges

![GitHub last commit](https://img.shields.io/github/last-commit/insumanth/paralleldownload?style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/insumanth/paralleldownload?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/insumanth/paralleldownload?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/insumanth/paralleldownload?style=for-the-badge)



------------------
## Python Package Index Install 

```
pip install paralleldownload
```
-------------------

### Usage:

**Basic example:**
```shell
$ paralleldownload input_url_file.txt
```
* It downloads the files using the urls in the file. Each url in a line.
* The downloaded files is stored in current directory.
* Uses number of process equal to number of CPU Cores in the machine.

**Getting help, info, version and example:**
```shell
$ paralleldownload [-h | -i | -v | -eg]
```
* These options will just print text and exits.
  * `-h ` Prints the help message.
  * `-i ` Prints information aboout the package.
  * `-v ` Prints current version of the package.
  * `-eg` Prints few example of how to use the this cli.

Specify save directory:
```shell
$ paralleldownload input_url_file.txt downloads_directory
```
* The downloaded files is stored in `downloads_directory` directory.
* You can provide absolute or relative paths for both url file and save directory.

**Use N Processes**:
```shell
$ paralleldownload input_url_file.txt -p 17
```
* Uses 17 processes to download files.
* Default is equal to the number of cpu core count in the machine.


**File names:**

```shell
$ paralleldownload input_url_file.txt [-u | -n | -a]
```

* By default, it searches for the file name in the response. If found, it will use this name. Else it will use a uuid string as file name. [Yet to be implemented]
  * `-u` All downloaded files will be named as uuid strings `[eg: 5b71113f-43be-40f5-b267-9b93919196aa.jpg]`
  * `-n` All downloaded files will be named as sequential numbers `[eg: 017.jpg]`
  * `-a` All downloaded files will be named as sequential lowercase english alphabets `[eg: exy.jpg]`
* If extension is needed, they have to be manually provided.


**Specify Extension**
```shell
$ paralleldownload input_url_file.txt -e png
```
* Uses the provided extension in file names.
* `.` (dot) is optional.
* If extension is needed, they must be provided when using `[-u | -n | -a]` .



------------------

#### Description

Do you want to download thousands of files at once but can't wait for sequential download? 

Today's machines have multiple CPU cores.
Most entry level machines have 4 Cores while higher end machines have around 8 Cores, 
Some desktop processor even have 16 - 32 Cores.
But using just one Core for downloading files is not the best approach if you have hundreds or thousands of files to download.

The rapid shift towards cloud technologies provide massive processing power, GigaBit network and faster writes to disk.
By properly making use of this processing power, bandwidth, memory and IO, we can make our life a bit easier.

paralleldownload is one of such package.
It is a cli tool used to download thousands of files in short time.
It achieves it by spinning seperate process per CPU core and downloading parallely.


Imagine a Machine with 24 Core CPU and Gigabit Network.
The process to download 1000 files, and it takes 1 second to fetch each file,

##### Sequential download

Python Interpreter does the following steps.

Make request  ➜ open a file ➜ save the content to the file

After it is done, Python Interpreter repeats the steps 1000 times sequentially.



It takes `1000 files` `x` `1 Second` = `1000 Seconds` or `~17 Minutes` to download all files.

`➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜`
 
##### Parallel download

28 Python Interpreter is spun up in all of 28 cores (one per core by default).

Each Python Interpreter does the following steps.

Make request  ➜ open a file ➜ save the content to the file

After it is done, Each Python Interpreter repeats the steps 42 times (1000 files / 24 process).

It takes `(1000 files` `/` `24 Processes)` `x` `1 Second` = `42 Seconds` or `~1 Minutes` to download all files.

```
➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜
➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜
➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜
[.. 19 more processes ..]
➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜
➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜
```

**Note:** This is just a logical comparison.
The time is not a real world example, many factors affects the download speeed.
There will be a slight overhead in setting up the process and collecting the work.
So, it will not download all in under a minute.
The Overhead should be negligable with higher input.





-----------------
![Made With Python](https://forthebadge.com/images/badges/made-with-python.svg)
![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)

<!--
<img src="https://forthebadge.com/images/badges/works-on-my-machine.svg" alt="works-on-my-machine" width="500" height="100">
-->
