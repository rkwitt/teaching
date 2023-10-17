# Computer Vision (PS)

## News / Important dates

- **Begin of lecture**: Oct. 4, 2023 at 10:30am
- **Location**: Rechnerübungsraum (Itzling, Jakob-Haringer Str. 2, FB AIHI/Informatik) 

## Grading

This year (2023), all groups will work on the same research paper (see below). Our goal is **not** to implement everything from scratch, but to use a publicly-available reference implementation (see link below) and to make yourself familiar with the key ideas. At a minimum, you should be able to finetune (we will cover that in the lecture) a pre-trained ConvNeXt model on your dataset (e.g., CIFAR10). It is essential that you understand the key ideas of the paper and how these are realized in the reference implementation (which relies on PyTorch). Otherwise, it will be hard to play around with different hyperparameters, or to disable certain parts of the model to understand the effects, etc. *In our PS sessions, I will help you understand the paper as well as the implementation*. The whole idea is to replicate an actual practical situation, where you are given a dataset and task (in our case classification) and you want to use a state-of-the-art model for the task. 

Eventually, you will write a report (max. 8 pages, excluding references, see template below) which summarizes the key aspects of the paper, and which documents your results and findings. Feel free to also point out parts of the work where, e.g., the descriptions in the paper differ from the implementation, or descriptions are unclear. 

**Note**: you can work together in groups of max. size **three**. Please enter your group members (and paper title) in this Excel spreadsheet [here](https://myfiles.sbg.ac.at/index.php/s/PzZkbNt92XxfBHQ) by Oct. 11, 2023.

*Each week, during the PS, I will meet with 2 groups (for 30 minutes each) and offer in-person support, explanations, etc. for the project.*

### Research paper

This year, **all** groups will work on the same paper: 

Liu et al.    
**A ConvNet for the 2020s**    
CVPR 2022     
[Official repository](https://github.com/facebookresearch/ConvNeXt)


### Group schedule

- Oct. 17 - Groups **1** and **2**

### LaTeX template

For your report use the [NeurIPS 22 LaTex template](https://neurips.cc/Conferences/2022/PaperInformation/StyleFiles).


## Preliminaries: Getting started with PyTorch

I do recommend a setup using [Anaconda Python](https://www.anaconda.com/products/individual). Below is a short how to install Anaconda + PyTorch on a Mac OS X system.

### Download and install Anaconda

First, download the Anaconda installer (for your system) from [here](https://www.anaconda.com/products/individual). Let's assume the download is stored in the  
`/Users/<USERNAME>/Downloads` folder. We will install Anaconda in `/Users/<USERNAME>/Software/anaconda3` (the following commands use the installer for Mac OS X; please adjust according to your system).

```
cd /Users/<USERNAME>/
mkdir Software
cd Software
mv ~/Downloads/Anaconda3-2023.07-2-MacOSX-x86_64.sh  .
chmod +x Anaconda3-2023.07-2-MacOSX-x86_64.sh
./Anaconda3-2023.07-2-MacOSX-x86_64.sh
```

Make sure you correctly specify the destination folder (`/Users/<USERNAME>/Software/anaconda3`) during the install process. I also do recommend *not* to run the
init script at the end of the installation process.

### Activate Anaconda

```
~/Software/anaconda3/bin/activate
```

### Install PyTorch

```
conda install pytorch torchvision torchaudio -c pytorch
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

The most recent (stable) version is **2.0.1** (as of Sep. 2023) which is also what you should see as the output of the `print` statement.
