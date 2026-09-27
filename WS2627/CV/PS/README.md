# Computer Vision (PS)

## News / Important dates

- **Begin of PS**: Oct. 7, 2025 (Vorbesprechung/Administrative stuff)
- **Location**: Seminarraum 1 (CPM Building, 1st floor)
- **Time**: 10am

## Grading

Grading is based on short in-class exercises every two-weeks (covering the material from the weeks before, see dates below). To pass the course you have to have at least 50% of all possible points. Then starting at 50% to 100% of all points, grades as spaced linearly. In the remaining time of the PS, we will cover practical aspects (or questions) relating to the
lecture material.

### In-class exercise dates

| **Dates** |
|---|
| Oct. 21, 2026 |
| Nov. 04, 2026 |
| Nov. 18, 2026 |
| Dec. 02, 2026 |
| Dec. 16, 2026 |
| Jan. 13, 2027 |
| Jan. 27, 2027 |

### Policy on the use of AI tools in the PS

For the in-class exercises that determine the grade, no AI tools are allowed.

## Running the VO lecture notebooks

In case you want to prepare for the in-class exercises but going trough (and running) the VO lecture notebooks, I do recommend a setup using [Anaconda Python](https://www.anaconda.com/products/individual). Below is a short guide on how to install Anaconda + PyTorch on a Mac OS X system, including some dependencies (the setup on Linux and Windows systems is pretty similar and very good resources can be found online).

### Download and install Anaconda

First, download the Anaconda installer (for your system) from 
[here](https://www.anaconda.com/products/individual). Let's assume the download is stored in the  
`/Users/<USERNAME>/Downloads` folder. We will install Anaconda in `/Users/<USERNAME>/Software/anaconda3` (the following commands use the installer for Mac OS X; please adjust according to your system).

```bash
cd /Users/rkwitt/Downloads/
wget https://repo.anaconda.com/archive/Anaconda3-2025.06-0-MacOSX-arm64.sh
cd /Users/rkwitt/
mkdir Software
cd Software
mv ~/Downloads/Anaconda3-2025.06-0-MacOSX-arm64.sh .
chmod +x Anaconda3-2025.06-0-MacOSX-arm64.sh
./Anaconda3-2025.06-0-MacOSX-arm64.sh
```

Make sure you correctly specify the destination folder (`/Users/<USERNAME>/Software/anaconda3`) during the installation process. I also do recommend *not* to run the init script at the end of the installation process (we will activate Anaconda by hand later on).

### Activate Anaconda and create an environment

```bash
~/Software/anaconda3/bin/activate
conda create -n "pytorch28" python=3.10
```

### Install dependencies

```bash
~/Software/anaconda3/bin/activate
conda activate pytorch28
pip3 install torch, torchvision, einops, otter-grader, matplotlib, jupyter
```

### Test the installation

In the Python shell, type

```python
import torch
print(torch.__version__)
```