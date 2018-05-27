---
layout: post
current: post
#cover:  assets/images/welcome.jpg
navigation: True
title: Making Pretty Plots
date: 2018-05-26
tags: [Basics]
class: post-template
subclass: 'post tag-basics'
author: andrew
---

One of the most common reasons for using Python for data analysis is the easy access to good-looking plots, via `matplotlib`. I have used Python for plotting data for many years now, reaching the point that I now **hate** to see bad-looing plots produced by [Microsoft Excel](https://datanitro.com/blog/better_excel_charts). 

In this post we will look at some packages in Python to help create pretty plots for your posters, papers, and presentations. 

For some examplary data, we will plot some data associated with the Arrhenius equation, 

$$ k = A\exp{\bigg(\frac{-E_a}{k_BT}\bigg)}. $$

Hopefully you are familiar with the reformulation of this equation such that the data can be plotted as a straight line with gradient $$ -E_a / k_B $$ and intercept $$ \ln{(A)} $$, 

$$ \ln{(k)} = \frac{-E_a}{k_B}\frac{1}{T} + \ln{(A)}. $$

The raw data can be found [here](ihttps://raw.githubusercontent.com/bjmorgan/python_in_chemistry/master/General/exp1.csv) for playing along the notebook at home. If you open the file in some text editor you can see that it consists of a *comment* line that starts with a # symbol, followed by data which is separated into three columns by commas (hence the file's extension of `.csv` [comma separated values]), the file should look something like this:

```
#this is some example Arrenhius data produced by ARM 
Temperature,k,dk
100.0,2.078e-04,2.078e-06
150.0,2.176e-04,2.176e-06
200.0,2.229e-04,2.229e-06
250.0,2.260e-04,2.260e-06
300.0,2.281e-04,2.281e-06
350.0,2.316e-04,2.316e-06
400.0,2.331e-04,2.331e-06
``` 

There are many ways to read data in from a file in Python, however we will use the `loadtxt` function from the `numpy` package to read in and store the data. We can do this using the following command:

```python 
import numpy as np
t, k, dk = np.loadtxt('exp1.csv', skiprows=2, delimiter=',', unpack=True)
```

The first line here will import the package `numpy` and give the alias `np` (this is just to save our lazy fingers from writing `numpy` everytime we want to use a function from this package). The next line will do the following:

- read in the file called `exp1.csv`, 
- skipping the first 2 rows (these are the comment line and the headings), since the columns are separated by commas it is necessary to make the function aware of this (the jargon for the separator is the **delimter**), 
- the normal way for this function to read in data is a a series of rows for which the data are related (rather than the columns we have) so we must tell the function to *unpack* this data (essentially the matrix storing the data is transposed). 
- All of this will store each of the three columns into the variables `t`, `k`, and `dk`. We can then have a look at one of these by printing the array: 

```python 
print(k)
```

Which will return: 

```
[ 0.0002078  0.0002176  0.0002229  0.000226   0.0002281  0.0002316
  0.0002331]
```

This data is stored as a [`numpy.ndarray`](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.ndarray.html), which is an information dense and efficient way to store homogeneous data. The most important aspect of us is that it is very-compatible with `numpy` functions. 

Now that the data has been read in, we can start to plot it. In Python plotting data quickly can be very simple. To plot the reciprocal temperature against the natural logarithm of the rate constant, we can do the following:

```python 
import matplotlib.pyplot as plt
plt.plot(1/t, np.log(k))
plt.tight_layout()
plt.show()
```

The `tight_layout()` function simply ensures that the when the file is presented all the formatting of the image is correct. This will print the following image:

![Better than excel](/assets/images/mpp001.png) 

Alright, so this looks okay-ish, but isn't really representing our data well (a line between our descrete points), we have failed to label our axes, and there are no error bars, lets try expanding what we have: 
 
```python 
import matplotlib.pyplot as plt
plt.errorbar(1/t, np.log(k), yerr=dk, marker='o', linestyle='')
plt.xlabel('1/T (K$^{-1}$)')
plt.ylabel('ln(k)')
plt.tight_layout()
plt.show()
```

We can already see an improvement in this image:

![This is passable](/assets/images/mpp002.png)

`matplotlib` is a hugely flexible package, that offers the user a massive amount of control about how the plot is presented. Many of the aesthetic control over the plot can be accessed by affecting the `rcParams` (this is a dictionary object used by `matplotlib`). For example,  if you wanted a grid on your plot, a green background, massive x-axis labels and the y-axis ticks pointing into the graph, the following could be used:

```python 
import matplotlib as mpl
mpl.rcParams['axes.grid'] = True
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['axes.facecolor'] = 'g'
import matplotlib.pyplot as plt
plt.errorbar(1/t, np.log(k), yerr=dk, marker='^', linestyle='', color='#34a5daff')
plt.xlabel('1/T (K$^{-1}$)')
plt.ylabel('ln(k)')
plt.tight_layout()
plt.show()
```

This will give a monstrosity which looks like this:
 
![My eyes! My beautiful eyes!](/assets/images/mpp003.png)

You will also notice that the marker in this has been changed to a triangle by using `'^'` instead of `'o'` and the color of the data points is now defined by a hex RGB code. The whole range of `rcParams` that can be varied can be found by using the following command:

```python 
mpl.rcParams.keys()
```

These can be varied to your heart's content until you find a particular plot design that you love. However, programmers are lazy and if you can't be bothered spending hours adjusting your plot in every way you can use the `seaborn` package. This package is in many ways a layer on top of matplotlib that allows some really [fancy plots](https://seaborn.pydata.org/examples/index.html) to be created. However, I am a big fan of it for two simple reasons:

1. Nicer standard colors; with native colourblind support,
2. Quick assignment of a plot context to control font sizes.

Both of these aspects are assigned in the `set()` function. So to plot the data above making use of the `seaborn` package we run the following:

```python 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set('talk', palette='colorblind')
plt.errorbar(1/t, np.log(k), yerr=dk/k, marker='o', linestyle='')
plt.xlabel('1/T (K$^{-1}$)')
plt.ylabel('ln(k)')
plt.tight_layout()
plt.show()
```

Which produces the following:

![*Hearts-for-eyes-emoji*](/assets/images/mpp004.png)

As you can see the plot context here is set to `'talk'`, `seaborn` has four possible contexts:

- `'paper'`
- `'notebook'`
- `'talk'`
- `'poster'`

Which will gradually increase the size of the elements in the plot to make them more easily read. The other keyword in the `set()` function is `palette`, `seaborn` allows a wide variety of palettes however, as a colourblind person my favourite is the `'colorblind'` (note the American spelling) option. The colours in this palette are specifically chosen to give good differentiation for those suffering from colourblindness. An example of the colours can be seen here, where the plots are offest by 0.1 in the y-axis: 

```python 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set('talk', palette='colorblind')
plt.errorbar(1/t, np.log(k), yerr=dk/k, marker='o', linestyle='')
plt.errorbar(1/t, np.log(k)+0.1, yerr=dk/k, marker='o', linestyle='')
plt.errorbar(1/t, np.log(k)+0.2, yerr=dk/k, marker='o', linestyle='')
plt.errorbar(1/t, np.log(k)+0.3, yerr=dk/k, marker='o', linestyle='')
plt.xlabel('1/T (K$^{-1}$)')
plt.ylabel('ln(k)')
plt.tight_layout()
plt.show()
```

![Quality contrast](/assets/images/mpp005.png)

As with many aspects of Python plotting is massively extensible and customisible. This was just a quick introduction to some aspects of plotting in Python and we will surely have more in the future. Below is a link to the Binder resource to allow you to play along at home. 

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/bjmorgan/python_in_chemistry/master?filepath=General/Making%20Pretty%20Plots.ipynb) 
