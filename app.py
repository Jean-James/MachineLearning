import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image  #Is used for insert images

# using streamlit we can display analysis and visuals

pickle_in = open("rfr.pkl","rb")
rfr=pickle.load(pickle_in)


def welcome():
    return "Welcome All"

def medical_insurance(age,sex,bmi,children,smoker,region):
    
    """       """
        

   
    prediction=rfr.predict([[age,sex,bmi,children,smoker,region]])
    print(prediction)
    return prediction



def main():
    st.title("Medical Insurance Charges")
    html_temp = """
    <div style="background-color:Green;padding:10px">
    <h2 style="color:white;text-align:center;">Medical Insurance Cost</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age"," ")
    sex = st.text_input("sex"," ")
    bmi = st.text_input("bmi"," ")
    children = st.text_input("children"," ")
    smoker = st.text_input("smoker"," ")
    region = st.text_input("region"," ")
    result=""
    if st.button("Predict"):
        result=medical_insurance(age,sex,bmi,children,smoker,region)
    st.success('The output is {}'.format(result))
    if st.button("More"):
        st.text("Thank You")
        st.text(" ")

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
