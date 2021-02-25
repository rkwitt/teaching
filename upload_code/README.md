# Creating automatic upload links for submissions

Tested on MAC OS X (Big Sur), running homebrew and Anaconda Python (most recent version as of Feb. '21).

## Prerequisites

1. Install the `owncloud` Python module via

    ```bash
    pip install pyocclient
    ```

2. Go to 

    `myfiles.sbg.ac.at`

    and login with your PLUS credentials. Create a *base folder* in which all submissions will be stored, e.g., `Uploads`.

3. Go to `Settings` -> `Security` and create an App password by assigning some *name* (e.g., `uploadcode`) and clicking on *Create new app password*. This password is needed in the next step.

4. Set up a config file, e.g., `config.json`

    ```bash
    touch myfiles_config.json
    ```

    and fill this file in the form

    ```bash
    {
        "url"     : "https://myfiles.sbg.ac.at/",
	    "user"    : <YOUR USER ID>,
	    "app_key" : <YOUR APPLICATION PASSWORD>
    }
    ```

## Creating sub-folders

To create a sub-folder, use `create_dir.py`. E.g., if you already have a folder `Uploads/ML-Summer-21` and you want to create a sub-folder named `ExA`, execute: 

```bash
python create_dir.py \
    --root /Uploads/ML-Summer-21/ \
    --config_file myfiles_config.json \
    --dir ExA/
```

## Creating upload links

Next, we can create upload links. First, download all participants of a lecture/PS/etc. as a **CSV** file (not *XML* and not *CSV for Excel*), e.g., saved to `student_info.csv`.

**Remark**: It is possible to also use CSV files exported from the exam control panel in PLUS online, where you only have the option to export *CSV for Excel*. These CSV files obviously :) differ from the classic student listing in PLUS Online courses. However, the `create_links.py` code also supports an `--exam` option which allows to use those CSV files as well. 

### Groups

In case students form groups, open the file and add a last column `Group` with integers indicating group membership.

### Link creation

```bash
python create_links.py \
    --root /Uploads/ML-Summer-21/ExA \
    --config_file myfiles_config.json \
    --student_file student_info.csv \
    --out_file students_ml_summer_21_exA.p
```

This will create upload links for each student. In case of groups, mupliple students share an upload link (i.e., the students in one particular group). All information is stored in a `pickle` file (here: `students_ml_summer_12_exA.p`). 

## Sending out upload links

To send personalized emails with the upload links, use `send.py`. *This only works with the PLUS Mail system currently*. Create a config file `email_config.json` with the following content:

```json
{
	"username"     : <USERNAME>,
	"password"     : <PASSWORD>,
	"email" 	   : <FIRSTNAME>.<LASTNAME>@sbg.ac.at
}
```
While this stores passwords in plaintext, it's fairly straightforward to replace the corresponding lines in `send.py` that reads the password from the JSON file by a call to 

```python
from getpass import getpass
...
pwd = getpass()
```


Then execute the `send.py` script as follows:

```bash
python send.py \
    --config_file email_config.json \
    --subject "Upload link for ExA" \
    --student_link_file students_ml_summer_21_exA.p
```

Adjust the `--subject` argument accordingly. As `students_ml_summer_21_exA.p` contains all the relevant student information and link details, this allows to create automatic emails per student, notifying the student about his/her upload link.