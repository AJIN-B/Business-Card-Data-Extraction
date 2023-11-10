
from streamlit_option_menu import option_menu 
import mysql.connector as my_sql 
from dotenv import load_dotenv
import streamlit as st 
from PIL import Image
import pandas as pd
import numpy as np
import easyocr
import math
import re
import io
import os


load_dotenv()

mydb = my_sql.connect(host=os.getenv('HOST'),user=os.getenv('USER'),
                      password=os.getenv('PASSWORD'),
                      port=os.getenv('PORT'),
                      database =os.getenv('DATABASE_NAME')) 
mycursor = mydb.cursor() 

# reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory

def Find_website(allstring):
    string = allstring.copy()
    for i,s in enumerate(string):
        if s.startswith('www') or s.startswith('https'):
            string.pop(i)
            string.insert(0,s)
            return string
        elif s.endswith('.com') and '@' not in s:
            string.pop(i)
            string.insert(0,s)
            return string
    string.pop()
    string.insert(0,s)
    return string


def Find_mail(allstring):
    string = allstring.copy()
    for i,s in enumerate(string):
        if re.findall('\S+@\S+', s):
            string.pop(i)
            string.insert(0,s)
            return string
    string.pop()
    string.insert(0,s)
    return string


def Find_phone(allstring):
    string = allstring.copy()
    for i,s in enumerate(string):
        if re.findall(r'\+\d+-\d+', s):
            string.pop(i)
            string.insert(0,s)
            return string
        elif re.findall(r'\d+-\d+-\d+', s):
            string.pop(i)
            string.insert(0,s)
            return string
    string.pop()
    string.insert(0,s)
    return string


def Find_name(des,res):
    string = [i[-2] for i in res]
    string.append('None')
    for r in res:
        if r[-2] == des[0]:p = r[0][0];break
    dis = []
    for qq in res:
        q = qq[0][0];dis.append(math.sqrt( ((p[0]-q[0])**2)+((p[1]-q[1])**2)));
    ind = np.argsort(dis)[1]
    string.pop(ind)
    string.insert(0,res[ind][-2])
    return string


def Find_designation(allstring,designations=['manager','hr','data','ceo','founder','executive'] ):
    string = allstring.copy()
    for i,s in enumerate(string):
        for ss in s.split(' '):
            if ss.lower() in designations:
                string.pop(i)
                string.insert(0,s)
                return string
    string.pop()
    string.insert(0,s)
    return string

def Find_Address1(allstring):
    string = allstring.copy()
    for i,s in enumerate(string):
        if re.findall(r'\d\d\d\d\d\d', s):
            s = re.findall(r'[a-zA-Z]+', s)
            if len(s) >= 1:
                string.pop(i)
                string.insert(0,s[0])
                return string
    string.pop()
    string.insert(0,s)
    return string

def Find_Address(allstring):
    string = allstring.copy()
    for i,s in enumerate(string):
        if 'St' in s or 'ST' in s:
            string.pop(i)
            string.insert(0,s)
            return string
    string.pop()
    string.insert(0,s)
    return string
    
def Find_Pincode(allstring):
    string = allstring.copy()
    for i,s in enumerate(string):
        if re.findall(r'\d\d\d\d\d\d', s):
            ss = re.findall(r'\d\d\d\d\d\d', s)[0]
            string.pop(i)
            string.insert(0,ss)
            return string
    string.pop()
    string.insert(0,s)
    return string


st.set_page_config(page_title = 'Business Card Data Extraction' , layout='wide')

st.markdown("<h1 style='text-align: center; color: green;'>Business Card Data Extraction</h1>", unsafe_allow_html=True)
st.markdown("***")


SELECT = option_menu( menu_title = None,orientation="horizontal",
                     options = ["Home","Upload & Extract","Modify","Contact"],
                     icons =["house","cloud-upload-fill",'columns-gap',"envelope-at"],default_index=0,
                     styles={"container": {"padding": "0!important", "background-color": "#6F36AD","size":"cover", "width": "100%"},
                             "icon": {"color": "black", "font-size": "20px"},
                             "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#A2CD5A"}, 
                             "nav-link-selected": {"background-color": "#A2CD5A"}}) 



if SELECT == 'Modify':
    st.markdown("### Modify the Database")
    mycursor.execute("SELECT * FROM data_extract")
    data = mycursor.fetchall()
    columns = ["ID","Name", "Designation", "Company Name", "Email", "Website",
               "Mobile Number1", "Mobile Number2", "Area", "City", "State", 
               "Pin Code", "Image"]
    data_frame = pd.DataFrame(data, columns=columns)
    st.write(data_frame)
    
    # Get the image ID from user input 
    image_id = st.number_input("Enter the ID of the Row to show image", min_value=1)
    
    mycursor.execute("SELECT image FROM data_extract WHERE image_id = %s", (image_id,))
    result = mycursor.fetchone()
    if result is not None:
        image_data = result[0]
        image = Image.open(io.BytesIO(image_data))
        st.image(image, use_column_width=True)
    else:
        st.warning("Image not found for the given ID.")
    
    col1, col2 = st.columns(2)
    with col1:
        id_ = st.number_input("Enter the ID of the entry you want to modify", min_value=1)
        id_ = str(id_)
        
        card_holder = st.text_input("Enter the correct Card Holder Name")
        if not card_holder:
            card_holder = data_frame.loc[data_frame["ID"] == id_, "Name"].item()
        company_name = st.text_input("Enter the correct Company Name")
        if not company_name:
            company_name = data_frame.loc[data_frame["ID"] == id_, "Company Name"].item()
        website = st.text_input("Enter the correct Website URL")
        if not website:
            website = data_frame.loc[data_frame["ID"] == id_, "Website"].item()
        mobile_number1 = st.text_input("Enter the correct Mobile Number1")
        if not mobile_number1:
            mobile_number1 = data_frame.loc[data_frame["ID"] == id_, "Mobile Number1"].item()
        area = st.text_input("Enter the correct Area")
        if not area:
            area = data_frame.loc[data_frame["ID"] == id_, "Area"].item()
        state = st.text_input("Enter the correct State")
        if not state:
            state = data_frame.loc[data_frame["ID"] == id_, "State"].item()
            
    with col2:
        designation = st.text_input("Enter the correct Designation")
        if not designation:
            designation = data_frame.loc[data_frame["ID"] == id_, "Designation"].item()
        email = st.text_input("Enter the correct Email")
        if not email:
            email = data_frame.loc[data_frame["ID"] == id_, "Email"].item()
        mobile_number2 = st.text_input("Enter the correct Mobile Number2")
        if not mobile_number2:
            mobile_number2 = data_frame.loc[data_frame["ID"] == id_, "Mobile Number2"].item()
        city = st.text_input("Enter the correct City")
        if not city:
            city = data_frame.loc[data_frame["ID"] == id_, "City"].item()
        pin_code = st.text_input("Enter the correct Pin Code")
        if not pin_code:
            pin_code = data_frame.loc[data_frame["ID"] == id_, "Pin Code"].item()
    
    if st.button("Modify Data"):
      sql = "UPDATE data_extract SET Company=%s, Name=%s, Designation=%s, Phone1=%s, Phone2=%s, Mail=%s, Website=%s, Area=%s, City=%s, State=%s, Pincode=%s WHERE image_id=%s"
      val = (company_name, card_holder, designation, mobile_number1, mobile_number2, email, website, area, city, state, pin_code, id_)
      mycursor.execute(sql, val)
      mydb.commit()
      st.success("Data modified successfully!")



if SELECT == "Contact":
    aboutme ="I am interested in pursuing a career in data science and waiting for a good opportunity to empower my skills and knowledge.Eagerly to learn and grow in the field of data science\
              and working towards becoming a professional data scientist."
    links={
        "GITHUB": "https://github.com/AJIN-B",
        "LINKEDIN": "https://www.linkedin.com/in/ajin-b-0851191b0/"}
    col1, col2= st.columns(2)
    with col1:
        st.subheader("Ajin B")
        st.subheader("Mail : ajinleo9940@gmail.com")

        S=st.columns(len(links))
        for i, (x, y) in enumerate(links.items()):
            S[i].write(f"[{x}]({y})")
    st.markdown("---")
    st.write(aboutme)
    st.markdown("---")


if SELECT == 'Home':
    st.markdown("---")
    st.markdown("### BizCardX: Extracting Business Card Data with OCR")
    
    st.markdown("#### Motivation : Extract information from business card image and save into a database along with the uploaded image")
    # st.markdown("> Extract information from business card image and save into a database along with the uploaded image")
    st.markdown("##### Description")
    st.markdown("> ##### This application was developed to that, users can upload an image \
                of a business card and extract relevant information from the image.After \
                    the extracted informations will be upload to the database.") 


if SELECT == 'Upload & Extract':
    st.markdown("### Upload a Business Card")
    uploaded_card = st.file_uploader("""For quick extraction of data prefer 
                                     an image of size less than 10 MB""", 
                                     type=["png", "jpeg", "jpg"])
    
    if uploaded_card:
        root = 'C:/Users/ajinl/Downloads/Data/'
        result = reader.readtext(root+uploaded_card.name) # , detail=0
        # DISPLAYING UPLOADED IMAGE
        st.markdown("### Uploaded Image:")
        st.image(uploaded_card.read(),width = 800) # ,width = 250
        
        image_id = uploaded_card.name
        image_id = image_id.split('.')[0]
        
        options = [i[-2] for i in result]
        options.append('None')
        # print(options)

        designation = Find_designation(options)

        name = Find_name(designation,result)
        website = Find_website(options)
        mail = Find_mail(options)
        phone1 = Find_phone(options)
        phone2 = Find_phone(phone1[1:])
        address1 = Find_Address(options)
        address2 = Find_Address1(address1[1:])
        Pincode = Find_Pincode(options)
        
        # print(options)
        
        add = [address1[0],address2[0]]
        full_adress = ','.join(add) if 'None' not in add else add[0] 
        full_adress = re.sub(r'\d\d\d\d\d\d','',full_adress)
        
        # print(full_adress)
        pattern_area=re.compile(r'\b123\s*(?:ABC|global)(?:\s+St\.?)?\b')
        area = re.findall(pattern_area, full_adress)
        
        pattern_city=re.compile(r'Chennai|Erode|Salem|HYDRABAD|Tirupur')
        city = re.findall(pattern_city, full_adress)
        
        pattern_state=re.compile(r'TamilNadu', re.IGNORECASE)
        state = re.findall(pattern_state, full_adress)        
        
        strin = ' '.join(options)
        for i in [name,mail,phone1,area,state,designation,website,phone2,city,Pincode]:
            try:strin = re.sub(i[0],'',strin)
            except:pass
        
        strin = ' '.join(strin.split())
        pattern_company = re.compile(r'\b(selva digitals|GLOBAL INSURANCE|BORCELLE AIRLINES|Family Restaurant|Sun Electricals)\b')
        company_name = re.findall(pattern_company, strin) 
        
        st.markdown("#### Note")
        st.markdown("Please check the extracted infromation given below is correct or not.If its not correct update it with the correct one")
        st.markdown("If you have found any error or no value in the data provided,you can modify it using modify button.But, just before that save the data shown above!") 
        col11, col22 = st.columns(2)

        with col11:
            name_ = st.selectbox("Name",name)
            com_name = st.selectbox("Company Name",company_name)
            mail_ = st.selectbox("Mail",mail)
            phone1_ = st.selectbox("Phone1",phone1)
            address1_ = st.selectbox("Address line 1",address1)
            area_ = st.selectbox("Area",area)
            state_ = st.selectbox("State",state)

        with col22:
            designation_ = st.selectbox("Designation",designation)
            website_ = st.selectbox("Website",website)
            phone2_ = st.selectbox("Phone2",phone2)
            address2_ = st.selectbox("Address line 2",address2)
            city_ = st.selectbox("City",city)
            Pincode_ = st.selectbox("Pincode",Pincode)
            
        up = st.button('Upload')
        if up:
            image_ = open(root+uploaded_card.name,'rb').read()
            mycursor.execute("INSERT IGNORE INTO data_extract (image_id, Name, Designation, Company, Mail, Website, Phone1, Phone2, Area, City, State, Pincode, Image) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(image_id, name_, designation_, com_name, mail_, website_, phone1_, phone2_, area_, city_, state_, Pincode_, image_)) ##create Tabel
            mydb.commit() 
        
            
            

        
