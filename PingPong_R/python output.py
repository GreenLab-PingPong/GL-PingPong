
# coding: utf-8

# ## Importing libraries

# In[2]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

os.getcwd()


# In[2]:


# os.chdir("/home/Shubham/Documents/green/")

# df_you = pd.read_csv("you1.csv", header = 0, skiprows = 3, sep=",", skipfooter = 9, usecols = [0,1,2,3])
# df_spot = pd.read_csv("spot1.csv", header = 0, skiprows = 3, sep=",", skipfooter = 9, usecols = [0,1,2,3])

# df_spot.shape,df_you.shape


# ## finding sum of power values for each session (each indivdual csv file)

# For low quality youtube 

# In[13]:


round(33.3333333,2)


# In[14]:


os.chdir("/home/shubham/Documents/green/youtube_low")
allFiles = glob.glob(os.getcwd() + "/*.csv")

#skip first 3 rows and last 9 rows of csv, as not part of data.
df = []
for filename in allFiles:
#         df_you = df_you.append(pd.read_csv(filename, header = None,skiprows = 5, sep=',', skipfooter = 10, usecols = [0,1,2,3]))
        df.append(pd.read_csv(filename, header = 0,skiprows = 3, sep=',', skipfooter = 9, usecols = [0,1,2,3]))

    
[round(df[i]['Battery Power [uW]'].sum()/1000000,2) for i in range(50)]


# for **high-quality youtube**

# In[4]:


os.chdir("/home/shubham/Documents/green/youtube_high")
allFiles = glob.glob(os.getcwd() + "/*.csv")

#skip first 3 rows and last 9 rows of csv, as not part of data.
df = []
for filename in allFiles:
#         df_you = df_you.append(pd.read_csv(filename, header = None,skiprows = 5, sep=',', skipfooter = 10, usecols = [0,1,2,3]))
        df.append(pd.read_csv(filename, header = 0,skiprows = 3, sep=',', skipfooter = 9, usecols = [0,1,2,3]))

    
[round(df[i]['Battery Power [uW]'].sum()/1000000,2) for i in range(50)]


# for **low-quality spotify**

# In[16]:


os.chdir("/home/shubham/Documents/green/spotify_low")
allFiles = glob.glob(os.getcwd() + "/*.csv")

#skip first 3 rows and last 9 rows of csv, as not part of data.
df = []
for filename in allFiles:
#         df_you = df_you.append(pd.read_csv(filename, header = None,skiprows = 5, sep=',', skipfooter = 10, usecols = [0,1,2,3]))
        df.append(pd.read_csv(filename, header = 0,skiprows = 3, sep=',', skipfooter = 9, usecols = [0,1,2,3]))

    
[round(df[i]['Battery Power [uW]'].sum()/1000000,2) for i in range(50)]


# In[3]:


os.chdir("/home/shubham/Documents/green/spotify_high")
allFiles = glob.glob(os.getcwd() + "/*.csv")

#skip first 3 rows and last 9 rows of csv, as not part of data.
df = []
for filename in allFiles:
#         df_you = df_you.append(pd.read_csv(filename, header = None,skiprows = 5, sep=',', skipfooter = 10, usecols = [0,1,2,3]))
        df.append(pd.read_csv(filename, header = 0,skiprows = 3, sep=',', skipfooter = 9, usecols = [0,1,2,3]))

    
[round(df[i]['Battery Power [uW]'].sum()/1000000,2) for i in range(50)]


# In[5]:


## include spotify high
python.__version__

