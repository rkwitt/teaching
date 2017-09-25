# Exercise sheet 4

## Exercise 4.1 (25 points)

In this exercise, you will have to implement a convolutional neural
network (CNN) for **people counting** (i.e., a regression task).

Specifically, we use the [UCSD Pedestrian dataset](http://www.svcl.ucsd.edu/projects/peoplecnt/) for this.
This dataset has surveillance videos overlooking a sidewalk, where
each frame is annotated by the number of people walking. For
more details, see the dataset description available at the link
above.

I will provide you with the [implementation](https://gist.github.com/rkwitt/0c781d1c3cc9ae5db8cdf35fa30648df) of the
`torch.utils.data.Dataset` so that you can use the vanilla
`torch.utils.data.DataLoader`. Your task is to implement a
a CNN architecture that allows you to perform the counting
task. For inspiration, you can look, e.g., of the AlexNet
implementation available as part of PyTorch, see
[here](https://github.com/pytorch/vision/blob/master/torchvision/models/alexnet.py).

In this exercise, you will only implement the **training**
of this *counting*-CNN.

## Exercise 4.2 (10 points)

In this exercise, you will use your trained network from
Ex. 4.1 to run a held-out portion of the UCSD Pedestrian
dataset through your network and assess its performance.
Specifically, you will have to run each image through the
net and eventually plot the predicted *people count* against
the ground truth and assess the *mean-squared-error (MSE)*
as well as the *mean-absolute-error*.
