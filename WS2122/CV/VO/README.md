# Computer Vision (VO)

## News / Important dates

- Begin of lecture: **Oct. 6, 2021**
- Google meet link (for Q&A): here (available once course starts)

## General

The computer vision lecture for the winter term 2021/2022 will be held **online** with regular **Q&A sessions**, either in-person or online, depending on how the COVID situation develops in fall. We will decide on the Q&A dates as we progress through the course (but a natural time slot is the assigned time slot for the lecture in PLUS Online).

*All lectures are available as pre-recorded videos, so you can watch them anytime.*

## Slack

We have a Slack channel `#computervision` on [http://visel.slack.com](visel.slack.com). You can sign up with your `@sbg.ac.at`, `@cosy.sbg.ac.at` or your `@stud.sbg.ac.at` email address. This is quite useful, as you can always ask questions, or we can schedule additional meetings (via Google meet) where I can answer any questions you might have.

## Grading

Grading is based on a **final exam** at the end of the semester or within the semester break. However, I am quite flexible with respect to that and we will definitely find dates that work for everyone. The exam will be an **open-book** exam where you can use all the material that you desire.

### Information for online exam

**Each student** who wants to participate in the exam (and is signed up in PLUS Online), please do the following:

1. Go to [random.org](https://www.random.org/integer-sets/) and generate 5 (unique) random integers in the range of 1 to 15 (if you obtain duplicates, repeat the procedure to obtain five unique numbers.
2. Send the output (e.g., `2, 4, 6, 8, 12f`) to me via e-mail (`Roland.Kwitt@sbg.ac.at`) with the email
subject `CV2122 exam sequence`.
3. 10 min. before the exam starts, I will release (on this website) a PDF with **15 questions**. Solve the exercises
with the numbers matching your personal random sequence (from Step 2). You have the possibility to switch out **one** question for a question you would rather solve. Please clearly indicate which question was switched.
4. Each question should be answered on a **separate page** (annotated with *page number*, *Name* and *Matrikelnummer*).
5. At the end of the exam time, *scan* or *take a picture* of your student ID and all sheets that have relevant content. Create a PDF `Exam-<YOURSTUDENTNUMBER>.pdf` containing all pages (including the page with your student ID).
6. I will provide (for all signed up students) an *upload link* (to a university-internal MyFiles folder) that you can use to upload the PDF file. If that does not work, the fallback option is to send the PDF file email to `Roland.Kwitt@sbg.ac.at`.

During the exam, I will be available on **Google Meet** (I will provide a link before the exam starts) for the time
of the exam, in case there are any questions.

## Material

One of **resources** I do recommend for the course is the [Deep Learning Book](http://www.deeplearningbook.org/) by Goodfellow, Bengio and
Courville (available online) which covers most of the deep learning basics (and more advanced topics as well).

Almost all of my course material is available through **Jupyter notebooks** (that accompany the lecture videos). Those notebooks can be downloaded from the course Github repository and also contain links to other resources. To checkout the complete teaching repository (including the WS2021 material), use:

```bash
git clone https://github.com/rkwitt/teaching.git
cd teaching/WS2122/CV
```

All notebooks can be found within the `material` subdirectory. Just go the (topic) directory you want, start a Jupyter notebook server and run the notebook via, e.g.:

```bash
cd teaching/WS2122/CV
cd material/01.1_TensorBasics
jupyter notebook
```

## Prerequisites

I do recommend to refresh your **linear algebra**, **statistics** and
**analysis** knowledge before starting the course. Also, please make yourself
familiar with Python, as I do use Python almost exclusively (via Jupyter notebooks). I will provide a short introduction in the PS, though. Also, you can start reading up on PyTorch which we will use as our environment for deep learning.

## PyTorch installation

Currently, the following tutorial video on installing Anaconda Python and PyTorch is only available in *German*.

- [**Tutorial** (german)](https://drive.google.com/file/d/1OCG9upipvTwCKdSPm3CIteRbbpuyxyul/view?usp=sharing)
- [**Tutorial** (english)](https://drive.google.com/file/d/1UJgkWttFZ4STwSIT_m-9npnSnsgEW3gd/view?usp=sharing)

## Course topics

Below is a more detailed list of topics covered in the course, subject to change depending
on the progress we make. For many of the topics, I will also provide links to the relevant
papers (primarily in the `papers` sub-directory within each topic-folder).

**Note**: Please download the videos! Online viewing is possible (depending on your browser, but quality might be bad).

- Introduction & Vision problems

**Technical preliminaries**

- [**Tensor basics**](../material/01.1_TensorBasics)
  - [Video (Part 1)](https://drive.google.com/file/d/1LX3ChT5pHeVYeKDE4FKXAoOzObo7SsN0/view?usp=sharing)
  - [Video (Part 2)](https://drive.google.com/file/d/1-qzcMGRZnym5GjZwwGhrBzjSvOHekzzY/view?usp=sharing)
- [**Data Handling**](../material/01.2_DataHandling )

**Core content**

- [**The perceptron**](../material/02_Perceptron)
  - [Video (Part 1)](https://drive.google.com/file/d/1z3PJJaW_FxzoTsYQyR6xTftVaN3DW045/view?usp=sharing)
  - [Video (Part 2)](https://drive.google.com/file/d/1jU7X9v7JSoi8zGucxe8TifPkAy5enrnd/view?usp=sharing)
- Automatic differentiation
  - [Video](https://drive.google.com/file/d/1P5kKkUzqerHbEb0nuZe1yO-pMyD_hDJ_/view?usp=sharing)
- [Gradient-based optimization](../material/04_GradientBasedOptimization)
- [AdaLine](../material/05_AdaLine)
- [Multilayer perceptrons (MLPs)](../material/06_MLP)
- [Stochastic gradient descent (SGD) & Variants](../material/07_SGD)
- [Convolution(s) & ConvNets](../material/08_ConvNets)
- [Loss functions](../material/09_CrossEntropy)
- [Residual learning (ResNets)](../material/10_ResidualLearning)
- [Model finetuning](../material/11_Finetuning)
- Regularization/Normalization 
- Autoencoders
- Generative models - Variational Autoencoders (VAEs), Generative Adversarial Networks (GANs)
- Transformers for vision (Attention mechanisms)
- [Semantic segmentation](../material/12-Segmentation)
- Object detection (if time allows)

## Data

- [Ants/Bees data](https://drive.google.com/open?id=1izFo-gdrxvDy1klIlu-_RZn3JNTaeogg)

## Other useful resources

- [Anaconda](https://www.anaconda.com/distribution/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [scikit-image](http://scikit-image.org/)
- [PyTorch](http://pytorch.org/)
- [Convolution arithmetic](https://github.com/vdumoulin/conv_arithmetic)
