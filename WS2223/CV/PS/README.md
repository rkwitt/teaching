# Computer Vision (PS)

## News / Important dates

- Begin of lecture: **Oct. 65, 2022 at 10:30am**
- **Location**: T03 (Itzling, Jakob-Haringer Str. 2, FB AIHI/Informatik) 

## General

The computer vision PS for the winter term 2021/2022 will be held **in-person**.

## Grading

tba.

## Preliminaries: Getting started with PyTorch

I do recommend a setup using [Anaconda Python](https://www.anaconda.com/products/individual). Below is a short how to to install Anaconda + PyTorch on a Mac OS X system.

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

The most recent (stable) version is **1.12.1** (as of Sep. 2022) which is also what you should see as
the output of the `print` statement).

## Running the course notebooks

The easiest way to run my course notebooks, is to clone my teaching repository
via

```
git clone https://github.com/rkwitt/teaching.git
```

then go to `teaching/WS2223/CV` and start a local Jupyter notebook server via

```
jupyter notebook
```

Basically, a new browser tab (in your default browser) should open where you see the file system
structure of the `teaching/WS2223/CV` folder.

## Assignments

tba.

Total number of possible points: **tba.**

