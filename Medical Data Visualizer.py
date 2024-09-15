#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('medical_examination.csv')


# In[8]:


# Convert height from cm to meters and calculate BMI
df['height_m'] = df['height'] / 100
df['BMI'] = df['weight'] / (df['height_m'] ** 2)

# Add the overweight column: 1 if BMI > 25, else 0
df['overweight'] = (df['BMI'] > 25).astype(int)


# In[4]:


# Normalize cholesterol and gluc columns
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# In[6]:


def draw_cat_plot():
    # Create a DataFrame for the cat plot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Rename columns to fit the catplot requirements
    df_cat = df_cat.rename(columns={'variable': 'feature', 'value': 'value'})
    
    # Group and reformat the data for the catplot
    df_cat = df_cat.groupby(['cardio', 'feature', 'value']).size().reset_index(name='count')
    
    # Draw the categorical plot
    fig = sns.catplot(x='feature', hue='value', col='cardio', data=df_cat, kind='count').fig
    plt.show()
    return fig


# In[ ]:


def draw_heat_map():
    # Filter out the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = corr.where(pd.np.triu(pd.np.ones(corr.shape), k=1).astype(bool))
    
    # Set up the matplotlib figure
    plt.figure(figsize=(12, 10))
    
    # Plot the heatmap
    fig = sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="coolwarm", center=0).figure
    plt.show()
    return fig


# In[ ]:




