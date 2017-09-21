# Exercise sheet 4

## Exercise 4.1 (10 points)

Write a Python function that performs smoothing (with a Gaussian kernel)
in the Fourier domain. To see the effect of smoothing
in the Fourier domain more clearly, we will run
this on an artificial 40 x 40 black image with a 10 x 10
white block in the middle. Use

```python
def generate_square():
  sq = np.zeros((40,40))
  sq[15:25,15:25] = 1
  return sq
```

to generate the test image. Your smoothing function should look something
like this:

```python
def frequency_smoothing(img, sigma):
  # your code goes here
  return smoothed_image

```
Here, `img` denotes the grayscale image and `sigma` specifies the width of the
(isotropic) Gaussian in the frequency domain (you have to write this yourself).

In your Jupyter notebook you include:

1. Code for the `frequency_smooth` function
2. Code to generate the Gaussian smoothing kernel
3. Visualization of the spectrum of the image *before* smoothing
4. Visualization of the spectrum of the image *after* smoothing
5. Visualization of the smoothed image
6. (**Bonus** - 2 points) Implement a non-isotropic Gaussian and visualize some results

### Useful resources

To compute the 2D FFT, look at the `numpy.fft` package.
