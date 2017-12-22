# Exercise sheet 5

## Exercise 5.1 (15 points)

In the final exercise of this Proseminar, you
should implement your own neural network layer (in our case, an activation function) in PyTorch.

The layer should compute a *Rectified Quadratic Unit (ReQU)* which is defined as

```
requ(x) = x^2 if x>0 and 0 otherwise
```

ReQU's operate element-wise on the input. I.e., if you input a Nx1 vector, the unit should apply the activation function to each of the vector elements.

In principle, the implementation should look something like the template below. Additional help can be found [here](http://pytorch.org/docs/master/notes/extending.html). It is also worth looking into the PyTorch implementations of other layers to get some inspiration.

```python
class ReQU(nn.Module):
    def __init__(self):
      """Your code goes here."""

    def forward(self, x):
      """Your code goes here."""
```

Test your code using a simple neural network with the following simple
structure:

```
Linear(2,20)-ReQU-Linear(20,1)-ReQU
```

As loss, use the MSE loss (i.e., `nn.MSELoss`). The training data is provided
below. `X` are the input points, `Y` are the targets. Note that the way the
data is prepared below, you have 2 batches of size 4.

```python
X = [
  [[0.01, 0.01],
   [0.01, 0.90],
   [0.90, 0.01],
   [0.95, 0.95]],
  [[0.02, 0.03],
   [0.04, 0.95],
   [0.97, 0.02],
   [0.96, 0.95]]
   ]
Y = [
  [[0.01],
   [0.90],
   [0.90],
   [0.01]],
  [[0.04],
   [0.97],
   [0.98],
   [0.1]]
   ]
```

Use SGD as your optimizer (with a learning rate of, say, 0.01) and run over the data for 10000 epochs (this should be quick even on a CPU). Finally, *report* the prediction results of your trained network when you run X[0] through it. If you plot the 2-D data in X and look at the targets Y, you will see that this network essentially learns an **XOR** function.

**Hint**: You can obviously draw some inspiration from the Gaussian layer example we developed during the X-Mas lecture on Dec. 19, 2017.
There is a link to the lecture demo on the main course website.
