# Exercise sheet 5

## Exercise 5.1 (10 points)

In this exercise, we implement a (spread-spectrum) watermarking
algorithm, based on the 2D wavelet transformation. The idea is
to run a 2D wavelet decomposition on a grayscale image, choose
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
Exercise 5.1.
