# Exercise sheet 3

**Deadline**: Nov. 13, 2017

## Exercise 3.1 (5 points)

Take the `cameraman` image provided in `skimage`

```python
from skimage import data
img = data.camera() # cameraman image
```

and implement **median filtering** with different neighborhood sizes.
You can use the functions provided by `skimage` for that.

Once you have done this, implement computation of the peak-signal-to-noise
ratio (PSNR) (see [here](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio))
in dB

```python
def psnr(img1, img2):
    # your code goes here
    return img_psnr
```

and plot the PSNR vs. increasing neighborhood sizes of the median filter. Start
with a 3 x 3 neighborhood. In each case, `img1 ` is the original (unfiltered)
image and `img2` is the filtering result. If you want, you do not have to use a square
neighborood, but you can also use a circlular neighborood (e.g., using
`from skimage.morphology.disk`, see documentation).

Add a text section to your Jupyter notebook **interpreting** the results.

## Exercise 3.2 (5 points)

same as Exercise 3.1 from above, but use a Gaussian smoothing
filter and vary the values for `sigma` (i.e., the standard deviation
of the Gaussian filter).
