#!/usr/bin/env python
# coding: utf-8

# In[67]:


print('Name : ')
print('Plot a line graph to find the average cholestrol found in various age groups')
print('Plot a line graph to find the correlation between systolic and diastolic blood pressure found in various age groups')


# In[1]:


#Task 1 
#Import all the libraries and read cardiovascular.csv
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('cardiovascular.csv')
df

#Task 2 
#Group by age and find the average cholesterol and make a dataframe out of it
group_by_age = df.groupby('age')['cholesterol'].mean().reset_index()
group_by_age

#Task 3 
#Plot a line graph for various age group and their cholesterol 
label = group_by_age['age']
value = group_by_age['cholesterol']

fig = plt.subplots(figsize=(19,8))

plt.plot(label, value, label = "Average Cholesterol" , linewidth=3.0)
plt.xlabel('age')
plt.xticks(rotation='vertical')

plt.ylabel('cholesterol')

plt.title('Average Cholesterol', fontsize=20)

plt.legend()

plt.show()


# # Average cholestrol found in various age groups

# In[2]:





# In[3]:





# Conclusion - 

# # Correlation between systolic and diastolic blood pressure

# In[84]:


# Diastolic blood pressure - is the pressure in the arteries when the heart rests between beats
# Systolic blood pressure - the pressure in your arteries when your heart beats

#predefine code for image
from IPython.display import Image
Image(filename='blood pressure readings chart.jpg') 
#predefine code end


# In[4]:


#Task 4
#Group by age and find maximum systolic blood pressure and create a dataframe project out of it


# In[5]:


#Task 5
#Group by age and find maximum diastolic blood pressure and create a dataframe project out of it


# In[6]:


#Task 6
#Plot a line graph to show a Correlation between systolic and diastolic blood pressure


# Conclusion - 

# In[ ]:




