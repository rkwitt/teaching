# Creating automatic upload links for submissions

Tested on MAC OS X (Big Sur), running homebrew and Anaconda Python (most recent version as of Feb. '21).

## Prerequisites

1. Install the `owncloud` Python module and the `exchangelib` (verison 3.3.2) Python module via

    ```bash
    pip install pyocclient
    pip install exchangelib==3.3.2
    ```
	
    For the pyocclient (v0.6), you need a fix in the method

	```python
	def share_file_with_link(self, path, **kwargs):
	```

    In particular:

	```python
    if res.status_code == 200:
        tree = ET.fromstring(res.content)
        self._check_ocs_status(tree)
        data_el = tree.find('data')
        data_el_name = data_el.find('name') # NEW
        return ShareInfo(
                            {
                                'id': data_el.find('id').text,
                                'path': path,
                                'url': data_el.find('url').text,
                                'token': data_el.find('token').text,
                                'name': data_el_name.text if data_el_name else # ADJUSTED
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

To send personalized emails with the upload links, use `send_upload_link.py`. *This only works with the PLUS Mail system currently*. Create a config file `email_config.json` with the following content:

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

### Update (May 2022)

Due to the technical inability of the university email service, I have switched to send my automatic 
upload/review links for students via GMAIL (using OAuth2 authentication). A useful resource to setup
GMAIL appropriately can be found [here](https://chozinthet20602.medium.com/sending-email-with-python-using-gmail-api-33628e36306a). 
The functionality of the script above remains the same, only that there is a `--credential_file` cmdline argument now, which
accepts the JSON credentials created (and downloaded) via the Google API.


## Setting upload folder permissions to READ_ONLY

Use 

```bash
python set_read_only.py \
    --config_file myfiles_config.json \
    --root /Uploads/ML-Summer-21/ExA \
    --student_link_file students_ml_summer_21_exA.p
```

This disables any uploads but makes the folders within `/Uploads/ML-Summer-21/ExA` READ_ONLY for students. These folders can then be used to also distribute points and corrections of exercises to students. 

Additionally, `set_read_only.py` updates the pickle file `students_ml_summer_21_exA.p` with read-only links.

## Sending out the read-only links

Finally, you can distribute the read-only links to the students, using syntax similar to `send_upload_links.py`:

```bash
python send_readonly_link.py \
    --config email_config.json \
    --subject Test \
    --subject "Review link for ExA" \
    --student_link_file students_ml_summer_21_exA.p
```
