# dumbphone-audio-tools

Simple Python script to work with `.mld`, `.mmf`(so far). The script can remove copy protection to then be able to be converted to other formats using PsmPlayer for example.
 
 ## Installation

First, clone the repository:

```bash
git clone git@github.com:memory-hunter/dumbphone-audio-tools.git
```

And then run the following command to install the dependencies.
```bash
pip install -r requirements.txt
```

## Usage
```
python dpat.py [-h] files [files ...]

Remove copy protection from dumbphone audio files

positional arguments:
  files       Files to remove copy protection from

options:
  -h, --help  show this help message and exit
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
