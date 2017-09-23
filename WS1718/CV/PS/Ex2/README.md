# Exercise sheet 2

## Exercise 2.1 (10 points)

In this exercise, we will implement a very simple version of the
**Histogram-Of-Oriented-Gradients** ([HOG](https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients)) descriptor of an image(region).

The idea (quote taken from Wikipedia) is that *that local object appearance and shape within an image can be described by the distribution of intensity gradients or edge directions*.

In this spirit, we will compute (1) horizontal and vertical edge responses
(using simple edge detection masks), then (2) divide the image into blocks
and (3) each block into cells. In our simple example, we assume that we have
256 x 256 grayscale images, with 16 x 16 pixel blocks and 8 x 8 pixel cells.
In each cell, we compute a histogram of the gradient orientations, using
a binning of the range [0,180] degree into 9 bins. Consequently, we get, for
each block, 4 histograms with 9 bins each. The contribution of each pixels
orientation to the histogram should be weighted by its gradient magnitude.

Once we have all histograms, we concatenate the histograms in each cell
(resulting in a vector with 9*4=36 entries) and normalize this vector by its
L2-norm. As we have 16 x 16 pixel blocks, we will finally get 256
36-dimensional vectors. These can, again, be concatenated to form a
9216-dimensional descriptor of the image.

Since all parameters are fixed in this exercise, you can simple write a
Python function

```python
def simple_HOG(img):
    # your code goes here
    return hog_descriptor
```
that does all the necessary computations.

**Bonus** (5 points): Download the [15 scenes](http://www-cvr.ai.uiuc.edu/ponce_grp/data/) dataset and select a
couple of images from each category. Then, compute for each grayscale image
its simple HOG descriptor. Voila, if you now do 1-Nearest Neighbor
classification (e.g., using the Euclidean distance between the vectors)
you have a first, admittely very simple, **image classifier**. However, do
not expect this descriptor to work very well, as this is a very crude
encoding of the images' appearance.

## Useful resources

As in previous exercises, `skimage.util.shape.view_as_blocks` can be
very useful. Once you have gradients in x and y direction, the functions
`np.rad2deg`, `np.arctan2` and `np.hypot` can be used to compute
gradient orientations and magnitudes. Finally, histogram computation can
be done by `np.histogram` and vectors can be concatenated via
`np.concatenate`. Look at the documentation of each of these functions
for details about its parameters.
