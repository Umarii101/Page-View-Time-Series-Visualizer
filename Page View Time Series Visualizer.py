#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# Load the data
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean the data by filtering out top and bottom 2.5% of page views
q_low = df['value'].quantile(0.025)
q_high = df['value'].quantile(0.975)
df_clean = df[(df['value'] >= q_low) & (df['value'] <= q_high)]


# In[ ]:


import matplotlib.pyplot as plt

def draw_line_plot():
    df_copy = df_clean.copy()
    
    plt.figure(figsize=(14, 7))
    plt.plot(df_copy.index, df_copy['value'], color='blue', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.grid(True)
    
    # Save the figure
    plt.savefig('line_plot.png')
    plt.show()

draw_line_plot()


# In[ ]:


def draw_bar_plot():
    df_copy = df_clean.copy()
    
    # Extract year and month from the index
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month_name()
    
    # Group by year and month to get average daily page views
    df_bar = df_copy.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Plot the bar chart
    df_bar.plot(kind='bar', figsize=(14, 7), colormap='viridis', legend=True)
    plt.title('Average Daily Page Views for Each Month Grouped by Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    
    # Save the figure
    plt.savefig('bar_plot.png')
    plt.show()

draw_bar_plot()


# In[ ]:


import seaborn as sns

def draw_box_plot():
    df_copy = df_clean.copy()
    
    # Extract year and month for box plots
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month_name()
    
    # Create a matplotlib figure
    plt.figure(figsize=(14, 7))
    
    # Year-wise box plot
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_copy)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    # Month-wise box plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_copy, order=[
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
    ])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    
    plt.tight_layout()
    
    # Save the figure
    plt.savefig('box_plot.png')
    plt.show()

draw_box_plot()


# In[ ]:




