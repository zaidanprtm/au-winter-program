# -*- coding: utf-8 -*-
"""practice2.ipynb

Automatically generated by Colaboratory.

"""

import numpy as np
# practice about numpy
arr = np.array([np.zeros(6), np.ones(6)])
print(arr)

arr2 = np.zeros((6,7))
print(arr2)
print(arr2.shape)

arrA = np.array([[1, 2], [3, 4]])
arrB = np.array([[5, 6], [7, 8]])
arrRes = np.dot(arrA, arrB)
print(arrRes)
print(np.min(arrRes))
print(np.max(arrRes))
print(np.mean(arrRes))

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
# %matplotlib inline
fig = plt.figure()
# draw pie chart
labels = 'day 1', 'day 2', 'day 3', 'day 4', 'day 5', 'day 6'
sizes = [9.4, 15.2, 21.5, 10.8, 16.9, 26.2]
explode = (0, 0, 1, 0, 1, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=0)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
# %matplotlib inline

x = np.linspace(-10,20,500)
y = x**3 + 5*(x**2) - 9 

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# practice pandas
import pandas as pd

s = pd.Series(data=range(3,11), index=list('ABCDEFGH'))
d = s.rename({'C':'CC', 'D' : 'DD'}, inplace = True)
print(s)
print(s.max())
print(s.min())
print(s.mean())

ser = pd.Series(['a', 'b', 'c', 'c', 'b', 'e', 'f', 'f', 'a', 'b'])
# %matplotlib inline
ser.value_counts(normalize=True).sort_index().plot(kind='bar')

import pandas as pd
data = {
  "math": [90,50,70,40],
  "english": [60,70,90,50],
  "history" : [33, 75, 88, 60],
  "chinese" : [55.0, 55.0, 55.0, 88.0]
}

df = pd.DataFrame(data, index = ["Simon", "Allen", "Jimmy", "Peter"])
print(df)
df2 = df[(df['history']<60) & (df['english']<60)]
print(df2)
df3 = df[(df['history']<60) | (df['english']<60) | (df['math']<60)]
print(df3)

import pandas as pd
df = pd.read_csv('http://bit.ly/kaggletrain')
# print(df.head(10))
df2 = pd.DataFrame(
    {
        "Survived" : [0,1],
        "Pclass" : [3.0,1.0],
        "Name" : ["Jack", "Rose"],
        "Sex" : ["male", "female"],
        "Age" : [23,20]
    },
    index = [891,892],
)
# mergedf = [df, df2]
result = df.append(df2)
print(result)
# print(df)