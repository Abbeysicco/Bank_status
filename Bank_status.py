import pandas as pd
import numpy as np
import pickle
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

# Giving a title
st.header('Bank Status Prediction')

    # Getting input Values from the User
country = st.text_input('country')
year = st.text_input('year')
location_type = st.text_input('location_type')
cellphone_access = st.text_input('cellphone_access')
household_size = st.text_input('household_size')
age_of_respondent = st.text_input('age_of_respondent')
gender_of_respondent = st.text_input('gender_of_respondent')
relationship_with_head = st.text_input('relationship_with_head')
marital_status = st.text_input('marital_status')
education_level = st.text_input('education_level')
job_type = st.text_input('job_type')


#load model
model_file=open('rand_model.pkl','rb')
model=pickle.load(model_file)


def predict_value(user_input_value):  
    try:  
        user_input = np.array(user_input_value)  
        user_input_reshaped = user_input.reshape(1, -1)  

        # Predicting the model  
        predicted = model.predict(user_input_reshaped)  
        print(f"Predicted value: {predicted}")  

        # Customize result for bank Account Status   
        return 'Bank Account is a Yes' if predicted[0] == 1 else 'Bank Account is a No'  
    except Exception as e:  
        return f"An error occurred during prediction: {e}" 

def main():
    # Code for prediction
    if st.button('Bank Status Prediction'):
        predict_c=predict_value([country, year, location_type, cellphone_access, household_size, age_of_respondent,
                  gender_of_respondent, relationship_with_head, marital_status, education_level, job_type])
        st.success(predict_c)

if __name__ == "__main__":
    main()