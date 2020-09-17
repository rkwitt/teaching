# Computer Vision (PS)

## News / Important dates

- We will start the PS on **Oct. 14, 2020**

## Assignments / Grading

In this PS, we will essentially implement the recent (2020) paper 

Koshla et al.    
**Supervised Contrastive Learning**      
[arXiv](https://arxiv.org/abs/2004.11362)     

*step-by-step*. This means, I will chunk up the implementation of 
the paper into managable steps.

I will provide assignments (for each step) which you have to solve
until a given deadline. Once the deadline is over, you get 
*a correct solution*. You can then work with this solution to 
complete the next assignment (and so on). In this manner, you can
always start fresh and errors are not carried along.

This is the first time, I will experiment with *Github classroom*
as a means to publish and hand-in the exercises. This means **you
will need a GitHub account** for the PS. 

We will implement the paper using [PyTorch](https://pytorch.org/). 
Below you find a description of the steps to setup PyTorch using 
Anaconda Python. Once we reach the point where we can start 
experimenting on a larger-scale, it will be beneficial to have
a GPU. For that, I do recommend to use *Google Collab* where 
you can have access to GPU's for free. I will provide a short
tutorial video on that.

## Preliminaries: Getting started with PyTorch

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
structure of the `teaching/WS2021/CV` folder.
