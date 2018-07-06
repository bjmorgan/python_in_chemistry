---
layout: page
current: pylj 
title: 
navigation: true
logo: 'assets/images/python_in_chemistry.png'
class: page-template
subclass: 'post page'
---

<img src="https://github.com/arm61/pylj/blob/master/logo/logo.png?raw=true" style="width: 80%;"/>

### what is pylj?

pylj is an open-source library to facilitate student interaction with classical simulation. It is designed to operate within the Jupyter notebook framework, making it easy to implement in the classroom, or computer lab. Additionally, due to the open-source, and documented, nature of the code it is easy for educators to add unique, custom extensions.

### what does pylj offer?

Currently pylj can perform the simulation of a 2D argon system by molecular dynamics, with both NVE and NVT ensembles available and making use of a Velocity-Verlet integrator, as well as Metropolis Monte-Carlo simulations. A series of sampling classes exist (found in the sample module), such as the Interactions (MD), Scattering (MD), and Energy classes. However, it is straightforward to build a custom sampling class either from scratch or using the sampling class building tools.

### examples

Examples of the [Monte-Carlo](http://35.230.133.1/notebook/notebooks/examples/monte_carlo.ipynb) and [molecular dynamics](http://35.230.133.1/notebook/notebooks/examples/molecular_dynamics.ipynb) interfaces can be found at the following links (the password is the name of the software). *Currently the cloud resource being accessed for this is small so wait times my be long*.  

Some examples of possible teaching laboratory exercises that use pylj can be found [here](https://github.com/arm61/pylj/tree/master/examples). 

### how to get pylj?

If you are interested in using pylj, in any sense, fork the code at [github.com/arm61/pylj](http://www.github.com/arm61/pylj) or email Andrew (arm61 ‘at’ bath.ac.uk). 

### is there documentation?

Full API level documentation is available at [pylj.rtfd.io](http://pylj.rtfd.io). We are currently working on a more high level user documentation but looking at the example notebooks above is a great place to start. 

### requirements

To run pylj locally we recommend installing the [Anaconda](http://pythoninchemistry.org/running-jupyter-locally), which gives access to Jupyter notebook framework and the necessary packages. It is also it is necessary to have a C++ compiler, most macOS or Linux machines should already have this, on Windows it is best to install the [Visual C++ package](https://www.microsoft.com/en-gb/download/details.aspx?id=48145). 

### contributing and feature requests

Information about contributing can be found [here](https://github.com/arm61/pylj/blob/master/CONTRIBUTING.md). 

### how to cite pylj 

Thank you for using pylj. If you use this code in a teaching laboratory or a publication we would greatly appreciate if you would cite the DOI in the Zenodo link below.

[![DOI](https://zenodo.org/badge/119863480.svg)](https://zenodo.org/badge/latestdoi/119863480)
