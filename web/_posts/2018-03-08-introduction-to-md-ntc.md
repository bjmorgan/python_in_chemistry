---
layout: post
current: post
#cover:  assets/images/welcome.jpg
navigation: True
title: Introduction to Molecular Dynamics for Neutron Scatters 
date: 2018-03-08
tags: [Applications]
class: post-template
subclass: 'post tag-applications'
author: andrew
---

This year I was invited to take part in the ISIS Neutron Training Course, a introductory course for neutron scattering scientists. The aim of our session was to introduce molecular dynamics and show how this could be applied to neutron scattering experiments. This involved a workshop showing how [falass](http://people.bath.ac.uk/arm61/falass/) could be used to analyse neutron reflectometry and an introdcutory lecture outlining molecular dynamics. 

To deliver this lecture, I decided to develop a small python utility (still very alpha in development) that performs simple 2D argon simulations and provides visualisation that is both supported by Jupyter and easily extensible. The attached notebook is the result of this course. 

It should be noted that the pylj (the MD package) is not perfect and possibly will cause the notebook to crash occasionally. Further due to the computationally intensive nature of MD, I recommend downloading the notebook, installing pylj via pip and running the notebook on your machine. If you really want to run it over Binder the link is included. Finally, make sure to also download the additional_code.py file as this makes the plotting easier.

[Download](https://github.com/bjmorgan/python_in_chemistry/blob/master/Neutron_training_Course) 

[Run the notebook](https://mybinder.org/v2/gh/bjmorgan/python_in_chemistry/master?filepath=Neutron_Training_Course%2Flecture.ipynb)
