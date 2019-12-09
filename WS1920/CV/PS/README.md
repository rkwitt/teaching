# Computer Vision (PS)

## News / Important dates

- [Meeting doodle](https://doodle.com/poll/2xhgwtizd6n74yui)
- Please let me know the project topic (i.e., paper title) and group membership by **Nov. 29, 2019**
- We will start the PS on **Oct. 2, 2019 (10:30-11:30am, T03)**

## Grading

The PS is split into **two parts**. In the first part (which lasts till around Nov./Dec.), each student will hand in weekly assignments (published below). The assignments are designed such that once we are done with all assignments, we will have a working CIFAR-10 neural network classifier. As the assignments build on top of each other, I will provide one possible solution once the deadline for an assignment has passed, so that you can start the next assignment without carrying over any errors.

In the **second part** you will work together in groups of max. size 3. Each group can choose from a selection of recent research papers on the topics of (1) *regularization* and (2) *theoretical aspects* of learning with neural networks.

For the implementation-oriented projects, you have to implement the method from the paper you select and experiment with it on the problem of learning a CNN-classifier on only 500 CIFAR-10 examples (which should be doable on your laptop or Desktop PC even without a GPU). The idea is that you obtain a full understanding on how these techniques work and what effect they have. My goal is that you (1) understand the technique in detail, then (2) implement the technique (although most of these things are already available in PyTorch or on GitHub) and (3) experiment with it to quantify its effects your neural network classifier's performance. Once you are done, write a report which critically reflects on the technique and presents your experimental results (max. 8 pages).

For the *theory-oriented* projects, the goal is to (1) understand the key ideas, (2) go through the
proofs and (3) identify strengths and weaknesses (e.g., with respect to the assumptions made). Similar to the implementation-oriented projects, you have to write a (max. 8 page) report in which you summarize your findings, and possibly more detailed variants of the proofs (which are often written quite concisely in the papers for space reasons).

Both parts are weighted equally to obtain the final grade (but you have to be positive in each sub-part).

## Handing-in assignments

Assignment have to be handed in (as Jupyter notebooks) at [abgaben.cosy.sbg.ac.at](https://abgaben.cosy.sbg.ac.at/).

For the second part of the proseminar, the report including the code can be handed-in by email.

## Getting started with PyTorch

I do recommend a setup using Anaconda Python. Below is a short howto to install
Anaconda + PyTorch on a Mac OS X system.

### Download and install Anaconda

First, download the Anaconda installer (for your system) from [here](https://www.anaconda.com/distribution/). Lets assume the download is stored in the  
`/Users/<USERNAME>/Downloads` folder. We will install Anaconda in
`/Users/<USERNAME>/Software/anaconda3`.

```
cd ~
mkdir Software
cd Software
mv ~/Downloads/Anaconda3-2019.07-MacOSX-x86_64.sh .
chmod +x Anaconda3-2019.07-MacOSX-x86_64.sh
./Anaconda3-2019.07-MacOSX-x86_64.sh
```

Make sure you correctly specify the destination folder (`/Users/<USERNAME>/Software/anaconda3`) during the install process. I also do recommend *not* to run the
init script at the end of the installation process.

### Activate Anaconda

```
~/Software/anaconda3/bin/activate
```

### Install PyTorch

```
conda install pytorch torchvision -c pytorch
```

### Test the installation

```
~/Software/anaconda3/bin/activate
python
```

In the Python shell type

```python
import torch
print(torch.__version__)
```

The most recent (stable) version is 1.2 (which is also what you should see as
  the output of the `print` statement).

## Running the course notebooks

The easiest way to run my course notebooks, is to clone my teaching repository
via

```
git clone https://github.com/rkwitt/teaching.git
```

then go to `teaching/WS1920/CV` and start a local Jupyter notebook server via

```
jupyter notebook
```

Basically, a new browser tab should open where you see the file system
structure of the `teaching/WS1920/CV` folder. Assignment notebooks for
the PS reside in the `PS` subfolder.


## Assignments

1. [Assignment 1](1-Assignment.ipynb) (due on Oct., 15, 11:59pm)
2. [Assignment 2](2-Assignment.ipynb) (due on Oct., 26, 11:59pm)
3. [Assignment 3](3-Assignment.ipynb) (due on Nov., 25, 11:59pm)

The MNIST training example can be found [here](MNIST-SimpleNetwork-Training.ipynb).

## Project topics

Below, you find a selection of papers which broadly cover the topics of (1)
regularization and (2) theoretical aspects of learning with (deep) neural networks.

Each paper constitutes **one** PS project. Please select **one** of them.

### Implementation-oriented projects

For most of the papers, you can find (PyTorch) code online (e.g., on GitHub) which you can
adapt to your needs and incorporate it into your implementation of the CIFAR-10
classifier from the previous assignments. Do not just
copy code around, but try to understand the key ideas; experiment with different
parameter settings (depending on the specific approach) and try to figure out what is
beneficial (or what is not) in terms of classification accuracy on our CIFAR-10
problem with 500 samples. When you report classification accuracy, report the
average accuracy you obtain over 10 runs (each run with a different selection of 500
  training samples), evaluated on the full CIFAR-10 testing split.

DeVries & Taylor (arXiv, 2017)  
*Improved Regularization of Convolutional Neural Networks with Cutout*    
[PDF](https://arxiv.org/pdf/1708.04552.pdf)

Zhang et al. (ICLR, 2018)      
*mixup: Beyond Empirical Risk Minimization*    
[PDF](https://openreview.net/pdf?id=r1Ddp1-Rb)

Verma et al. (ICML, 2019)    
*Manifold Mixup: Better Representations by Interpolating Hidden States*    
[PDF](http://proceedings.mlr.press/v97/verma19a/verma19a.pdf)

Cubuk et al. (CVPR, 2019)    
*AutoAugment: Learning Augmentation Strategies from Data*     
[PDF](https://zpascal.net/cvpr2019/Cubuk_AutoAugment_Learning_Augmentation_Strategies_From_Data_CVPR_2019_paper.pdf)    
*Remark*: Do not try to implement learning of the augmentation policies, just find the policies online, implement them and experiment with them.

Kobayashi (BMVC, 2019)    
*Large Margin in Softmax Cross-Entropy Loss*     
[PDF](https://bmvc2019.org/wp-content/uploads/papers/0636-paper.pdf)

## Theory-oriented projects

For the more theoretical projects, the goal is to (1) understand the key ideas
and summarize them, (2) go through the proofs and (3) give your opinion on the
strengths and weaknesses of the paper (e.g., in terms of assumptions made, etc.)

Anil et al. (ICML, 2019)    
*Sorting Out Lipschitz Function Approximation*   
[PDF](http://proceedings.mlr.press/v97/anil19a.html)

Sokolic et al., (AISTATS, 2017)     
*Generalization Error of Invariant Classifiers*     
[PDF](http://proceedings.mlr.press/v54/sokolic17a/sokolic17a.pdf)

Bartlett et al. (NIPS, 2017)    
*Spectrally-normalized margin bounds for neural networks*    
[PDF](https://arxiv.org/abs/1706.08498)
