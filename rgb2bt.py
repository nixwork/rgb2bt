import argparse
import cv2 as cv
import os.path
import sys

### Parse commans line arguments ###
parser = argparse.ArgumentParser(
    description="Convert RGB image to a 4-2-2 YCrCb file")
parser.add_argument("file",
                    help="Name of an image to convert")
parser.add_argument("-W", "--width", type=int, default=720,
                    help="Required width of the output image")
parser.add_argument("-H", "--height", type=int, default=576,
                    help="Required height of the output image")
parser.add_argument("-O", "--output", default="output.txt",
                    help="Output file name")
args = parser.parse_args()

print("Input file is " + args.file)
print("Output file is " + args.output)
print("Output width is " + str(args.width))
print("Output height is " + str(args.height))

if not os.path.isfile(args.file):
    print("ERROR: no such file " + args.file)
    sys.exit()

### Image processing ###
img = cv.imread(args.file)
img = cv.resize(img, (args.width, args.height), interpolation = cv.INTER_LINEAR)
img = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)

# normalization to 1-254 range
# we get doubles here!
img = img * (253 / 255) + 1

### Write pixels to the file ###
outfile = open(args.output, 'w')
height, width, depth = img.shape
for y in range(0, height):
    for x in range(0, width):
        # Cb for even pixels, Cr for odd
        outfile.write("%03d " % (img.item(y, x, (2, 1)[x % 2])))
        # Y
        outfile.write("%03d " % (img.item(y, x, 0)))

    outfile.write("\n")

outfile.close()
