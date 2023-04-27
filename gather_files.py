import csv
import sys
import os
import shutil

# Have to do this because the fields are too big :shrug:
csv.field_size_limit(sys.maxsize)

files = os.listdir('./NoMoreSilence_Documents/')

errors = 0

os.makedirs('./NoMoreSilence_SampleDocuments', exist_ok=True)

with open('NoMoreSilence_SampleData.csv', 'r') as datafile:
    reader = csv.DictReader(datafile, delimiter=',', quotechar='"')
    for row in reader:
        if row['Local Identifier'] != ' ':
            has_id = 'HAS ID'
            id = row['Local Identifier']
            id_ocr = f"{id}.ocr"
            id_pdf = f"{id}.pdf"
            if id_ocr not in files:
                errors += 1
                print(f"UNABLE TO MATCH FILE: {id}; ({id_ocr})")
            else:
                print(f"gathered ./NoMoreSilence_Documents/{id_ocr} to ./NoMoreSilence_SampleDocuments/{id_ocr}")
                shutil.copy2(f"./NoMoreSilence_Documents/{id_ocr}", f"./NoMoreSilence_SampleDocuments/{id_ocr}")
            if id_pdf not in files:
                print(f"UNABLE TO MATCH FILE: {id}; ({id_pdf})")
            else:
                print(f"gathered ./NoMoreSilence_Documents/{id_pdf} to ./NoMoreSilence_SampleDocuments/{id_pdf}")
                shutil.copy2(f"./NoMoreSilence_Documents/{id_pdf}", f"./NoMoreSilence_SampleDocuments/{id_pdf}")
        if row['Local Identifier'] == ' ':
            has_id = 'NO ID'
            id = row['Title'].split('.')[0]
            id_ocr = f"{id}.ocr"
            id_pdf = f"{id}.pdf"
            if id_ocr not in files:
                errors += 1
                print(f"UNABLE TO MATCH FILE: {row['Title']}")
            else:
                print(f"gathered ./NoMoreSilence_Documents/{id_ocr} to ./NoMoreSilence_SampleDocuments/{id_ocr}")
                shutil.copy2(f"./NoMoreSilence_Documents/{id_ocr}", f"./NoMoreSilence_SampleDocuments/{id_ocr}")
            if id_pdf not in files:
                print(f"UNABLE TO MATCH FILE: {row['Title']}")
            else:
                print(f"gathered ./NoMoreSilence_Documents/{id_pdf} to ./NoMoreSilence_SampleDocuments/{id_pdf}")
                shutil.copy2(f"./NoMoreSilence_Documents/{id_pdf}", f"./NoMoreSilence_SampleDocuments/{id_pdf}")

print(f"Number of files not matched/gathered: {errors}")
