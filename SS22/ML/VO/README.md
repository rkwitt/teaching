# Machine Learning (VO)

## News

- The Google Meet link for **Q&A** sessions will be available soon!
- The VO will be held **fully online**

## Scheduled Q&A sessions

- **`03/07/2022`** (10:30am - *Vorbesprechung* VO/PS combined)

## Organization

Given the current COVID situation and according to the PLUS guidelines, teaching this course **fully online** seems to be the most reasonable variant.
The course is structured as a series of lectures. For each lecture, I will provide *videos* that can be downloaded and watched whenever you prefer. 

*I do recommend that you watch the lecture videos in the provided order.*

I will also provide, on a regular basis, an **online Q&A session** (via Google meet, see link above), where you can ask questions, or raise issues that have come up while studying the material. My plan is to do this every (or every other) week. The dates can be found [here](#scheduled-qa-sessions).

## Slack channel

The Slack channel #machinelearning is on [`visel.slack.com`](https://visel.slack.com). It should be possible to sign up with your offical University of Salzburg e-mail address ending in `@plus.ac.at` or `@sbg.ac.at` (`@cosy.sbg.ac.at` and `@stud.sbg.ac.at` work as well).

## Grading

Grading is based on **one final exam** (open-book type) at the end of the course.

### Information for online exam

The exam this year will be an **online**, written exam. It is an **open-book** exam, so you can use 
whatever literature/course material you desire. The procedure is detailed below:

**Each student** who wants to participate in the exam (and is signed up in PLUS Online), do the following:

1. Go to [random.org](https://www.random.org/integer-sets/) and generate 5 (unique) random integers in the range of 1 to 15 (if you obtain duplicates, repeat the procedure to obtain five unique numbers).
2. Send the output (e.g., `2, 4, 6, 8, 12`) to me via e-mail (`Roland.Kwitt@plus.ac.at`) with the email
subject `ML22 exam sequence`.
3. 10 min. before the exam starts, I will release (on the VO website) a PDF with **15 questions**. Solve the exercises
with the numbers matching your personal random sequence (from Step 2). You have the possibility to switch out **one** question for a question you would rather solve. Please clearly state which question was switched (e.g., `1->10`).
4. Each question should be answered on a **separate page** (annotated with *page number*, *Name* and *Matrikelnummer*).
5. At the end of the exam time, *scan* or *take a picture* of your student ID and all sheets that have relevant content and zip those files.
6. I will either provide (for all signed up students) an upload link that you can use to upload the zip file. If that does not work, the fallback option is to send the zip file via email to `Roland.Kwitt@plus.ac.at` (within a 10 min. time window after the exam has ended).

During the exam, I will be available on **Google Meet** (I will provide a link before the exam starts) for the time 
of the exam, in case there are any questions.

## Lecture material

The course is rather self-contained and most of the material will be developed *step-by-step* on the blackboard (which is my iPad now :). To every video, I will also provide a PDF with my written notes.

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

- **Introduction & Preliminaries**     
  *Some motivation for what we will be talking about; Basics on measurable spaces, measures, measure spaces, measurable functions, probability spaces and random variables*    
  [Video](https://drive.google.com/file/d/1Al2rAMxerJfhejVU0iUeHZ_0LCVqTpCm/view?usp=sharing), [Notes](https://drive.google.com/file/d/1Kmfia-0ZcIPgnGclkP7aq-4Si3365FoL/view?usp=sharing)

### Books (for reference)

Mohri, Rostamizadeh, Talwakar<br>
**Foundations of Machine Learning**<br>
MIT Press, 2012     
[Online](https://cs.nyu.edu/~mohri/mlbook/)

Shalev-Schwartz, Ben-David<br>
**Understanding Machine Learning: From Theory to Algorithms**<br>
Cambridge Univ. Press, 2014
