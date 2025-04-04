#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')


# In[9]:


plt.figure(figsize=(12, 6))
sns.boxplot(x='sex', y='age', hue='survived', data=titanic)
plt.title('Distribution of Age by Gender and Survival Status')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

# Load Titanic data
titanic = sns.load_dataset('titanic')

# ----------- Pie Chart 1: Overall Survival Distribution -----------

survival_counts = titanic['survived'].value_counts()
labels = ['Did Not Survive', 'Survived']
colors = ['lightcoral', 'mediumseagreen']

plt.figure(figsize=(6, 6))
plt.pie(survival_counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Overall Survival Distribution')
plt.axis('equal')
plt.show()

# ----------- Pie Chart 2: Survival by Gender -----------

# Separate by gender and survival
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

for i, gender in enumerate(['male', 'female']):
    gender_data = titanic[titanic['sex'] == gender]
    counts = gender_data['survived'].value_counts()
    labels = ['Did Not Survive', 'Survived']
    axs[i].pie(counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    axs[i].set_title(f'Survival Distribution ({gender.capitalize()})')
    axs[i].axis('equal')

plt.tight_layout()
plt.show()


# In[12]:


import pandas as pd

# Load the Titanic data (replace with your correct path if needed)
titanic = sns.load_dataset('titanic')

# Drop missing ages
age_data = titanic['age'].dropna()

# Calculate IQR
Q1 = age_data.quantile(0.25)
Q3 = age_data.quantile(0.75)
IQR = Q3 - Q1

# Define bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
age_outliers = titanic[(titanic['age'] < lower_bound) | (titanic['age'] > upper_bound)]

# Display them
print(age_outliers[['age', 'sex', 'pclass', 'survived']])


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Set style
sns.set(style="whitegrid")

# Create box plot for 'age' by 'sex'
plt.figure(figsize=(8, 5))
sns.boxplot(x='sex', y='age', data=titanic, palette='pastel', width=0.5)

# Titles and labels
plt.title("Box Plot of Age by Gender (with Outliers)", fontsize=14)
plt.xlabel("Gender")
plt.ylabel("Age")

# Show plot
plt.tight_layout()
plt.show()


# In[ ]:




