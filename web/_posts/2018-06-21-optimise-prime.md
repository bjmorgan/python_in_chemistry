---
layout: post
current: post
#cover:  assets/images/welcome.jpg
navigation: True
title: Optimise Prime
date: 2018-06-21
tags: [Applications]
class: post-template
subclass: 'post tag-basics'
author: andrew
published: false
---

One of my most commonly used [libraries](/import-anything) in Python is [Scipy](https://scipy.org/scipylib/index.html), in particular my favourite function in this library has to be ```scipy.optimise.curve_fit```. This function from the Scipy library is designed to perform a non-linear least squares minimisation for a given function to some data. This might sound **greek** for now, however hopefully after reading this post you will be able to apply ```curve_fit``` in your own work.

The idea of a least-squares minimisation for a given function is a common problem in data analysis, when you have some *functional form* that you think describes the relationships present in your experimental data. The ```curve_fit``` function lets you determine ideal values for the variables in this functional form for your given dataset. As with many problems this is best described with an example.

Consider the ideal gas law,

$$ pV = nRT, $$

where, $$p$$ is the pressure of the system, $$V$$ the volume, $$n$$ the number of moles of substance, $$R$$ the ideal gas constant, and $$T$$ the temperature. Now say we performed an experiment, where we measured the pressure exterted by a given amount (1 mole) gas at constant volume (1 m<sup>3</sup>) at various temperatures, where the uncertainity in the pressure measurement is 2 %.

*Table 1. Example data*
| Temperature (K) | Pressure (Pa) |
| --------------- | ------------- |
| 290             | 35.2          |
| 300             | 36.0          |                    
| 310             | 37.3          |
| 320             | 38.6          |
| 330             | 39.4          |
| 340             | 40.9          |
| 350             | 42.0          |

First, lets [plot](/making-pretty-graphs) this data.

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set('talk', palette='colorblind')

t = np.array([290, 300, 310, 320, 330, 340, 350])
p = np.array([35.2, 36.0, 37.3, 38.6, 39.4, 40.9, 42.0])
p_err = p * 0.02

plt.errorbar(t, p, yerr=p_err, marker='o', linestyle='')
plt.xlabel('T (K)')
plt.ylabel('p (Pa)')
plt.tight_layout()
plt.show()
```

![](/assets/images/op001.png)
*Figure 1. A simple plot of temperature against pressure.*

This data looks pretty linear, from this plot -- a good place to start. Now the next thing is to right a function that models the **ideal gas law**, when we know the volume and amount of substance.

```python
def ideal_gas_law(t, R):
    return R * t
```

  
