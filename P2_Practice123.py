#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
arr_random = np.random.randint(low=1, high=100, size=(3,5))
df=pd.DataFrame(arr_random, columns=["A","B","C","D","E"], index=["1","2","3"])
print(df)

f1, f2 = plt.subplots(2,1,figsize=(15,8))
f2[0].plot(df.index.values, df['A'], c='green',label="line1")
f2[0].plot(df.index.values, df['B'], c='orange',label="line2")
f2[0].plot(df.index.values, df['C'], c='red',label="line3")
f2[0].plot(df.index.values, df['D'], c='blue',label="line4")
f2[0].plot(df.index.values, df['E'], c='yellow',label="line5")
f2[0].legend(loc=9, ncol=5)

f2[1].plot(df.index.values, df["A"], marker="o", lw=0)
f2[1].plot(df.index.values, df["B"], marker="o", lw=0)
f2[1].plot(df.index.values, df["C"], marker="o", lw=0)
f2[1].plot(df.index.values, df["D"], marker="o", lw=0)
f2[1].plot(df.index.values, df["E"], marker="o", lw=0)


# In[54]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
arr_random = np.random.randint(low=1, high=100, size=(30,5))
df=pd.DataFrame(arr_random, columns=["A","B","C","D","E"], index=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"])

fig, ax = plt.subplots(3, 1, figsize=(15,18))

ax[0].bar(df.index.values, df['A'], color="green")
for i in range(df.shape[0]):
    ax[0].text(i, df['A'][i]+1, df['A'][i], horizontalalignment='center')
ax[0].legend('A')

ax[1].bar(df.index.values, df['B'], color="red")
for i in range(df.shape[0]):
    ax[1].text(i, df['B'][i]+1, df['B'][i], horizontalalignment='center')
ax[1].legend('B')

ax[2].bar(df.index.values,df['B'], color="green", label="A")
ax[2].bar(df.index.values, df['A'], bottom=df['B'], color="red", label="B")
for i in range(df.shape[0]):
    ax[2].text(i, df['B'][i]+df['A'][i], df['B'][i]+df['A'][i], horizontalalignment='center')
ax[2].legend(loc=0)


# In[ ]:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
arr_random = np.random.randint(low=1, high=100, size=(30,5))




# In[ ]:




