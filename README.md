# BizCardX: Extracting Business Card Data with OCR

## Project Descriptions:
#### Developed an Streamlit web application which extracts information from the business cards using Optical Character Recognition (OCR).Using the application the users can upload an image of a business card and extract relevant informations.

### Overview
- Created a Streamlit web application to interact with the user.  
- To extract the information from the image **EASY OCR** library has been used.
- The extracted information should include the company name, card holdername, designation, mobile number, email address, website URL, area, city, state,and pin code.
- Then the information has been display in their particular field if the filed is incorrect user can change the information in the filed.
- The modified data has been stored in a Mysql database.

<h3 align="left">Languages and Tools:</h3>

<p align="left">
   <!-- Python -->
  <a href="https://www.python.org" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  </a>
  
   <!-- Numpy -->
  <a href="https://pytorch.org/" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/numpy/numpy-ar21.svg" alt="Numpy" width="70" height="40"/>
  </a>

   <!-- Pandas -->
  <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/>
  </a>

   <!-- Git -->
  <a href="https://git-scm.com/" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/>
  </a>

   <!-- MySQL -->
  <a href="https://www.mysql.com/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/>
  </a>
  
   <!-- Streamlit -->
  <a href="https://streamlit.io/" target="_blank" rel="noreferrer">
    <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" alt="streamlit" width="70" height="40"/>
  </a>

---

#### To run this app
`python -m streamlit run app.py` **or** `streamlit run app.py`

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


### **Local Setup**:

1. **Clone the Repository**:
```bash
git clone git@github.com:AJIN-B/Business-Card-Data-Extraction.git
cd Business-Card-Data-Extraction
```

2. **Set Up a Virtual Environment** (Optional but Recommended):
```bash
# For macOS and Linux:
python3 -m venv venv

# For Windows:
python -m venv venv
```

3. **Activate the Virtual Environment**:
```bash
# For macOS and Linux:
source venv/bin/activate

# For Windows:
.\venv\Scripts\activate
```

4. **Install Required Dependencies**:
```bash
pip install -r requirements.txt
```

5. **Set up the Environment Variables**:

```bash
# add the following Keys

HOST="Your HOST ID"

USER="Your USER ID"

PASSWORD="Your PASSWORD"

PORT="Your PORT"

DATABASE_NAME="Your DATABASE NAME"

```

6. **Run**:
```bash
python -m streamlit run app.py 
or 
streamlit run app.py
```

After running the command, Streamlit will provide a local URL (usually `http://localhost:8501/`) which you can open in your web browser to access application.

