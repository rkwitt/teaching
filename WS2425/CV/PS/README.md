# Computer Vision (PS)

## News / Important dates

- **Begin of lecture**: tba
- **Location**: tba

## Grading

Grading is based on solving programming assignments related to computer vision topics. Solutions are handed-in online as Python files 
and will be automatically graded. You will also have the possibility to assess your solutions on your own to check if they are correct. 
Assignments are published in the form of exercise sheets. For each exercise sheet there exists a seperate GitHub repository that 
explains what needs to be done.

### Automatic grading

Automatic grading is done via [Otter-Grader](https://otter-grader.readthedocs.io/en/latest/). Each assignment will have an automatic
test assigned to it (which you can also run on your own) that will be run by me once the deadline for an exercise sheet has passed. We 
will go through an example in the first PS. To setup your environment so that you can start working on the assignments, I have provided
an exemplary setup below (adjust to your system).

## Preliminaries

I do recommend a setup using [Anaconda Python](https://www.anaconda.com/products/individual). Below is a short how to install Anaconda + PyTorch on a Mac OS X system, including some dependencies.

### Download and install Anaconda

First, download the Anaconda installer (for your system) from [here](https://www.anaconda.com/products/individual). Let's assume the download is stored in the  
`/Users/<USERNAME>/Downloads` folder. We will install Anaconda in `/Users/<USERNAME>/Software/anaconda3` (the following commands use the installer for Mac OS X; please adjust according to your system).

```bash
cd /Users/rkwitt/Downloads/
wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-MacOSX-arm64.sh
cd /Users/rkwitt/
mkdir Software
cd Software
mv ~/Downloads/Anaconda3-2024.06-1-MacOSX-arm64.sh .
chmod +x Anaconda3-2024.06-1-MacOSX-arm64.sh
./Anaconda3-2024.06-1-MacOSX-arm64.sh
```

Make sure you correctly specify the destination folder (`/Users/<USERNAME>/Software/anaconda3`) during the install process. I also do recommend *not* to run the
init script at the end of the installation process.

### Activate Anaconda and create an environment

```bash
~/Software/anaconda3/bin/activate
conda create -n "pytorch23" python=3.10
```

### Install dependencies

```bash
~/Software/anaconda3/bin/activate
conda activate pytorch23
conda install pytorch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 -c pytorch
pip3 install einops, otter-grader, matplotlib
```

### Test the installation

In the Python shell type

```python
import torch
print(torch.__version__)
```

## Evaluating your solutions

Lets take as an example *Exercise sheet 1* which you can find below. First, clone the repository (lets assume for simplicity all is done in `/tmp/`)
as follows:

```bash
cd /tmp/
git clone https://github.com/rkwitt-teaching/CV-2425-ExSheet1.git
cd CV-2425-ExSheet1
```

In this folder you find a file `submission.py`. This is the file where you will put your code and which you have to submit later on. *I do recommend
you already rename that file to the format `submission_<STUDENTID>.py` replacing `<STUDENTID>` with your actual student ID. Lets assume this is 
`1234`. 

```bash
mv submission.py submission_1234.py
```

Now, open the file (I do recommend using Visual Studio Code, but feel free to use what you want!). In that file you find 
the first assignment:

```python
# Exercise 1.1
def assignment_ex1() -> torch.Tensor:
    # YOUR CODE GOES HERE
    pass
```

As a test case, let's just return a 3x3 tensor of all zeros (this is obviously not the correct solution):

```python
# Exercise 1.1
def assignment_ex1() -> torch.Tensor:
    return torch.zeros(3,3)
```

To assess this "solution", run (using the Otter-grader)

```bash
~/Software/anaconda3/bin/activate
conda activate pytorch23
otter check submission_1234.py -q t1 
```

and you will see the test fails! Here `t1` identifies the test for this first assignment (which can be found in `tests/t1.py`). 
If you want to, e.g., run the third test, replace `t1` with `t3`. 


## Exercise sheets

|  | Upload link | GitHub repo. | Deadline |
|----------|----------|----------|---------|
| Exercise sheet 1    | [Upload here](https://plusacat-my.sharepoint.com/:f:/g/personal/roland_kwitt_plus_ac_at/Er6gH4qEOe5OgwCMIVe9KkQBjb4WuKWXwWa6wiG3BILN_w)    | [Repo](https://github.com/rkwitt-teaching/CV-2425-ExSheet1/tree/main)    | tba |
| Exercise sheet 2    | [Upload here](https://plusacat-my.sharepoint.com/:f:/g/personal/roland_kwitt_plus_ac_at/Ehr9cWjH1q1FrfU962BtoqABzNRCMFPLMuUGnWgCsl4JqA)    | [Repo](https://github.com/rkwitt-teaching/CV-2425-ExSheet2) | tba    |