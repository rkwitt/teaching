# Computer Vision (PS)

## News / Important dates

- We will start the PS on **Oct. 2, 2019 (10:30-11:30am, T03)**

## Grading

The PS is split into **two parts**. In the first part (which lasts till around Nov./Dec.), each student will hand in 
weekly assignments (published below). The assignments are designed such that once we are done with all assignments, we will have a working CIFAR-10 neural network classifier. As the assignments build on top of each other, I will provide one possible solution once the deadline for an assignment has passed, so that you can start the next assignment without carrying over any errors.

In the **second part** you will work together in groups of max. size 3. Each group can choose from a selection of recent research papers on the topic of *regularization* (I will provide links as we go along). Each paper essentially presents a different strategy to regularize training of neural networks. You will then experiment with the technique you choose on the problem of learning from only 500 CIFAR-10 examples (which should be doable on your laptop or Desktop PC even without a GPU). The idea is that you obtain a full understanding on how these techniques work and what effect they have. My goal is that you (1) understand the technique in detail, then (2) implement the technique (although most of these things are already available in PyTorch) and (3) experiment with it to quantify its effects your neural network classifier's performance. Once you are done, write a report which critically reflects on the technique and presents your experimental results (max. 5-8 pages).

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
structure of the `teaching/WS1920/CV` folder. All the notebooks reside under
`material`.


## Assignments

1. Assignment 1 (due on Oct., 15, 11:59pm)
2. Assignment 2 (due on )
3. Assignment 2 (due on )
