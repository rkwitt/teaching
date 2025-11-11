# Computer Vision (PS)

## News / Important dates

- **Begin of PS**: Oct. 8, 2025 (Vorbesprechung/Administrative stuff)
- **Location**: Seminarraum 1 (CPM Building, 1st floor)
- **Time**: 10am

## Grading

Grading is based on solving programming assignments loosely related to computer vision topics. Solutions are handed in online as Python files and will be **automatically** graded. You will also have the possibility to assess your solutions on your own to check if they are correct. Assignments are published in the form of **exercise sheets**. For each exercise sheet, there exists a separate GitHub repository that explains what needs to be done (in particular, a `README.md` file in each repository).

### Automatic grading

Automatic grading is done via [Otter-Grader](https://otter-grader.readthedocs.io/en/latest/). Each assignment will have automatic tests assigned to it (which you can run yourself) that will be run by me once the deadline for an exercise sheet has passed. *We will go through an example in the first PS*. To set up your environment so that you can start working on the assignments, I have provided an exemplary setup below (adjust to your system).

⚠️ All handed-in exercises have to *pass* the auto-grader, if not, **0 points** will be assigned automatically (hence, I do recommend to test them before handing them in). Please also make sure the file naming, as specified in the exercise sheet, is correct.

### Policy on the use of AI tools in the PS

Students are allowed to use AI tools (e.g., ChatGPT, Copilot, etc.) as **supporting resources** when working on the programming exercises of this PS, however, its use **must be transparently declared** in the handed-in/uploaded submissions. Also, I may ask you to explain, in detail, how your code works, and why you made certain choices. If you **cannot** convincingly (this is the key word here) demonstrate an in-depth understanding of your own solution, your exercise will receive **0 points** regardless of correctness.

*This policy is in accordance with University guidelines, see [here](https://im.sbg.ac.at/spaces/QM/pages/303891131/Leistungs%C3%BCberpr%C3%BCfung?preview=/303891131/490639350/Leitfaden%20KI%20und%20schriftliche%20Arbeiten%20im%20Studium%20v2025-09%20LOGO.pdf)*.

**Recommendation**: Use AI tools only to support your learning (e.g., for debugging, brainstorming, or clarifying concepts), not to replace your own reasoning and problem-solving.

## Preliminaries

I do recommend a setup using [Anaconda Python](https://www.anaconda.com/products/individual). Below is a short guide on how to install Anaconda + PyTorch on a Mac OS X system, including some dependencies (the setup on Linux and Windows systems is pretty similar and very good resources can be found online).

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

## Evaluating your solutions

Let's take as an example *Exercise sheet 1* which you can find below. First, clone the repository (lets assume for simplicity that all is done in `/tmp/`)
as follows:

```bash
cd /tmp/
git clone https://github.com/rkwitt-teaching/CV-2526-ExSheet1
cd CV-2526-ExSheet1
```

In this folder you will find a file `submission.py`. This is the file where you will put your code and which you have to submit later on. *I do recommend you already rename that file to the format `submission_<STUDENTID>.py` replacing `<STUDENTID>` with your actual student ID.* Let's assume this is `1234`.

```bash
mv submission.py submission_1234.py
```

Now, open the file (I do recommend using Visual Studio Code, but feel free to use what you want!). In that file you will find the first assignment:

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

To assess this "solution", run

```bash
~/Software/anaconda3/bin/activate
conda activate pytorch28
otter check submission_1234.py -q t1 
```

## Exercise sheets

|  | Upload link | GitHub repo. | Deadline |
|----------|----------|----------|---------|
| Exercise sheet 1    | [Upload link](https://plusacat-my.sharepoint.com/:f:/g/personal/roland_kwitt_plus_ac_at/EuZfRbFY_rpGtAe8fUiRcmEBN_ZENBtednB_SYVAGDynBg)  | [Repo](https://github.com/rkwitt-teaching/CV-2526-ExSheet1) | Oct-14-2025 (11:59pm) |
| Exercise sheet 2    | [Upload link](https://plusacat-my.sharepoint.com/:f:/g/personal/roland_kwitt_plus_ac_at/EuZfRbFY_rpGtAe8fUiRcmEBN_ZENBtednB_SYVAGDynBg) | [Repo](https://github.com/rkwitt-teaching/CV-2526-ExSheet2) | Nov-04-2025 (11:59pm) |
| Exericise sheet 3   | [Upload link](https://plusacat-my.sharepoint.com/:f:/g/personal/roland_kwitt_plus_ac_at/EhBXcLBJFyNCgmeSNbBq7nMBNOr7725NqnNH1uAjILnBLA) | [Repo](https://github.com/rkwitt-teaching/CV-2526-ExSheet3) | Nov-19-2025 (11:59pm) |

**Status**

*Status updates will be published once automatic grading has finished for each exercise sheet! (Please check regularly)*

Current (anonymized) points can be found here (will be updated as we go along).
