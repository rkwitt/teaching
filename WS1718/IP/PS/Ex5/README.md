# Exercise sheet 5

## Exercise 5.1 (10 points)

In this exercise, we implement an additive (spread-spectrum) watermarking
scheme, based on the 2D wavelet transform. The idea is
to run a 2D wavelet decomposition on a **grayscale image**, choose
a subband and add a bipolar (-1,+1) watermark sequence `w` to the wavelet
coefficients `y` of this subband. This sequence is added with a certain
*strength* `alpha` (i.e., a multiplicative factor), i.e., `y = x + alpha*w`.
This is called *additive spread-spectrum watermarking*.
Finally, we will reconstruct the image from the wavelet coefficients.

In principle, the **steps** are as follows:
1. Wavelet-decompose the image
2. Choose a subband
3. Generate a random bipolar watermark sequence
4. Add the sequence to the wavelet coefficients of the subband
5. Reconstruct the image from the coefficients

A possible embedding function for the watermark could look like this:

```python
def embed(img, where, alpha, seed):
    # your code goes here
    return watermarked_image, watermark_sequence
```

The function returns the watermarked image and the watermark sequence.

### Resources

Use the `PyWavelets` Python package, e.g., with Anaconda you can
install this using

```bash
conda install pywavelets
```
and then quickly test with
```bash
python
>> import pywt
```

## Exercise 5.2 (10 points)

In this exercise, we implement a simple (correlation-based)
watermark detector for the watermarking algorithm of
Exercise 5.1 and evaluate this detector with a couple of
randomly chosen watermarks.

In principle, the **steps** are as follows:
1. Embed a watermark
```python
wm_img, wm = embed(img, (1,0), 0.01, 1234)
```
2. Detect the watermark by decomposing the image using the 2D wavelet transform,
select the subband (in my example level=1,subband=0, remember we get 3 subbands
per decomposition level) and correlate the coefficients `x` with the watermark sequence `w`, e.g.,
```python
def detect(img, where, w):
    # your code goes here
    return score
```
The correlation is computed as `1/N * (x[0]*w[0] + ... + w[N]*x[N])`
 where `N` denotes the number of coefficients in the subband.
3. Generate 1000 random watermarks and plot/compare the detection scores to the
detection score you get with the actual embedded watermark (using the correct
random number generator seed).
4. **Bonus** (2 points): Choose differend embedding strenghts `alpha` (e.g., 0.01,0.05,...,0.5) and compute the PSNR
between the original image and the watermarked image. Maybe visualize the image
and check if you see any obvious distortions caused by the embedding process.
