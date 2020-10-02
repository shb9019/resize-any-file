# Resize Any File

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Command line tool to resize files to target size of (ideally) any type. Currently,
only images are supported.

## Setup

```commandline
git clone https://github.com/shb9019/resize-any-file.git
cd resize-any-file
pip install --editable .
```
Note: Prefer installing this repo on a virtualenv.
 
 ## Features
 
#### Resize image
Given target image size in bytes, scale the image preserving aspect ratio.
 ```commandline
resize-any-file input_file.jpg output_file.jpg --target_size 5000
```

#### Compress Image
Given target image size in bytes, change quality of the image preserving dimensions. 
 ```commandline
resize-any-file input_file.jpg output_file.jpg --target_size 5000 --preserve_dimensions
```

## Supported Types

### Images

* jpg, jpeg
* png
* tiff
* webp
* ppm
