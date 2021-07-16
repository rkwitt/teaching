# Machine Learning (VO)

## News

- [Exam PDF](https://drive.google.com/file/d/1yHxGkBrsYIBcjsJwnfFkkf2lyAdMBwOl/view?usp=sharing)
- Exam upload links (for 16.7.2021, 10:00am) sent out
- Exam instructions posted
- Low audio volume issue fixed
- The VO will be held **fully online**
- Our Google meet link for the **Q&A** sessions is [here](https://meet.google.com/zka-jpyj-hmg)

## Scheduled Q&A sessions

- **`06/28/2021`** (11:00am)
- **`06/14/2021`** (11:00am)
- **`05/31/2021`** (11:00am)
- **`04/26/2021`** (11:00am)
- **`04/12/2021`** (11:00am)
- **`03/22/2021`** (11:30am)
- **`03/01/2021`** (11:30am - *Vorbesprechung* VO/PS combined)

## Organization

The course is structured as a series of lectures. For each lecture, I will provide *videos* that can be downloaded and watched whenever you prefer. 

*I do recommend that you watch the lecture videos in the provided order.*

I will also provide, on a regular basis, an **online Q&A session** (via Google meet, see link above), where you can ask questions, or raise issues that have come up while studying the material. My plan is to do this every other week (Mondays 11am). The dates can be found [here](#scheduled-qa-sessions).

## Slack channel

The slack channel #machinelearning is on [`visel.slack.com`](https://visel.slack.com). It should be possible to sign up with your offical University of Salzburg e-mail address ending in `@sbg.ac.at` (`@cosy.sbg.ac.at` and `@stud.sbg.ac.at` work as well).

## Grading

Grading is based on **one final exam** (open-book type) at the end of the course.

### Information for online exam

The exam this year will be an **online**, written exam. It is an **open-book** exam, so you can use 
whatever literature/course material you desire. The procedure is detailed below:

**Each student** who wants to participate in the exam (and is signed up in PLUS Online), do the following:

1. Go to [random.org](https://www.random.org/integer-sets/) and generate 5 (unique) random integers in the range of 1 to 15 (if you obtain duplicates, repeat the procedure to obtain five unique numbers).
2. Send the output (e.g., `2, 4, 6, 8, 12`) to me via e-mail (`Roland.Kwitt@sbg.ac.at`) with the email
subject `ML21 exam sequence`.
3. 10 min. before the exam starts, I will release (on the VO website) a PDF with **15 questions**. Solve the exercises
with the numbers matching your personal random sequence (from Step 2). You have the possibility to switch out **one** question for a question you would rather solve. Please clearly state which question was switched (e.g., `1->10`).
4. Each question should be answered on a **separate page** (annotated with *page number*, *Name* and *Matrikelnummer*).
5. At the end of the exam time, *scan* or *take a picture* of your student ID and all sheets that have relevant content and zip those files.
6. I will either provide (for all signed up students) an upload link that you can use to upload the zip file. If that does not work, the failback option is to send the zip file via email to `Roland.Kwitt@sbg.ac.at` (within a 10 min. time window after the exam has ended).

During the exam, I will be available on **Google Meet** (I will provide a link before the exam starts) for the time 
of the exam, in case there are any questions.

## Lecture material

The course is rather self-contained and most of the material will be developed step-by-step on the blackboard (which is my iPad now :). To every video, I will also provide a PDF with my written notes.

Additionally, you can find most of the material in my supporting [slides](ml.pdf), and in the book by Shalev-Schwartz and Ben-David (see below) which is my main reference for the course.  

### Staying up-to-date

Please, **always check the most recent versions** (since updates might have occurred).
I typically update the slides from time to time to clarify issues raised by the students.
I do recommend that you simpy clone my teaching repository (done once) via

```bash
cd ~/
git clone https://github.com/rkwitt/teaching.git rkwitt-teaching
```

and then regularly do a `git pull`:

```bash
cd ~/rkwitt-teaching
cd SS21
git pull
```

### Lecture videos & Course notes

- **Introduction & Preliminaries**     
  *Some motivation for what we will be talking about; Basics on measurable spaces, measures, measure spaces, measurable functions, probability spaces and random variables*    
  [Video](https://drive.google.com/file/d/1Al2rAMxerJfhejVU0iUeHZ_0LCVqTpCm/view?usp=sharing), [Notes](https://drive.google.com/file/d/1Kmfia-0ZcIPgnGclkP7aq-4Si3365FoL/view?usp=sharing)
- **Formal model & PAC learning**     
  *Introduction to our formal model for learning, generalization error, empirical error, inductive bias & hypothesis classes, realizability assumption, learnability of finite hypothesis classes, PAC learning*  
  [Video (Part A)](https://drive.google.com/file/d/1PG_tPQkOZI04j8UOZxqFx2nGL_0ewgyR/view?usp=sharing), [Video (Part B)](https://drive.google.com/file/d/1CC6eaf0OWwttTl-g5e4b6wMPpKC6e7jG/view?usp=sharing), [Notes](https://drive.google.com/file/d/1Y-KdREhZyqSpMteT85ILMDQS3439sa48/view?usp=sharing)
  
- **Preliminaries (continued)**    
  *Lebesgue integration, expected value, Markov inequality*    
  [Video](https://drive.google.com/file/d/1fMgQeX3juT_TEEQ4YFVlUVOIYjjzFexa/view?usp=sharing), [Notes](https://drive.google.com/file/d/1rvVyYzTf___HPKbshQGfChJW_1m4qyiq/view?usp=sharing)   

- **Agnostic PAC learning & Uniform convergence**    
  *Loss functions, agnostic PAC learning, uniform convergence, agnostic PAC learnability of finite hypothesis classes*.   
   [Video](https://drive.google.com/file/d/13NjZKaOHqkAUrTLKQy7kQ_mphpntowrN/view?usp=sharing), [Notes](https://drive.google.com/file/d/14ONJqJy7mwqDTfcbQbT5R88WUWQ3_HG4/view?usp=sharing), [Errata](agnostic_pac_learning_and_uniform_convergence_ERRATA.pdf)
 
- **No Free Lunch**   
  *Proof of one no free lunch theorem & Implications*     
  [Video](https://drive.google.com/file/d/1BrJMIWwNK14qxhIpkzQsQa_5-PfmSZIP/view?usp=sharing), [Notes](https://drive.google.com/file/d/1e2ARtpIRRg-N5BmtuY-XsYr7dIC45Pd9/view?usp=sharing)
  
- **VC Dimension**   
  *Shattering, VC-dimension (with examples), growth function*            
  [Video (Part A)](https://drive.google.com/file/d/1OPQXGnligzh7Hn2lHj9OAqaWc-1mu70G/view?usp=sharing),  [Video (Part B)](https://drive.google.com/file/d/17_3NWAladZ2FrN-Hbh_csygp9cOAXggz/view?usp=sharing), [Video (Part C)](https://drive.google.com/file/d/1ipD9__HP_SdGcL1QYHo-R_dOga4ISImP/view?usp=sharing), [Video (Part D)](https://drive.google.com/file/d/17vOf-NBEEaOnHTFSeAB97HQX36uSbQyW/view?usp=sharing), [Notes](https://drive.google.com/file/d/1Y07aHDuEshBiOnxeBMPQ9aDlvAAk7uSS/view?usp=sharing)
  
- **Linear predictors**     
  *Halfspaces, Logistic Regression*      
  [Video (Part A)](https://drive.google.com/file/d/1eEooRqc5sv0Q6-E0A6cdqpb7-PHox0rw/view?usp=sharing), [Video (Part B)](https://drive.google.com/file/d/12bgBHBWVeu-Px9GIbJxOERyf-aipGjVC/view?usp=sharing), [Notes](https://drive.google.com/file/d/1jcC0iSLsFYvfRMecGWjs2Xh6hBBEiHrA/view?usp=sharing)

### Books (as reference)

Mohri, Rostamizadeh, Talwakar<br>
**Foundations of Machine Learning**<br>
MIT Press, 2012

Shalev-Schwartz, Ben-David<br>
**Understanding Machine Learning: From Theory to Algorithms**<br>
Cambridge Univ. Press, 2014
