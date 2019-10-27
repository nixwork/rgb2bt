# RGB2BT

A tool for converting RGB image into YCrCb 4:2:2 format image presented as a text file.

## Dependencies
- python3
- opencv-python

```bash
$ pip install opencv-python
$ pip install opencv-contrib-python
```

## Usage
```bash
$ python rgb2bt.py file
```
*file* - input image (jpg or something).
That command generates **output.txt** file with YCrCb pixel values line by line. Size of output image is 720x576.
Default output file name and resolution can be changed via command line arguments.

For more information see help message
```bash
$ python rgb2bt.py --help
```
