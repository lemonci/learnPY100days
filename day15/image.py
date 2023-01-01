# All are scripts
from PIL import Image
image = Image.open('./res/guido.jpg')
image.format, image.size, image.mode
image.show()

rect = 100, 50, 520, 560
# left, top, right, bottom
image.crop(rect).show()

size = 128, 128
image.thumbnail(size)
image.show()

image.rotate(180).show()
image.transpose(Image.Transpose.FLIP_LEFT_RIGHT).show()

for x in range(80, 310):
    for y in range(20, 360):
        image.putpixel((x, y), (128, 128, 128))

image.show()

from PIL import Image, ImageFilter
image = Image.open('./res/guido.jpg')
image.filter(ImageFilter.CONTOUR).show()