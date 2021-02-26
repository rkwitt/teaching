# Computer Vision (VO)

## News / Important dates

- **1st exam date: Fri., Feb. 26, 10:00am** (2hrs) (Google meet link for questions during exam is [here](https://meet.google.com/jtr-srkm-kdp))
- We will start with the first lecture on **Oct. 7, 2020** (online)
- The Google meet link for online meetings can be found [here](https://meet.google.com/dmx-eqme-jqa)
- Exam [link](https://drive.google.com/file/d/1wRWgC-dlHGUT9nP8cjNUJ6igqDnCBTE4/view?usp=sharing)

The course will happen **fully online**. I will provide lecture videos as we go along (see below). 

## Slack

We have a Slack channel `#computervision` on [http://visel.slack.com](visel.slack.com). You can sign up with your `@sbg.ac.at`, `@cosy.sbg.ac.at` or your `@stud.sbg.ac.at` email address. This is quite useful, as you can always ask questions, or we can schedule meetings (via Google meet) where I can answer questions you might have.

## Grading

Grading is based on a **final exam** at the end of the semester (typically the first date for the exam is the last lecture, however, we can find a date other than that which works for most students).

### Information for exam

The exam is an **open-book** exam, i.e., you can use whatever material you want. I will provide a Google meet link so that you can ask questions during the exam. 

The **procedure** (step-by-step) is as follows:

1. Sign up for exam in PLUS Online
2. Send me (by e-mail) a list of 5 random integers (e.g., using [random.org](https://www.random.org/integers/)) in the range 1-15
3. On the exam date, you will get the PDF with *all* questions via e-mail (about 10min before the exam starts)
4. You answer the five questions that correspond to your sequence of random integers (one sheet of paper per question)
5. Write your *full name* and *student number* on all sheets of paper
6. Scan all the pages (or take a picture of sufficient quality)
7. Send me the scans per e-mail *before* the exam ends

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
  - [Lecture video](https://drive.google.com/file/d/1oRkuf9aymP8CdEYrKssVoKbTcoKZwcoB/view?usp=sharing)
- [**AdaLine**](https://github.com/rkwitt/teaching/tree/master/WS2021/CV/material/04-AdaLine)
  - Lecture video
- [**Multilayer perceptrons (MLPs)**](../material/09_MLP)
  - [Lecture video](https://drive.google.com/file/d/1Hm6y6xDo7_oEPzyDY__0Ma2Dbs8Hd72p/view?usp=sharing)
- [**Stochastic Gradient Descent (SGD) & Variants**](../material/08-SGD)
  - [Lecture video (Part-1)](https://drive.google.com/file/d/16-jP3hPU3z5S8L4holmxRAqlc7dckH9y/view?usp=sharing)
  - [Lecture video (Part-2)](https://drive.google.com/file/d/1lLgKoJoYUIKH-1QH32KsWTVOpU4OtFxz/view?usp=sharing)
- [**Convolution**](../material/10-ConvNets)
  - [Lecture video (Part-1)](https://drive.google.com/file/d/1iAiik5TRq6AumtIUrjQJNPrcZ0GGA10P/view?usp=sharing)
- **Loss functions**
  - [Cross-Entropy (Binary/Multi-Class)](../material/11-CrossEntropy)
    - [Lecture video (Part-1)](https://drive.google.com/file/d/1PztaJGiFN2iwBWCEesc7AOEGF_wvBdcV/view?usp=sharing)
  - Supervised contrastive loss
    - [Lecture video](https://drive.google.com/file/d/1D1sV4AX5agI42y2AwNgul1zgJDPGY7yY/view?usp=sharing)
- [**Residual learning**](../material/12-ResidualLearning)
  - [Lecture video](https://drive.google.com/file/d/1itWV0V9rEwvQ2r-PJLyipdPfFTNAkcfC/view?usp=sharing), [Google Colab Video](https://drive.google.com/file/d/1vn9XPX5ijzrhzccObolfbq0EaQE9MI7r/view?usp=sharing), [Paper](https://arxiv.org/abs/1512.03385)
- Regularization/Normalization & Fine-Tuning
    - Lecture video
- **Autoencoders**
  - Lecture video
- **Variational Autoencoders (VAEs)**
  - [Lecture video (Part-1)](https://drive.google.com/file/d/1tEMQXbndM1neWjHLexwCXpq4I0InptjZ/view?usp=sharing)
  - [Lecture video (Part-2)](https://drive.google.com/file/d/1LHaP0ENgHy4H4S8yG6svafQDBul5FDXN/view?usp=sharing)
  - [Lecture video (Part-3)](https://drive.google.com/file/d/1AXoum7JNvSWpGfk1qZ97U_fPWHL4BxHj/view?usp=sharing)
  - Lecture video (Part-4)

## Data

- [Ants/Bees data](https://drive.google.com/open?id=1izFo-gdrxvDy1klIlu-_RZn3JNTaeogg)

## More useful resources

- [Anaconda](https://www.anaconda.com/distribution/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [scikit-image](http://scikit-image.org/)
- [PyTorch](http://pytorch.org/)
- [Convolution arithmetic](https://github.com/vdumoulin/conv_arithmetic)
