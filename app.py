import checkScore
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import fileupload


with st.sidebar:
    selected = option_menu(menu_title='Main Menu',options=['About','Check Score'])

if selected == 'About':
    st.title('WELCOME TO RESUME SCORE CHECKER ')
    intro = """<!DOCTYPE html>
<html>
<head>
<title>RESUME SCORE CHECKER</title>
</head>
<body>

<h1>RESUME SCORE CHECKER</h1>
<p style="font-family:Trebuchet MS;">Resume Score Checker is designed to scan a job seeker resume template for work experience, skills, education, and other relevant information. It determines if the resume is a good match for the position/Job choosed by the user. It evaluates the resume with the Job Description 
on scale of 100 </p>
<h2>How to check Score ?</h2>
<ol>
<li>Select Job</li>
<li>View Job Description </li>
<li>Upload Resume </li>
<li>Click to view score</li>
</ol>

</body>
</html>"""
    st.components.v1.html(intro, width=None, height=600, scrolling=True)
    #st.markdown(intro,unsafe_allow_html=True)







else:
    st.title('Get Started ... ')
    df = pd.read_csv('cleanedDataJob.csv')
    idx = {}
    cnt = 0
    for i in df['Job ']:
        idx[i] = cnt
        cnt+=1


    option = st.selectbox('Pick One', df['Job '])
    index = idx[option]
    print(index)
    st.write('Job Choosed : ', option)
    if st.button('Click to see Job Decsctiption'):
        st.write('JOB DES')
        #st.write(df.at[option,'des'])
        st.markdown(df.at[index,'des'])
    exp = st.number_input('Experience in (yrs) ', step=1)
    st.write('Experience : ', exp)
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx'])
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        text1 = fileupload.read_resume(bytes_data, uploaded_file.type)
    if st.button('Click to check SCORE'):
        score = checkScore.Check_Score(text1,index,exp)
        st.write('Score : ',round(score,4))