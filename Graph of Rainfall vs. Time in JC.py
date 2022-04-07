import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'figure.figsize':(9,5), 'figure.dpi':90})
x = np.arange(0, 30, 1)
y = (x * (x * 1.0036)) + 53.7



plt.plot(x, y)
plt.title("Rainfall vs. Time (years from 2020) in Johns Creek, Georgia \n (accounting for increase due to climate change)")
plt.xlabel("Time (years from 2020)")
plt.ylabel("Amount of rainfall (inches)")
plt.show()

