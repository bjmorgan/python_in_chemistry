---
layout: post
current: post
#cover:  assets/images/welcome.jpg
navigation: True
title: Working with Physical Constants and Units
date: 2017-12-16
tags: [Basics]
class: post-template
subclass: 'post tag-basics'
author: ben 
---

A lot of the expressions that describe chemical phenomena involve physical constants, such as the speed of light, $$c$$, Avogardo's constant, $$N_A$$, Planck's constant, $$h$$, and the Boltzmann constant, $$k_B$$. When working with algebraic expressions, it is also important to keep track of the relevant units. Different experiments may conventionally report data in non-S.I. units and these units must be converted for comparing data or calculating chemical properties. 

While manipulating units manually (for example, when working through a problem by hand) is an important skill, if you are solving numerical problems using code you ideally want to avoid typing in unit conversions and values for constants. Any numbers that are typed in, are possible places where you could mistype. Mistakes in your code can hopefully be spotted when they produce errors, or from testing that your code produces a known result. Mistakes in numbers typed in are harder to spot, and can propogate through to your results.

To reduce the change of introducing errors, there are two easy techniques you can follow:

- Define your constants and unit conversions once by assigned them to variables (conventionally at the top of your code), rather than retyping them each time. 
- If possible, read constants and unit conversions automatically from databases. 

These techniques are illustrated in the notebook below, which shows how to use the <code>scipy.constants</code> database to work more conveniently with physical constants and unit conversions. 

[Run the notebook](https://mybinder.org/v2/gh/bjmorgan/python_in_chemistry/master?filepath=General/Working%20with%20units%20and%20physical%20constants.ipynb)
