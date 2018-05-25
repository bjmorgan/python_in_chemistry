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

To deliver this lecture, I decided to develop a small python utility that performs simple 2D argon simulations and provides visualisation that is both supported by Jupyter and easily extensible. The attached notebook is the result of this course. 

It should be noted that due to the computationally intensive nature of MD, I recommend downloading the notebook, installing pylj via pip and running the notebook on your machine. On Window type the following into the Anaconda Prompt, on macOS or Linux type it into the terminal. 

```
pip install pylj
```

Finally, make sure to also download the additional_code.py file as this makes the plotting easier (make sure that the additional_code.py file is in the same folder as the lecture when you launch the Jupyter notebook).

[Download Lecture](https://raw.githubusercontent.com/bjmorgan/python_in_chemistry/master/Neutron_Training_Course/lecture.ipynb)

[Download additional_code](https://raw.githubusercontent.com/bjmorgan/python_in_chemistry/master/Neutron_Training_Course/additional_code.py)

(Right click and download the files)

There is currently a server running on which the lecture can be worked through. However, a password is needed, please email Andrew to gain access (arm61 'at' bath.ac.uk). Check that out [here](http://35.230.133.1/notebook/notebooks/NTC/lecture.ipynb).
