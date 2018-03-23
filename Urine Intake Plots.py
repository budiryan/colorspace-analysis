
# coding: utf-8

# In[99]:
import pandas as pd
import matplotlib.pyplot as plt


# In[89]:


urine = pd.read_excel("data plot Final analysis.xlsx", skiprows=1)


# In[90]:


idx = 84


# In[91]:


jeffry_urine_time = urine['Time'].iloc[:idx + 1].dropna()
jeffry_urine_day = urine['Day'].iloc[:idx + 1].dropna()
jeffry_urine_avg = urine['Average'].iloc[:idx + 1].dropna()


# In[92]:


jeffry = pd.DataFrame({'day': jeffry_urine_day, 'time': jeffry_urine_time, 'average': jeffry_urine_avg})


# In[108]:


jeffry['time'] = pd.to_datetime(jeffry['time'])


# In[112]:

plt.figure(figsize=(30,6), dpi=80)
plt.plot(jeffry['time'], jeffry['average'])
plt.show()
