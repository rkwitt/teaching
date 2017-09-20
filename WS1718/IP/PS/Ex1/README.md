# Exercise Sheet 1

**Deadline**: Oct. 16, 2017

## Exercise 1 (5 points)

Write a Python function `avg_H_global` which takes as input the filename
of an RGB image and computes the average value of the H channel. This value
should be returned. So, e.g.,

```python
def avg_H_global(img_file_name):
  ...
  return avg_H_val
```

Either use `skimage` routines (search the documentation) to do the RGB
to HSV conversion, or implement it yourself by looking up the formula.
Test your function with

```
print avg_H_global('beach.jpg')
```

using `beach.jpg` which can be found in this folder of the repository.

## Exercise 2 (5 points)

Write a Python function `avg_H_per_block` which takes, as input, a
filename of an RGB image as well as a tuple (N,M) that specifies a
block size. The function should first convert the image to HSV color
space and then partition the image into blocks of size N x M pixel.
For each block, the average value of the H channel should be computed.
The function should return a `numpy` array of dimensions X x Y which
holds, at the (i,j)-th position, the avgerage H channel value of the
(i,j)-th block. E.g.,

```python
def avg_H(image_file, block_size):
  ...
  return avg_H_val
```

In this example, `block_size[0]` and `block_size[1]` represent N and
M, respectively. Again, test your function with

```python
H_avg = avg_H('beach.jpg', (16,16))
plt.imshow(H_avg, cmap='gray')
```

**Note**: Only use image- and block-sizes that are compatible, so, e.g.,
a 256 x 256 image with 16 x 16 blocks.
