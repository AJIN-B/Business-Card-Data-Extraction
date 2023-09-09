# BizCardX: Extracting Business Card Data with OCR

## Project Descriptions:

#### This application was developed to that, users can upload an image of a business card and extract relevant information from the image.After the extracted informations will be upload to the database.

- The problem statement is to create a Streamlit application that allows users can upload an image of a business card and extract relevant information:
   
   - Using _**easy ocr** we retrieve all the text data form the image.
   - The extracted information should include the company name, card holdername, designation, mobile number, email address, website URL, area, city, state,and pin code.
   - Store the data in a Mysql database.

---

#### To run this app

`python -m streamlit run app.py`

###### or

`streamlit run app.py`

#### sample:
![main window](https://github.com/AJIN-B/Business-Card-Data-Extraction/blob/main/main.png?raw=true)

![upload](https://github.com/AJIN-B/Business-Card-Data-Extraction/blob/main/up-ext.png?raw=true)

![modify](https://github.com/AJIN-B/Business-Card-Data-Extraction/blob/main/up.png?raw=true)

#### NOTE

- provide your sql user, database name, password.

## Basic Requirements:

- __[Python 3.10](https://docs.python.org/3/)__
- __[easyocr](https://pypi.org/project/easyocr/)__ 
- __[mysql_connector](https://dev.mysql.com/doc/connector-python/en/)__ 
- __[Pandas](https://pandas.pydata.org/docs/)__
- __[Streamlit](https://docs.streamlit.io/)__
- __[Numpy](https://numpy.org/doc/)__ 
- __[Pillow](https://pypi.org/project/Pillow/)__

### To install the basic Requirements

`pip install - r requirements.txt`



