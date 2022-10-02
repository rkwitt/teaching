# Computer Vision (VO)

## News / Important dates

- Begin of lecture: **Oct. 65, 2022 at 8:30am*
- **Location**: T03 (Itzling, Jakob-Haringer Str. 2, FB AIHI/Informatik) 

## General

The computer vision lecture for the winter term 2022/2023 will be held **in-person** (or online, depending on how the COVID situation develops in fall/winter). 

*Many of the lectures are available as pre-recorded videos, from earlier years. You can watch them anytime, but note that some of the content might not exactly match the material presented in the 2022/2023 lecture*.

## Slack

We have a Slack channel `#computervision` on [slack.com](https://visel.slack.com). You can sign up with your `@sbg.ac.at`, `@plus.ac.at`, `@cosy.sbg.ac.at` or your `@stud.sbg.ac.at` email address. This is quite useful, as you can always ask questions, or we can schedule additional online/in-person meetings where I can answer any questions you might have.

## Grading

Grading is based on a **final exam** at the end of the semester, or within the semester break. However, I am quite flexible regarding exam dates and we will definitely find dates that work for everyone. In case we have to switch to an online course due to COVID, the exam will be an **open-book** exam where you can use all the material that you desire. Otherwise, it's just a regular exam.

## Material

One of **literature resources** I do recommend for this course is the [Deep Learning Book](http://www.deeplearningbook.org/) by Goodfellow, Bengio and
Courville (available online) which covers most of the deep learning basics (and more advanced topics as well).

Almost all of my course material is available through **Jupyter notebooks**. Those notebooks can be downloaded from the course's Github repository and also contain links to other resources. To checkout the complete teaching repository (including the material for this semester), use:

```bash
git clone https://github.com/rkwitt/teaching.git
cd teaching/WS2223/CV
```

All notebooks can be found within the `material` subdirectory. Just go the (topic) directory you want, start a Jupyter notebook server and run the notebook via, e.g.:

```bash
cd teaching/WS2223/CV
cd material/01.1_TensorBasics
jupyter notebook
```

## Prerequisites

I do recommend refreshing your **linear algebra**, **statistics** and **analysis** knowledge before starting the course. Also, please make yourself
familiar with Python, as I do use Python almost exclusively (via Jupyter notebooks). Also, you can start reading up on [PyTorch](https://pytorch.org/) which we will use as our environment for implementing deep learning approaches to computer vision.

## PyTorch installation

Currently, the following tutorial videos on installing Anaconda Python and PyTorch are available:

- [**Tutorial** (german)](https://drive.google.com/file/d/1OCG9upipvTwCKdSPm3CIteRbbpuyxyul/view?usp=sharing)
- [**Tutorial** (english)](https://drive.google.com/file/d/1UJgkWttFZ4STwSIT_m-9npnSnsgEW3gd/view?usp=sharing)

## Course topics

Below is a more detailed list of topics covered in the course, subject to change depending
on the progress we make. For many of the topics, I will also provide links to the relevant
papers (primarily in the `papers` sub-directory within each topic-folder).

**Note**: In case you want to watch the videos, please *download* them first. Online viewing is possible (depending on your browser, but quality might be bad, at least this was the feedback I got from previous instances of this course).

- [Introduction & (Computer) vision problems](../material/IntroSlides.pdf)

**Technical preliminaries**

- [**Tensor basics**](../material/01.1_TensorBasics)
  - [Video (Part 1)](https://drive.google.com/file/d/1LX3ChT5pHeVYeKDE4FKXAoOzObo7SsN0/view?usp=sharing)
  - [Video (Part 2)](https://drive.google.com/file/d/1-qzcMGRZnym5GjZwwGhrBzjSvOHekzzY/view?usp=sharing)
- [**Data Handling**](../material/01.2_DataHandling )

## Data

- [Ants/Bees data](https://drive.google.com/open?id=1izFo-gdrxvDy1klIlu-_RZn3JNTaeogg)

## Other useful resources

- [Anaconda](https://www.anaconda.com/distribution/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [scikit-image](http://scikit-image.org/)
- [PyTorch](http://pytorch.org/)
- [Jax](https://jax.readthedocs.io/en/latest/index.html)
- [Convolution arithmetic](https://github.com/vdumoulin/conv_arithmetic)
- [Einops](https://einops.rocks/)
- [Einsum tutorial](https://rockt.github.io/2018/04/30/einsum)