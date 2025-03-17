# John Wangwang, Libaries notes

# What is a library? 
# A library is a collection of functions and methods that can be imported and used

# What are some standard python libraries?
# Matplotlib
# TensorFlow
# Pandas
# Numpy
# SciPy
# Scrapy
# Scikit-learn
# PyGame 
# PyTorch
# PyBrain

# Why do we import other libraries?
# So we don't have to write the function ourselves. 
 
# What information do you find in the documentation for a library?
# Installation guide and how each function work

# What are good sources for tutorials on a library you have never used before?
# Community or Documentation: quickstart

# What is a README file?
# Af file in your directories containing information about the projects

# What things belong on a README file?
# Project Description (Require)
# Installation Guide (Require)
# Execution and usage (Require)
# Used Techonology (Require)
# Current features (Require)
# Contributing
# Contributors (Require)
# Author's info (Require)
# Change log
# License

# Why do we include README files with our projects?
# To provide other developer and potentially user with information on the project 


import matplotlib.pyplot as plt
import numpy as np
from faker import Faker

fake = Faker()

fake.name()
# 'Lucy Cechtelar'

fake.address()
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

fake.text()
# 'Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi
#  beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt
#  amet quidem. Iusto deleniti cum autem ad quia aperiam.
#  A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur qui
#  quaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernatur
#  voluptatem sit aliquam. Dolores voluptatum est.
#  Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.
#  Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.
#  Et sint et. Ut ducimus quod nemo ab voluptatum.'

fake = Faker('en_UK')
for _ in range(10):
  print(fake.name())

# 'Adaline Reichel'
# 'Dr. Santa Prosacco DVM'
# 'Noemy Vandervort V'
# 'Lexi O'Conner'
# 'Gracie Weber'
# 'Roscoe Johns'
# 'Emmett Lebsack'
# 'Keegan Thiel'
# 'Wellington Koelpin II'
# 'Ms. Karley Kiehn V'

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.fig, ax = plt.subplots()

