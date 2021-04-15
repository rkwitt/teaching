import pandas as pd
import numpy as np

def read_students(file):
    """
    Read student information into dictionary, keyed by the student ID, based on a CSV file exported from PLUS online (Remark: as CSV).
    """
    students = dict()
    df = pd.read_csv(file)
    for _, r in df.iterrows():
        students[r['Matrikelnummer']] = {
            'Vorname': r['Vorname'],
            'Nachname': r['Familienname'],
            'email': r['E-Mail'], 
            'group': r['Group'] if ('Group' in df) else -1}
    return students


def read_students_exam(file):
    students = dict()
    df = pd.read_csv(file, sep=";", encoding="iso-8859-1")
    for _, r in df.iterrows():
        students[r['REGISTRATION_NUMBER']] = {
            'Vorname': r['FIRST_NAME_OF_STUDENT'],
            'Nachname': r['FAMILY_NAME_OF_STUDENT'],
            'email': r['EMAIL_ADDRESS'], 
            'group': r['Group'] if ('Group' in df) else -1}
    return students

