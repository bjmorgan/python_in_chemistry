---
layout: post
current: post
#cover:  assets/images/welcome.jpg
navigation: True
title: Import Anything 
date: 2018-05-30
tags: [Basics]
class: post-template
subclass: 'post tag-basics'
author: andrew
---

One of the most common reasons for using Python over other languages, like [C](https://en.wikipedia.org/wiki/C_(programming_language)) or [Fortran](https://en.wikipedia.org/wiki/Fortran) is the **huge** number of packages (or libraries or modules) that are available (see my favourite [xkcd](https://xkcd.com) comic to send people as the start to use Python below). It is quite likely that you have made use of Python packages before and perhaps not even realised. This post will show how to install a package, and the different ways to make use of them. 

<a href="https://xkcd.com/353/"><img src="https://imgs.xkcd.com/comics/python.png" width="60%"></a>
Credit: [xkcd](https://xkcd.com)

A Python package is yet another way for programmers to be **lazy**. For example, instead of writing a specific function to calculate the square-root of a series of numbers in an array, it is a lot **easier** (and faster) to use someone else's work, in this case the `sqrt` function from the `numpy` package. Futhermore, the number of packages that exist for Python is huge, with 140403 (at the time of writing) packages available for download from [pypi](https://pypi.org) (a popular Python package manager). 

#### How to get packages

If you have followed the guide to [run Jupyter locally](/running-jupyter-locally), this means that you will have installed the Anaconda software. This comes with a large number of packages, such as `numpy`, `scipy`, and `matplotlib`. However, it does not include **all** packages that you might want to use. For example, in the [Making Pretty Plots](/making-pretty-plots) post we make use of the `seaborn` package, which does not come with Anaconda and must be installed.

This means that it is necessary to **install** the package. There are many ways to install packages, however many are available on the pypi package manager which makes installation *very easy*. However, as with many things, the method for interacting with the package manager changes slightly depending on the operating system:

- **On Windows**: It is necessary to launch the `Anaconda Prompt`, the quickest way to find this is to search in the Start Menu for "Anaconda Prompt". Launching this should open a window similar to that in the image below. 
- **On macOS or Linux**: It is possibly to interact with the package manager via the terminal. This can be launched by searching for "Terminal" in the Spotlight search bar (macOS) or the appropriate search functionality on linux. 

The command to install any package that is available on the pypi package manager is:

```python
pip install package-you-want-to-install
```

So for installing `seaborn` on Windows or macOS/Linux can be seen below. 

<img src="/assets/images/import001.png" width="80%">
Credit: Thanks Megan Stalker for the Windows image.

Runnning such a command will install the contents of the appropriate package in your Python interperator, allowing you to use it in your code. More information about the pypi package manager can be found [here](https://pypi.org/).

#### Using packages

In order to make use of a **particular function** within a package we must ask the Python interperator to `import` it. There are two possible ways to do this:

1. We can `import` the entire package and then make use of any function within,
2. We can `import` specific functions from within a function.

```python 
# importing the entire numpy package and giving it the alias np
import numpy as np 
# using the numpy square-root function on an array 
a = range(1, 10)
b = np.sqrt(a)

# importing only the square-root function from the numpy package
from numpy import sqrt
# using the numpy square-root function on an array 
a = range(1, 10)
b = sqrt(a)
```

Notice that in the first example in order to leverage `numpy`'s square-root function, it was necessary to tell the Python interperator that you wanted it to use the `numpy` package with `np.`. 

It should be noted here that, personally, I consider **best practice** to be the first example, as the latter could create some confusion in the following example: 

```python 
from numpy import sqrt
from math import sqrt
a = range(1, 10)
b = sqrt(a)
```

This code will give the following error:

```python 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-51-010dd619ec5a> in <module>()
      2 from math import sqrt
      3 a = range(1, 10)
----> 4 b = sqrt(a)

TypeError: must be real number, not range
```

This is because the square-root function from the `math` package cannot be used on a series (array or list) of numbers, and by importing it **after** the `numpy` version, overwrites the `numpy` verison.

Hopefully, this has been a useful, and straightforward, introduction to the purpose and application of packages to **extend** the capabilities of the Python programming language. 

#### Appendix

Just as a note, you may see the following syntax in import statements. 

```python 
from numpy import *
```

This says import all of the functions from the package `numpy`. This means that all of the functions within the `numpy` package can be accessed without needing to use the `np.` or `numpy.` syntax. Again, this may lead to unexpected results as seen in the previous example. 
