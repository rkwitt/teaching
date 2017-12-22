# Exercise sheet 7

## Exercise 7.1 (20 points)

In this exercise, we will implement a relatively simple image
segmentation algorithm that is similar to the ideas presented
in the [SLIC superpixels](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.165.8269&rep=rep1&type=pdf) paper.

### Idea

Basically, we will take a color image (RGB) and try to *cluster* the
color vectors (3x1 vectors/pixel) into a collection of K clusters
(with K as an input parameter). For this, we will use the *KMeans* clustering algorithm, implemented in `sklearn` (we will discuss
KMeans clustering in the lecture, but you can also read-up on this
[here](https://de.wikipedia.org/wiki/K-Means-Algorithmus)).

Since KMeans (by default) relies on Euclidean distances between the input points (i.e., our color vectors) and Euclidean distances in RGB space do not really conform to our (human) perception of color distances, we will run clustering in the LAB color space instead (conversion can be done using the methods in `skimage.color`). LAB is more appropriate for this task.

The KMeans algorithm returns us a collection of K *cluster centers*, i.e., K representatives of the colors occurring in the image. We can then replace the color values in the original image by the cluster center it was assigned to (i.e., the cluster centers that are *closest* to each pixel color vector in the image). This will give us a first *segmentation* of the image into partitions that are *close* in color space.

As an extension we add, to the LAB color values, the (x,y) position
of each pixel on the image grid, i.e., each pixel now is represented as a vector `[L,A,B,x,y]`. The idea here is that pixel that are close in color space **and** close in spatial distance should be clustered together. **Note**: In our implementation we will simply ignore the fact that the range of LAB values and (x,y) values might *not* be compatible (in terms of value range). For those of you who want to get bonus points, read the original paper and add a comment (to the Jupyter notebook) on how you would deal with this problem.

### Details

#### KMeans clustering

Given an image in LAB color space (W,H,3), we can reshape the image
array into a (W*H,3) matrix, where W and H denote the width and height of the image, e.g.,

```python
X = im.reshape((im.shape[0]*im.shape[1],3))
```

To run KMeans clustering on this data matrix, we simply
create an instance of the KMeans class, specify the number
of clusters and run the KMeans algorithm by calling
the `fit()` method, i.e.,

```python
km = KMeans(n_clusters=200)
km.fit(X)
```
As this will probably be very slow (depending on the image size), we can simply draw a random sample from the data in
`X` and run the KMeans algorithm on that instead:

```python
from sklearn.utils import shuffle

sample = shuffle(X, random_state=0)[:5000]
km = KMeans(n_clusters=200)
km.fit(sample)
```

Once finished, the cluster centers will be contained in
`km.cluster_centers_`. To get the assignment of *all* color
vectors in `X`, we can run the `predict()` method of the
`KMeans` class as follows:

```python
labels = km.predict(X)
```

For K=200, `labels` should contain (W*H) integer values in
the range [0,200]. You could now reshape this into a (W,H)
matrix and visualize the result as an image.

#### Recreating a color image from the KMeans result

Essentially, you have to write a method that takes, as
input, the *cluster centers* as well as the
*cluster assignments* and fills up a (W,H,3) matrix that can be
visualized.

```python
def create_image(centers, labels, w, h):
    image = np.zeros((w, h, 3))
    """
    your code goes here.
    """
    return image
```

Play around with the number of cluster centers (e.g., from
20-400) and visualize the images.

#### Adding spatial coordinates

To add the (x,y) positions of each pixel, you simply have to
concatenate the data matrix `X` with the matrix of spatial coordinates along the horizontal direction. This will give you a (X.shape[0],5) matrix `Y` on which you can run the KMeans clustering algorithm (instead of `X`).

#### Extracting and overlaying boundaries

To actually get a segmentation in the form of *segmentation boundaries*, you
can use `skimage`'s `mark_boundaries` method from
`skimage.segmentation`. Here's an example:

```python
plt.imshow(
    mark_boundaries(
        image,
        labels.reshape((image.shape[0],image.shape[1])),
        color=(1, 0, 0)))
```
The `color` argument specifies the color of the boundary that is overlayed on
the `image`. Make sure that you convert the LAB image back to RGB, so that you get a nicely looking image.

**Remark**: When you run your `create_image` method and you pass the `centers` your centers will be 5-dimensional in the case where you added the spatial coordinates. In order to use the same routine with and without spatial coordinates, just pass the first three dimensions of `km._cluster_centers_` to the method.

### What should you hand-in?

The Jupyter notebook should contain the full source code and a couple of segmented images with different choices of the number of
clusters K. Compare the results that you get *with* and *without* adding spatial coordinates to the data matrix.

### Why do we call these superpixels?

The segmentation that you get will be an *over-segmentation* of the image, but most of the boundaries of the objects will be nicely captured. In some sense, this method partitions the image into a set of larger "pixels" (of consistent image appearance) - so called *superpixels* - that can then be used for further processing (e.g., classification).
