# Computer Vision (VO)

## Exam dates

|  | Date, Time, Place |
|--------|----------------|
| 1st exam date  | tba |
| 2nd exam date  | tba |
| 3d exam date   | tba |

## News / Important dates

- **Begin of lecture**: Oct. 1st, 2025 (Vorbesprechung/Administrative stuff)
- **Location**: Rechnerraum, Jakob-Haringer Str. 2

## General

*Many of the lectures are available as pre-recorded videos from previous (COVID) years. You can watch them anytime, but note that part of the material might not exactly match the material presented in the 2025/2026 lecture and that there will be additional content this year.*

## Slack

We have a Slack channel `#computervision` on [slack.com](https://visel.slack.com). You can sign up with your `@sbg.ac.at`, `@plus.ac.at`, `@cosy.sbg.ac.at` or your `@stud.sbg.ac.at` email address. This is quite useful as you can always ask questions, or we can schedule additional online/in-person meetings where I can answer any questions you might have.

## Grading

Grading is based on a **final exam** at the end of the semester or within the semester break. However, I am quite flexible regarding exam dates, and we will find dates that work for everyone.

## Material

One of the **literature resources** I do recommend for this course is the [Deep Learning Book](http://www.deeplearningbook.org/) by Goodfellow, Bengio and Courville (available online) which covers most of the deep learning basics (and more advanced topics as well).

Almost all of my course material is available through **Jupyter notebooks**. Those notebooks can be downloaded from the course's Github repository and also contain links to other resources. To check out the complete teaching repository (including the material for this semester), use:

```bash
git clone https://github.com/rkwitt/teaching.git
cd teaching/WS2526/CV
```

All notebooks can be found within the `material` subdirectory. Just go to the (topic) directory you want, start a Jupyter notebook server and run the notebook via, e.g.:

```bash
cd teaching/WS2526/CV
cd material/01.1_TensorBasics
jupyter notebook
```

## Prerequisites

I do recommend refreshing your **linear algebra**, **statistics** and **analysis** knowledge before starting the course. Also, please make yourself familiar with Python as I do use Python almost exclusively (via Jupyter notebooks). Besides, you can start reading up on [PyTorch](https://pytorch.org/) which we will use as our environment for implementing deep learning approaches to computer vision.

## Course topics

Below is a more detailed list of topics covered in the course, subject to change depending on the progress we make. For many of the topics, I will also provide links to the relevant papers (primarily in the `papers` sub-directory within each topic-folder).

**Note**: In case you want to watch the videos, please *download* them first. Online viewing is possible (depending on your browser, but quality might be bad, at least this was the feedback I got from previous instances of this course).

- [**Introduction & Computer vision problems**](../material/IntroSlides.pdf)

## Material

### Prelimiaries

- [**Tensor basics**](../material/01.1_TensorBasics)

### Topics

## Data

- [Ants/Bees data](https://drive.google.com/open?id=1izFo-gdrxvDy1klIlu-_RZn3JNTaeogg)

## Other useful resources

- [Anaconda](https://www.anaconda.com/download/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [scikit-image](http://scikit-image.org/)
- [PyTorch](http://pytorch.org/)
- [Jax](https://jax.readthedocs.io/en/latest/index.html)
- [Convolution arithmetic](https://github.com/vdumoulin/conv_arithmetic)
- [Einops](https://einops.rocks/)
- [Einsum tutorial](https://rockt.github.io/2018/04/30/einsum)
