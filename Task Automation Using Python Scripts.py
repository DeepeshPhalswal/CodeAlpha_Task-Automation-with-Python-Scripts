#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


def clean_and_preprocess_data(customers_data):    # Assume customers_data is a DataFrame containing customer information

    # Drop rows with missing values
    student_data.dropna(inplace=True)

    # Convert 'Name' column to uppercase
    student_data['Name'] = student_data['Name'].str.upper()   
    
    # Convert 'REGNO' column to numeric format
    student_data['Regno'] = pd.to_numeric(student_data['Regno'], errors='coerce')

    # Convert 'Gender' column to lowercase
    student_data['Gender'] = student_data['Gender'].str.lower()

    # Convert 'Join Date' column to datetime format
    student_data['Join Date'] = pd.to_datetime(student_data['Join Date'])

    return student_data


# In[5]:


student_data = pd.DataFrame({
    'Name': ['John', 'Jane', 'Alex'],
    'Regno': [25, None, 30],
    'Gender': ['Male', 'Female', None],
    'Join Date': ['2024-01-01', '2024-02-15', '2024-03-10']
})


# In[7]:


# Clean and preprocess the data
cleaned_student_data = clean_and_preprocess_data(student_data)


# In[8]:


# Display the cleaned and preprocessed data
print(cleaned_student_data)


# In[ ]:




