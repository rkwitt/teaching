# Computer Vision (VO)

## News / Important dates

Available at the end of the (summer) term break (September).

## Slack

We have a Slack channel `#computervision` on [http://visel.slack.com](visel.slack.com). You can sign up with your `@sbg.ac.at`, `@cosy.sbg.ac.at` or your `@stud.sbg.ac.at` email address. This is quite useful, as you can always ask questions, or we can schedule meetings (via Google meet) where I can answer questions you might have.

## Grading

Grading is based on a **final exam** at the end of the semester (typically the first date for the exam is the last lecture, however, we can find a date other than that which works for most students).

## Material

One of the **core resources** of the course is the [Deep Learning Book](http://www.deeplearningbook.org/) by Goodfellow, Bengio and
Courville (available online) which covers most of the deep learning basics.

Almost all of my course material is available through Jupyter notebooks. Those notebooks can be downloaded from the course Github
repository and also contain links to other resources. To checkout the complete teaching repository (including the WS2021 material), use:

```bash
git clone https://github.com/rkwitt/teaching.git
cd teaching/WS2122/CV
```

All notebooks can be found within the `material` subdirectory. Just go the (topic) directory you want, start a Jupyter notebook server and run the notebook via, e.g.:

```bash
cd teaching/WS2122/CV
cd material/01_TensorBasics
jupyter notebook
```

## Prerequisites

I do recommend to refresh your **linear algebra**, **statistics** and
**analysis** knowledge before starting the course. Also, please make yourself
familiar with Python, as I do use Python almost exclusively (via Jupyter notebooks). I will provide a short introduction in the PS, though. Also, you can start reading up on PyTorch which we will use as our environment for deep learning.

## PyTorch installation

Currently, the following tutorial video on installing Anaconda Python and PyTorch is only available in *German*. 

- [Tutorial](https://drive.google.com/file/d/10zHkyBmyxlaSF6u9FPgOPP7Uw9ztQyJ-/view?usp=sharing)

## Course topics

Below is a more detailed list of topics covered in the course, subject to change depending
on the progress we make. For many of the topics, I will also provide links to the relevant
papers (primarily in the `papers` sub-directory within each topic-folder).

*Videos will be available at the beginning of the winter term!*

- Introduction & Vision problems

**Technical preliminaries**

- [Tensor basics](material/01_TensorBasics)
  - [Video (Part 1)](https://drive.google.com/file/d/1m70fcZylLI6310rZnQXbloMuatUHwz2N/view?usp=sharing)
  - [Video (Part 2)](https://drive.google.com/file/d/1GVWYzyqxNFvWDfR2HJqotGkjRAuadiTS/view?usp=sharing)
- Data Handling

**Core content**

- [The perceptron](material/02_ThePerceptron)
  - [Video (Part 1)](https://drive.google.com/file/d/1enV2K_-UVziiPHuTxW7k2PmZ71YA9pqJ/view?usp=sharing)
  - [Video (Part 2)](https://drive.google.com/file/d/1BSw3L6EhlZSlCAIl83MBSFGCHSU99CRd/view?usp=sharing)
- Automatic differentiation
- Gradient-based optimization
- AdaLine
- Multilayer perceptrons (MLPs)
- Stochastic Gradient Descent (SGD) & Variants
- Convolution(s)
- Loss functions
- Residual learning
- Regularization/Normalization & Fine-Tuning
- Autoencoders
- Generative models - Variational Autoencoders (VAEs)
- Image segmentation
- Object detection

## Data

- [Ants/Bees data](https://drive.google.com/open?id=1izFo-gdrxvDy1klIlu-_RZn3JNTaeogg)

## Other useful resources

- [Anaconda](https://www.anaconda.com/distribution/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [scikit-image](http://scikit-image.org/)
- [PyTorch](http://pytorch.org/)
- [Convolution arithmetic](https://github.com/vdumoulin/conv_arithmetic)
