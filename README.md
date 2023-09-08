# Youtube-Data-Harvesting

## Project Descriptions:

#### This app is build for to extract the youtube channel data 

- The problem statement is to create a Streamlit application that allows users to access and analyze data from __YouTube Channels__:
   
   - Using _**Google API** we retrieve all the relevant data for a _**YouTube channel ID**_.
  
        __| Channel name | Subscribers | Total video count | Playlist ID | Video ID | Likes| Comments of each video |__
     
   - Store the data in a MongoDB database.
   - Ability to collect data form the YouTube channels and store them in the data lake by clicking a button.

---

#### To run this app

`python -m streamlit run app.py`

###### or

`streamlit run app.py`

#### NOTE

- provide your api key for the youtube 
- provide your sql user, database name, password.
- provide your mongodb database name.

## Basic Requirements:

- __[Python 3.10](https://docs.python.org/3/)__
- __[googleapiclient](https://developers.google.com/api-client-library)__ 
- __[mysql_connector](https://dev.mysql.com/doc/connector-python/en/)__ 
- __[Pandas](https://pandas.pydata.org/docs/)__
- __[Streamlit](https://docs.streamlit.io/)__
- __[Numpy](https://numpy.org/doc/)__ 
- __[pymongo](https://pymongo.readthedocs.io/en/stable/)__

### To install the basic Requirements

`pip install - r requirements.txt`



