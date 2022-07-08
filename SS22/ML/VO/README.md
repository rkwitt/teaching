# Machine Learning (VO)

## News

- **Exam (1st): July 13, 2022 at 9:30am** (room **T03**, see PLUS Online) - this is a *regular exam*, not an *open-book* one
- Lecture begins on **Monday, March 7, 2022** at **9am**

## Organization

Given the current COVID + teaching guidelines (see [here](https://www.plus.ac.at/news/lehre-ab-maerz-2022/?pgrp=218&is_paged=0)), the lecture will be held in person. The course is structured as a series of lectures. For each lecture, I will provide *videos* that can be downloaded and watched whenever you prefer. Even though, the lecture is **in person**, students have access to these videos as supplementary material.

*I do recommend that you watch the lecture videos in the provided order.*

## Slack channel

The Slack channel #machinelearning is on [`visel.slack.com`](https://visel.slack.com). It should be possible to sign up with your offical University of Salzburg e-mail address ending in `@plus.ac.at` or `@sbg.ac.at` (`@cosy.sbg.ac.at` and `@stud.sbg.ac.at` work as well).

## Grading

Grading is based on **one final exam** at the end of the course.

## Lecture material

The course is rather self-contained and most of the material will be developed *step-by-step* on the blackboard (which was my iPad for a long time now :). To every video, I will also provide a PDF with my written notes.

Additionally, you can find much of the material in my supporting [slides](ml.pdf), and in the book by Shalev-Schwartz and Ben-David (see below), which is my main reference for the course. Another awesome book (although in slightly different notation here and there) is by Mohri, Rostamizadeh & Talwakar (see also below).

### Staying up-to-date

Please, **always check the most recent version** (since updates might have occurred) of this repository.
I do recommend that you simply clone my teaching repository (done once) via

```bash
cd ~/
git clone https://github.com/rkwitt/teaching.git rkwitt-teaching
```

and then regularly do a `git pull`:

```bash
cd ~/rkwitt-teaching
cd SS22
git pull
```

### Lecture videos & Course notes

*For reference, below you find videos (for most parts) of the material covered in the lecture. Some videos are from earlier years. In addition, you can also find my notes during the lecture (including the ones from earlier years). On some topics, my notes for 2022 differ to the 2021 notes, as I have left out some parts. Relevant to the exam is obviously only the material covered in the summer term 2022.* 


- **Introduction & Preliminaries**     
  *Some motivation for what we will be talking about; Basics on measurable spaces, measures, measure spaces, measurable functions, probability spaces and random variables*    
  [Video](https://drive.google.com/file/d/1Al2rAMxerJfhejVU0iUeHZ_0LCVqTpCm/view?usp=sharing), [Notes 2021](https://drive.google.com/file/d/1Kmfia-0ZcIPgnGclkP7aq-4Si3365FoL/view?usp=sharing)

- **Formal model & PAC learning**     
  *Introduction to our formal model for learning, generalization error, empirical error, inductive bias & hypothesis classes, realizability assumption, learnability of finite hypothesis classes, PAC learning*  
  [Video (Part A)](https://drive.google.com/file/d/1PG_tPQkOZI04j8UOZxqFx2nGL_0ewgyR/view?usp=sharing), [Video (Part B)](https://drive.google.com/file/d/1CC6eaf0OWwttTl-g5e4b6wMPpKC6e7jG/view?usp=sharing), [Notes 2021](https://drive.google.com/file/d/1Y-KdREhZyqSpMteT85ILMDQS3439sa48/view?usp=sharing)
  
- **Preliminaries (continued)**    
  *Lebesgue integration, Expected value, Markov inequality*    
  [Video](https://drive.google.com/file/d/1fMgQeX3juT_TEEQ4YFVlUVOIYjjzFexa/view?usp=sharing), [Notes 2021](https://drive.google.com/file/d/1rvVyYzTf___HPKbshQGfChJW_1m4qyiq/view?usp=sharing)   
  
- **Agnostic PAC learning & Uniform convergence**    
  *General loss functions, agnostic PAC learning, uniform convergence, agnostic PAC learnability of finite hypothesis classes*.   
   [Video](https://drive.google.com/file/d/13NjZKaOHqkAUrTLKQy7kQ_mphpntowrN/view?usp=sharing), [Notes 2021](https://drive.google.com/file/d/14ONJqJy7mwqDTfcbQbT5R88WUWQ3_HG4/view?usp=sharing), [Errata](agnostic_pac_learning_and_uniform_convergence_ERRATA.pdf)

- **No-Free-Lunch (NFL)**   
  *Proof of one no free lunch theorem & Implications, Bias/Complexity tradeoff*  
  [Video](https://drive.google.com/file/d/1BrJMIWwNK14qxhIpkzQsQa_5-PfmSZIP/view?usp=sharing), [Notes 2021](https://drive.google.com/file/d/1e2ARtpIRRg-N5BmtuY-XsYr7dIC45Pd9/view?usp=sharing), [Notes 2022](NFL-Notes-2022.pdf )

- **VC Dimension**     
  *Shattering, VC Dimension, Fundamental theorem of statistical learning*      
  [Video (Part A)](https://drive.google.com/file/d/1OPQXGnligzh7Hn2lHj9OAqaWc-1mu70G/view?usp=sharing),  [Video (Part B)](https://drive.google.com/file/d/17_3NWAladZ2FrN-Hbh_csygp9cOAXggz/view?usp=sharing), [Video (Part C)](https://drive.google.com/file/d/1ipD9__HP_SdGcL1QYHo-R_dOga4ISImP/view?usp=sharing), [Video (Part D)](https://drive.google.com/file/d/17vOf-NBEEaOnHTFSeAB97HQX36uSbQyW/view?usp=sharing), [Notes 2021](https://drive.google.com/file/d/1Y07aHDuEshBiOnxeBMPQ9aDlvAAk7uSS/view?usp=sharing), [Notes 2022](VCDimension-Notes-2022.pdf)

- **Linear predictors**     
  *Halfspace classifiers (+ Logistic regression; not covered 2022)*     
  [Video (Part A)](https://drive.google.com/file/d/1eEooRqc5sv0Q6-E0A6cdqpb7-PHox0rw/view?usp=sharing), [Video (Part B)](https://drive.google.com/file/d/12bgBHBWVeu-Px9GIbJxOERyf-aipGjVC/view?usp=sharing), [Notes 2021](https://drive.google.com/file/d/1jcC0iSLsFYvfRMecGWjs2Xh6hBBEiHrA/view?usp=sharing), [Notes 2022](LinearPredictors-Notes.pdf)

- **Boosting**
  *AdaBoost*

### Books (for reference)

Mohri, Rostamizadeh, Talwakar<br>
**Foundations of Machine Learning**<br>
MIT Press, 2012     
[Online](https://cs.nyu.edu/~mohri/mlbook/)

Shalev-Schwartz, Ben-David<br>
**Understanding Machine Learning: From Theory to Algorithms**<br>
Cambridge Univ. Press, 2014
