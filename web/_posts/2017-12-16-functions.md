---
layout: post
current: post
#cover:  assets/images/welcome.jpg
navigation: True
title: Functions 
date: 2017-12-16
tags: [Basics]
class: post-template
subclass: 'post tag-basics'
author: andrew
---

Functions are a fundamental aspect of many programming languages. They allow a programmer to both simplify their code by hiding away many lines of code into a single line, while reducing the amount of work a programmer needs to do, if they need to do the same thing many times. 

The concept of a function will hopefully be familar from mathematics, e.g.

$$ f(x) $$

where, $$ f(x) $$ is some mathematical operation that acts on the argument $$ x $$, while the details of the function are abstracted away. An example of a function is, 

$$ f(x) = x^2 $$

Using this we can say that $$ f(2) = 4 $$, $$ f(3)=9 $$, etc. 

A function in programming is very similar, it consists of arguments and returns a value after some operation has taken place. 

The Pythonic way to *define* a function is:

```python
def name_of_function(argument):
    operation
    return result
```

The ```def``` tells the computer that you are wanting to **define** a function, the ```return``` tells the computer that this is the thing that should be sent back to the where the function is called. 

The use of **functions** is an important paradigm in programming -- the following Jupyter notebook gives some examples of functions and how they can be used. 

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/bjmorgan/python_in_chemistry/master?filepath=General%2FFunctions.ipynb)
