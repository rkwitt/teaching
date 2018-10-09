# Computer Vision (PS)

## News / Important dates

- The PS will start on **Oct. 2, 2018**

## Groups

You will work together in **groups of 3 (max.)**. Please find your group
members and let me know by **Oct. 9, 2018** (this is a **hard** deadline).

## Grading

Grading is based on (A) **one detailed paper review** (max. 10 pages) and
(B) a project that
is to be finished by the end of the course (topics will be announced shortly).
100 points are achievable, split into 40 points for the review and 60 points
for the project. Ideally, you hand-in the project in the form of a Jupyter
notebook with all steps documented, or you create your own Python scripts
and document them appropriately.

*All* group members will get the same grade, except for cases where it is
obvious that group members did not participate to the required extent.

## A. Paper review

Choose one of the papers listed on the [main course website](../VO).

## B. Project topics

The core motiviation of the PS projects is not necessarily to come up with a new approach to solve a problem, but to take an existing research article, implement it, and document every step. Some of the project proposals are
more engineering oriented, some require to study the theory in a little bit
more detail. There is an assessment provided to each project to help you
select one.

Please note that in case of the more theoretical projects/articles,
the experiments can be limited to toy data (so, training is quick).
For the more engineering-oriented projects, you can train on reasonably
sized subsets of MNIST or CIFAR-10 for instance, and you do not have to
train the networks till convergence (to save time).

### 1. One-class learning

Here, the problem is to learn a predictor of class membership
for one class **using training data from only that particular class**.
In some settings, this is also referred to as novelty or anomaly detection
(depends on how you look at it) and has been addressed using all kinds
of different ideas. Below is a recent work on this type of problem.

#### Articles

- Ruff et al., *Deep One-Class Classification*, ICML 2018, [PDF](http://proceedings.mlr.press/v80/ruff18a.html)

#### Resources
- MNIST and CIFAR-10/100 data available via PyTorch

#### Assessment
Engineering/Theory

### 2. Image recognition (with ResNets)

The goal is to train a neural network for
visual recognition (i.e., given an image, predict its class label).
Below is the original article explaining the details so called residual
networks (*ResNets*), i.e., current state-of-the-art architecture for
this type of problem. The task is to implement a ResNet and feel free
to adjust things where you see fit. **Do not just copy the PyTorch
example*. Try to assess which parts of the architecture are
more relevant than others recognition performance.

#### Articles

- He et al., *Deep Residual Learning for Image Recognition* , CVPR 2015, [PDF](https://arxiv.org/abs/1512.03385)

#### Resources

- MNIST and CIFAR-10/100 data available via PyTorch
- [TinyImageNet](https://tiny-imagenet.herokuapp.com/) (**optional**)

#### Assessment
Engineering

### 3. Image segmentation (with U-Nets)

#### Articles

- Ronneberger et al., *U-Net: Convolutional Networks for Biomedical Image Segmentation*, MICCAI 2015, [PDF](https://arxiv.org/abs/1505.04597)

#### Resources

- A retinal blood vessel segmentation dataset: [DRIVE](http://www.isi.uu.nl/Research/Databases/DRIVE/download.php)

#### Assessment
Engineering

### 4. Generative advesarial networks (GANs)

The task is to explore designing and training GANs. For simplicity, create
a GAN that learns a multivariate Gaussian in 2D. Samples from this Gaussian
will serve as our **training** data. Input to the generator should be
uniformly distributed samples.

#### Articles
- Goodfellow et al., *Generative Adversarial Nets*, NIPS 2014, [PDF](https://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf)
- Salimans et al., *Improved training techniques for GANs*, NIPS 2016,  [PDF](https://arxiv.org/abs/1606.03498)

#### Resources

You will not need a real dataset for this, as you can just create your
own training data by sampling from the Gaussian. You can obviously use
an image dataset (e.g., MNIST, CIFAR-10) as well if you prefer.

#### Assessment
Engineering/Theory

### 5. Variational autoencoders (VAEs)

In this project, you have to implement a variational autoencoder.
This type of generative model will allow you to sample in the latent
space (i.e., the space induced by the encoder), run those samples
through the decoder and get realistically looking images.

#### Articles

- Kingma et al., *Auto-Encoding Variational Bayes*, ICLR 2014, [PDF](https://arxiv.org/abs/1312.6114)
- Rezende et al., *Stochastic Backpropagation and Approximate Inference in Deep Generative Models*, ICML 2014, [PDF](https://arxiv.org/abs/1401.4082)

#### Resources

- MNIST and CIFAR-10/100 data available via PyTorch

#### Assessment
Theory/engineering

### 6. Masked Autoregressive Flows (MAF)

For those who are into density estimation, this project should be
interesting to, you as you will implement an approach to what is
known as **neural density estimation**. In particular, given data, 
the task is to model the joint density of a set of variables. This
is different to VAEs or GANs, in that neural density estimators 
provide *exact* density evaluations.

#### Articles

- Papamakarios et al., *Masked Autoregressive Flow for Density Estimation*, NIPS 2017, [PDF](https://homepages.inf.ed.ac.uk/imurray2/pub/17maf/maf.pdf)
- Germain et al., *MADE: Masked Autoencoder for Distribution
Estimation*, ICML 2015, [PDF](https://arxiv.org/abs/1502.03509)

#### Resources

For the project to finish, its enough to revisit the toy example in
(Papamakarios et al., 2016, Fig. 1). This toy example uses synthetic
data that is easy to generate and can be used to train the model.

#### Assessment
Theory/Engineering
