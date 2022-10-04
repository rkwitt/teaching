# Computer Vision (PS)

## News / Important dates

- Please enter group memberships and paper titles [here](https://myfiles.sbg.ac.at/index.php/s/PzZkbNt92XxfBHQ) till Oct. 12, 2022
- Begin of lecture: **Oct. 5, 2022 at 10:30am**
- **Location**: T03 (Itzling, Jakob-Haringer Str. 2, FB AIHI/Informatik) 

## General

The computer vision PS for the winter term 2021/2022 will be held **in-person**.

## Grading

At the beginning of the PS, you will get a selection of influential research papers from which you can choose one. Work through the paper, implement it (or large parts of it), and experiment with the approach - try to reproduce some (or all) experiments of the paper, or be creative and think about new, alternative things you can test. Working on toy-examples, e.g., using synthetic data is totally fine. Then write up a summary of the paper, explain the key ideas and document your results and findings. This report should not be more than 8 pages (excluding references). Grading will be based on the quality of the handed-in report (including the documented source code). You can also base your code off of some pre-existing code (e.g., from GitHub), but make sure you understand what's going on - otherwise, it will be very hard to do any serious experiments with it. 

**Note**: you can work together in groups of max. size **three**. Please enter your group members (and paper title) in this Excel spreadsheet [here](https://myfiles.sbg.ac.at/index.php/s/PzZkbNt92XxfBHQ) by Oct. 12, 2022.

*Each week, during the PS, I will meet with 2 groups (for 30 minutes each) and offer in-person support, explanations, etc. for the project.*

### Selection of research papers

S.K. Ainsworth, J. Hayase and S. Srinivasa     
**Git Re-Basin: Merging Models modulo Permutation Symmetries**   
[arXiv](https://arxiv.org/abs/2209.04836)    
2022

Dosovitskiy et al.    
**An Image is worth `16x16` words: Transformers for Image Recognition at Scale**     
[arXiv](https://arxiv.org/abs/2010.11929)     
*ICLR '21*
 
J. Sohl-Dickstein, E.A. Weiss, N. Maheswaranathan and S. Ganguli    
**Deep Unsupervised Learning using Nonequilibrium Thermodynamics**  
[arXiv](https://arxiv.org/abs/1503.03585)    
*ICML '15*    

H. Zhang and Y.N. Dauphin and T. Ma    
**Fixup Initialization: Residual Learning Without Normalization**    
[arXiv](https://arxiv.org/abs/1901.09321)    
*ICLR '19*

K. He, X. Chen, S. Xie, Y. Li, P. Dollár and R. Girshick    
**Masked Autoencoders Are Scalable Vision Learners**    
[arXiv](https://arxiv.org/abs/2111.06377)    
*CVPR '22*












### LaTeX template

For your report use the [NeurIPS 22 LaTex template](https://neurips.cc/Conferences/2022/PaperInformation/StyleFiles).


## Preliminaries: Getting started with PyTorch

I do recommend a setup using [Anaconda Python](https://www.anaconda.com/products/individual). Below is a short how to install Anaconda + PyTorch on a Mac OS X system.

### Download and install Anaconda

First, download the Anaconda installer (for your system) from [here](https://www.anaconda.com/products/individual). Lets assume the download is stored in the  
`/Users/<USERNAME>/Downloads` folder. We will install Anaconda in `/Users/<USERNAME>/Software/anaconda3` (the following commands use the installer for Mac OS X; please adjust according to your system).

```
cd /Users/<USERNAME>/
mkdir Software
cd Software
mv ~/Downloads/Anaconda3-2022.05-MacOSX-x86_64.sh .
chmod +x Anaconda3-2022.05-MacOSX-x86_64.sh
./Anaconda3-2022.05-MacOSX-x86_64.sh
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

The most recent (stable) version is **1.12.1** (as of Sep. 2022) which is also what you should see as the output of the `print` statement.
