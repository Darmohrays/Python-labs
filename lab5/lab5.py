import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

n=207
m=16

array = numpy.random.randint(0, n*m, size=(n, m))

def find_closest(q, array):
    idx = numpy.argmin(numpy.abs(array - q))
    indx = numpy.unravel_index(idx, array.shape)
    return array[indx]

closest = find_closest(200, array)
print(closest)

img = Image.open('0_0.jpg').convert("L")
arr = numpy.asarray(img)
plt.imshow(arr, cmap='gray')
plt.show()