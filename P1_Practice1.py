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