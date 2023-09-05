# Computer Vision (PS)

## News / Important dates

- **Begin of lecture**: Oct. 4, 2023 at 10:30am
- **Location**: Rechnerübungsraum (Itzling, Jakob-Haringer Str. 2, FB AIHI/Informatik) 

## Grading

At the beginning of the PS, you will get a selection of influential (recent) research papers from which you can choose one. Work through the paper, implement it (or large parts of it, based on publicly-available reference implementation(s)), and experiment with the approach - try to reproduce some (or all) experiments of the paper, or be creative and think about new, alternative things you can test. Working on toy examples, e.g., using synthetic data is fine. Then write up a summary of the paper, explain the key ideas and document your results and findings. This report should not be more than 8 pages (excluding references). Grading will be based on the quality of the handed-in report (including the documented source code). You can also base your code off of some pre-existing code (e.g., from GitHub), but make sure you understand what's going on - otherwise, it will be very hard to do any serious experiments with it. 

**Note**: you can work together in groups of max. size **three**. Please enter your group members (and paper title) in this Excel spreadsheet [here](https://myfiles.sbg.ac.at/index.php/s/PzZkbNt92XxfBHQ) by Oct. 11, 2023.

*Each week, during the PS, I will meet with 2 groups (for 30 minutes each) and offer in-person support, explanations, etc. for the project.*

### Selection of research papers

will be announced at the beginning of the PS.

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
