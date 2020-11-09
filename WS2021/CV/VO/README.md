# Computer Vision (VO)

## News / Important dates

- We will start with the first lecture on **Oct. 7, 2020** (online)
- The Google meet link for online meetings can be found [here](https://meet.google.com/dmx-eqme-jqa)

The course will happen **fully online**. I will provide lecture videos as we go along (see below). 

## Slack

We have a Slack channel `#computervision` on [http://visel.slack.com](visel.slack.com). You can sign up with your `@sbg.ac.at`, `@cosy.sbg.ac.at` or your `@stud.sbg.ac.at` email address. This is quite useful, as you can always ask questions, or we can schedule meetings (via Google meet) where I can answer questions you might have.

## Grading

Grading is based on a **final exam** at the end of the semester (typically the first date for the exam is the last lecture, however, we can find a date other than that which works for most students).

## Material

One of the **core resources** of the course is the [Deep Learning Book](http://www.deeplearningbook.org/) by Goodfellow, Bengio and
Courville (available online) which covers most of the deep learning basics.

All \most all of my course material is available through Jupyter notebooks. Those notebooks can be downloaded from the course Github 
repository and also contain links to other resources. To checkout the complete teaching repository (including the WS2021 material), use:

```bash
git clone https://github.com/rkwitt/teaching.git
cd teaching/WS2021/CV
```

All notebooks can be found within the `material` subdirectory. Just go the (topic) directory you want, start 
a Jupyter notebook server and run the notebook via, e.g.:

```bash
cd teaching/WS2021/CV
cd material/01_TensorBasics
jupyter notebook
```

## Prerequisites

I do recommend to refresh your **linear algebra**, **statistics** and
**analysis** knowledge before starting the course. Also, please make yourself
familiar with Python, as I do use Python almost exclusively (via Jupyter notebooks).
I will provide a short introduction in the PS, though. Also, you can start
reading up on PyTorch which we will use as our environment for deep learning.

## PyTorch installation

- [Tutorial](https://drive.google.com/file/d/1W4A1H7CqDgDbVh_1uiWRyVJhYyntjzn4/view?usp=sharing)

## Course topics

Below is a more detailed list of topics covered in the course, subject to change depending
on the progress we make. For many of the topics, I will also provide links to the relevant
papers (primarily in the `papers` sub-directory within each topic-folder).

- [**Introduction & Vision problems**](../material/IntroSlides.pdf)
- [**Tensor basics**](../material/01_TensorBasics)
  - [Lecture video (Part-1)](https://drive.google.com/file/d/1WJ4O-CxwjCVBG90URcWhUW2No4onNCQ4/view?usp=sharing)
  - [Lecture video (Part-2)](https://drive.google.com/file/d/1kNYWZoED0EZP9idpF9BKt20De-haSLiB/view?usp=sharing)
- [**Data Handling**](../material/05_DataHandling)
- [**The perceptron**](../material/03_Perceptron)
  - [Lecture video (Part-1)](https://drive.google.com/file/d/1GYIHBW08pPCQ85yS63p-Bx08tW_7jjVx/view?usp=sharing)
  - [Lecture video (Part-2)](https://drive.google.com/file/d/1ocZ0GGMZai0sOUL0VAp1c2fmCkkAq5Mk/view?usp=sharing)
- [**Automatic differentiation**](https://github.com/rkwitt/teaching/tree/master/WS2021/CV/material/06_AutoGrad)
  - [Lecture video](https://drive.google.com/file/d/1HK097JUSTYC6rSPR2U-DuulnqoGS0Pth/view?usp=sharing)
- [**Gradient-based optimization**](https://github.com/rkwitt/teaching/tree/master/WS2021/CV/material/07_GradientBasedOptimization)
  - [Lecture video (Part-1)](https://drive.google.com/file/d/1oRkuf9aymP8CdEYrKssVoKbTcoKZwcoB/view?usp=sharing)
- [**AdaLine**](https://github.com/rkwitt/teaching/tree/master/WS2021/CV/material/04-AdaLine)
  - Lecture video
- **Multilayer perceptrons (MLPs)**
  - [Lecture video](https://drive.google.com/file/d/1Hm6y6xDo7_oEPzyDY__0Ma2Dbs8Hd72p/view?usp=sharing)
- **Backpropagation**
  - Lecture video
- **Stochastic Gradient Descent (SGD) & Variants**
  - Lecture video
- **Loss functions**
  - Lecture video
- **Residual learning**
  - Lecture video
- **Autoencoding architectures**
  - Lecture video
- **Variational Autoencoders (VAEs)**
  - [Lecture video (Part-1)](https://drive.google.com/file/d/1tEMQXbndM1neWjHLexwCXpq4I0InptjZ/view?usp=sharing)
  - [Lecture video (Part-2)](https://drive.google.com/file/d/1LHaP0ENgHy4H4S8yG6svafQDBul5FDXN/view?usp=sharing)
  - [Lecture video (Part-3)](https://drive.google.com/file/d/1AXoum7JNvSWpGfk1qZ97U_fPWHL4BxHj/view?usp=sharing)
  - Lecture video (Jupyter notebook)
  - Jupyter notebook
- **Adversarial learning**
- **Contrastive learning**

## Data

- [Ants/Bees data](https://drive.google.com/open?id=1izFo-gdrxvDy1klIlu-_RZn3JNTaeogg)

## More useful resources

- [Anaconda](https://www.anaconda.com/distribution/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [scikit-image](http://scikit-image.org/)
- [PyTorch](http://pytorch.org/)
- [Convolution arithmetic](https://github.com/vdumoulin/conv_arithmetic)
