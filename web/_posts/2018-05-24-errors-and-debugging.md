---
layout: post
current: post
#cover:  assets/images/welcome.jpg
navigation: True
title: Errors and Debugging 
date: 2018-05-24
tags: [Basics]
class: post-template
subclass: 'post tag-basics'
author: andrew
---

While teaching Python for data analysis in the first- and second-year computational labs in Bath, one of the most common questions I receive from students can be answered with this simple response:

> "Please scroll to the bottom of that block of text and read the last bit"

Those that have worked with Python before will *hopefully* know that I am talking about error tracebacks. 

**Error traceback** is the name for the print out appears when some error is found in the Python code, it is called a traceback because it aims to help you *trace back* to where the bug is. An example of a simple error traceback can be seen by running the following in a Python interpreter:

```python 
import numy as np
```

Here we are trying to import the numpy module, but have spelt numpy wrong. This code will return something which looks like this:

```python 
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-3-73b7917897b3> in <module>()
----> 1 import numy as np

ModuleNotFoundError: No module named 'numy'
```

Now, at first glance this can appear quite scary. However, just remember that the most important line in an error traceback is the **last one**, for this particular example we have:

```python  
ModuleNotFoundError: No module named 'numy'
```

This line alone should tell you what the problem in your code is...**should**. Although, remember though that these error traceback messages are written by other humans who originally wrote the code you are using, so the error message may not be perfectly clear. That said, in the above example just by reading the final line of the error traceback we will be able to quickly see that we've spelt numpy wrong.

Of course, not all problems can be solved by just reading the last line. The code below shows two possible attempts at using the `np.append()` function (which should add a number to the end of an array). Here we are trying to add the next two numbers in the Fibonacci sequence to the existing array: 

```python 
import numpy as np

a = np.array([0, 1, 1, 2, 3, 5, 8])
a = np.append(a, [11, 19])
a = np.append(a, 11, 19)
``` 

Running this code gives the following error:

```python 
---------------------------------------------------------------------------
AxisError                                 Traceback (most recent call last)
<ipython-input-31-198b73a8c7ca> in <module>()
      2 
      3 a = np.array([0, 1, 1, 2, 3, 5, 8])
      4 a = np.append(a, [11, 19])
----> 5 a = np.append(a, 11, 19)

~/anaconda3/lib/python3.6/site-packages/numpy/lib/function_base.py in append(arr, values, axis)
   5164         values = ravel(values)
   5165         axis = arr.ndim-1
-> 5166     return concatenate((arr, values), axis=axis)

AxisError: axis 19 is out of bounds for array of dimension 1
```

Here it is not immediately why the error has arisen. The last line of the traceback seems to be incidating sum issue related to an `axis`, which in our ignorance about the `np.append()` function, we know nothing about. However, there is another tip to help us solve this problem, which involves the **arrow indicator**:

```python 
---->
```

This arrow incidates which line the error occured on, and is extremely useful as codes become become larger and more convoluted. In the above example the line indicates that the error has arisen on the line `a = np.append(a, 11, 19)`, and following investigation of the [`np.append()` documentation](https://docs.scipy.org/doc/numpy/reference/generated/numpy.append.html), we can discover that the incorrect syntax has been used. The second argument needs to be an array (or list) if both numbers are to be added. The number `19` was understood to the be *axis* argument, for which 19 was not an allowed value. The line above features the correct syntax, hence there was no error found. 

This of course is only the tip of the iceberg of error tracebacks and the amount of information available in them. But, hopefully this means people can spend less time waiting for me to help and more time debugging code yourself. 
