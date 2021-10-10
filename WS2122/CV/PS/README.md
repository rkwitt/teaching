# Computer Vision (PS)

## News / Important dates

- Begin of lecture: **Oct. 6, 2021**
- Google meet link (for Q&A): here (available once course starts)

## General

The computer vision PS for the winter term 2021/2022 will be held **online** with regular **Q&A sessions**, either in-person or online, depending on how the COVID situation develops in fall. We will decide on the Q&A dates as we progress through the course (but a natural time slot is the assigned time slot for the lecture in PLUS Online).

## Grading

Throughout the PS, you have to solve a series of small/medium-size assignments, related to the content of the lecture. This will mostly be exercises requiring to write Python code. You can work together in groups of **max. size 3**. The first *assignment* will be to get together in groups and enter all group members (only firstname+lastname) into this [spreadsheet](https://myfiles.sbg.ac.at/index.php/s/qE6DYagFcHM9kX5). I trust you that you do not overwrite the membership assignment of the other groups.

### Handing-in Assignments

For each assignment, you will receive (on your official university email account) a unique upload link (each member of a group gets the same link) where you can submit your solution (with format, filename, etc., specified in the assignment). Once the **deadline** for an assignment has passed, I will disable this upload link. Later, you will then receive (again via email) a separate *read-only* link to the same folder where you can see my comments and the number of points achieved. Hence, you can track your number of points throughout the semester. The assignments (see bottom of this page) will mostly come in the form of Jupyter notebooks, where all instructions will be contained.

## Preliminaries: Getting started with PyTorch

I do recommend a setup using [Anaconda Python](https://www.anaconda.com/products/individual). Below is a short how to to install Anaconda + PyTorch on a Mac OS X system.

### Download and install Anaconda

First, download the Anaconda installer (for your system) from [here](https://www.anaconda.com/products/individual). Lets assume the download is stored in the  
`/Users/<USERNAME>/Downloads` folder. We will install Anaconda in `/Users/<USERNAME>/Software/anaconda3` (the following commands use the installer for Mac OS X; please adjust according to your system).

```
cd /Users/<USERNAME>/
mkdir Software
cd Software
mv ~/Downloads/Anaconda3-2021.05-MacOSX-x86_64.sh .
chmod +x Anaconda3-2021.05-MacOSX-x86_64.sh
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

The most recent (stable) version is **1.9** (as of Aug., 25, 2021) which is also what you should see as
the output of the `print` statement).

## Running the course notebooks

The easiest way to run my course notebooks, is to clone my teaching repository
via

```
git clone https://github.com/rkwitt/teaching.git
```

then go to `teaching/WS2122/CV` and start a local Jupyter notebook server via

```
jupyter notebook
```

Basically, a new browser tab (in your default browser) should open where you see the file system
structure of the `teaching/WS2122/CV` folder.

## Assignmentts

| | **Deadline**  | **Points** | **Link** | **Status** |
|---|---|---|---|---|
| Exercise sheet A  | *to be announced*  | **8** (+1)   | [here](ExA/) | *in preparation* |
| Exercise sheet B  | *to be announced*  | **10**       | [here](ExB/) | *in preparation* |
| Exercise sheet C  | *to be announced*  | **8**        | [here](ExC/) | *in preparation* |



