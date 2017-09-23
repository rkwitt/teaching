# Exercise sheet 1 (5 points)

## Exercise 1.1

Experiment with the `skimage` Harris corner detector, and explore the effect
of changes in its parameters. E.g., study the effect of different values of
Gaussian smoothing and different values of gamma (see slides) in the response
function. Read the documentation of the corresponding
`skimage.feature.corner_harris` function.

Use the provided `checkerboard.png` for testing. For a couple of different
Gaussian smoothing and gamma parameters, visualize the detection results
overlaid on the image in your Jupyter notebook.

### Hints

To enable inline plotting in Jupyter notebooks add

```python
%matplotlib inline
from matplotlib import pyplot as plt
```
at the top of your notebook. You can then use `plt.imshow(...)` to show images.
To plot multiple figures next to each other, use, e.g.,

```python
plt.figure(1)
plt.subplot(121)
plt.imshow(...)
plt.subplot(122)
plt.imshow(...)
```
to show to images on a 2 x 1 grid. Look at the corresponding documentation
to use different layouts.

To load images, use
```python
from skimage import io
img  = io.imread('checkerboard.png')
```

### Resources

To find points of local maxima, look at `skimage.feature.corner_peaks` or
`skimage.feature.peak_local_max`.
