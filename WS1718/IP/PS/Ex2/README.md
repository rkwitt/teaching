# Exercise Sheet 2

**Deadline**: tba.

## Exercise 2.1 (5 points)

Write a Python function which computes a Gaussian pyramid of a grayscale image.
In particular, the function should take either a grayscale image as input, or
a RGB color image and compute a N-level Gaussian pyramid decomposition. We
simplify this example

**Note**:
Do not use the `skimage` provided `skimage.transform.pyramid_gaussian` function,
but implement it yourself using Gaussian smoothing and downsampling.

The function should return a dictionary with the decomposition level
index as key. E.g.,

```python
def compute_Gaussian_pyramid(img, levels, sigma):
    pyr = {}
    ...
    return pyr
```

Test, for example, with

```python
from skimage import io
from skimage.color import rgb2gray

img_c = io.imread('beach.jpg')
img_g = rgb2gray(img_c)
pyr = compute_Gaussian_pyramid(img_g, levels=4, sigma=2*2/6.0)
```

Visualize each level of the pyramid as an image in the Jupyter notebook.

**Hints**: The `scipy`'s `ndimage` module can be helpful for Gaussian smoothing.
For visualization, you can import the following in your Jupyter notebook:
```python
%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt

# your code goes here

plt.imshow(img_g, cmap='gray')
```

## Exercise 2.2 (5 points)

Write a Python function that takes, as input, a grayscale image and
performs histogram equalization. The function should output the
histogram-equalized image.

```python
def histogram_equalize(img):
    #...
    return out
```

Use the `myelin.png` image from this directory for testing and visualize
the original and the histogram-equalized image.

Visualize the grayscale histograms of the original and the histogram-equalized
image. **Hint**: To plot multiple images next to each other, you can use

```python
plt.figure(1)
plt.subplot(211)
plt.imshow(...)
plt.subplot(212)
plt.imshow(...)
```

## Exercise 2.3 (10 points)

Write a Python function that takes two images, a **source** image and
a **target** image (both grayscale) and then matches the source image's
histogram to the target images' histogram.

```python
def histogram_match(source, target):
    #...
    return matched
```
Visualize the CDF of the (1) source, the (2) target and (3) the histogram-equalized
source image. Use `lena.jpg` as source image and `stairs.jpg` as the target image.

### Hints for 2.2 and 2.3

`skimage.exposure.cumulative_distribution` computes the CDF of an image's
grayscale values. `np.interp` allows you to interpolate. Also, in Python you can
distribute values based on indices easily, e.g.,

```python
a = np.array([1,2,3])
b = np.array([0,0,0,0,2,2])
```
This will create a numpy array with values `[1,1,1,1,3,3]`. This is very
helpful when you already have the matching between grayscale values from
the source and the target image. For example, once you have the matching
between grayscale values of the source and the target image, you can simply
distribute the matching results to the corresponding spatial locations.
