# No More Silence sample dataset. 

This is a sample dataset (currently under construction) version of the full dataset from the No More Silence project, https://www.library.ucsf.edu/archives/aids/data-projects/. This sample dataset has been created to allow workshop attendees, people wanting to assess the value of the dataset for their research use, and other uses that do not require the downloading of the entire dataset. 

This repository also contains the python scripts used to create the sample: create-sample.py which takes 5 items from each collection in the dataset, and gather-files.py which looks for the files themselves (.pdf and .ocr) that correspond to the documents and puts them into a new directory containing only the documents in the sample set. Most users will not need to use these scrips, but they are provided anyway so that people can use them if desired, or tweak them to generate their own version of a sample according to whatever specifications they'd like. They also allow for an examination of how this sample was generated for those who are fluent in python code. 

The sample version of the dataset is the file named NoMoreSilence_SampleData.csv
