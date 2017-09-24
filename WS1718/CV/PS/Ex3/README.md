# Exercise sheet 3

## Exercise 3.1 (20 points)

In this exercise, we will implement a **very simple** image classifier based on HOG signatures. In particular, we will build a classifier for the infamous [15 scenes](http://www-cvr.ai.uiuc.edu/ponce_grp/data/) dataset.
This dataset consists of (grayscale) scene images from 15 scenes (as the dataset name
suggests :).

In principle, we will compute HOG signatures for every image in the dataset, then train a linear Support-Vector-Machine (SVM) classifier
from a subset of the images' signatures and eventually use the trained classifier to predict class labels for
the remaining images.

**Hand-in** a Jupyter notebook which implements this
pipeline and, at the end, reports the classification
accuracy (total and per-class) on the testing portion
of the data.

Below is a more detailed description of the **required
steps**.

### HOG computation

Use the HOG descriptor implementation available as part of `skimage`. I do
recommend to use 8 orientations, 16 x 16 pixel per cell and 16 (i.e., 4 x 4)
blocks per cell.


### Splitting the data into training / testing

`sklearn.model_selection.train_test_split` provides all
the functionality that you need to split your data into
training and testing. I do recommend to keep 30% of the
data for testing and use the rest for training.

To use this function, *first* compute HOG signatures
for all images and store the these signatures in a
`numpy` matrix - one signature per row.
Also, build-up a Python list of integers that identifies the label (0,..,14) of each image. The
position of the label in the list should obviously
correspond to the row in the data matrix. The data matrix and the label list can then be used as inputs
to `sklearn.model_selection.train_test_split`.

### Classifier training

Make yourself familiar with the `sklearn.svm.SVC` documentation. Specifically,
we will set the parameter `kernel='linear'` to instantiate a **linear SVM**.
You can also try to use the standard setting `kernel='rbf'` if you want, but this might require more tuning.
