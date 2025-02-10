---
layout: post
title:  "Your Data Science Toolbox: Need to Know Libraries in Python"
author: Kelson Jensen
description: Short yet informative description
image: "C:/Users/User/OneDrive/Documents/Winter 2025/Stat 386/My-Blog/assets/images/data_toolbox.jpg"
---
## _Introduction_
Need a place to start your data science toolbox? Python is one of the best tools for working with data, but to really make the most of it, you need the right libraries. Three must-haves in any data scientist’s toolbox are [Pandas](https://www.learnenough.com/blog/how-to-import-Pandas-in-python), [NumPy](https://numpy.org/doc/2.2/user/absolute_beginners.html), and [Matplotlib](https://matplotlib.org/). These libraries make it easy to clean and analyze data, run fast numerical calculations, and create visualizations that actually make sense. Whether you're sorting through messy datasets, crunching numbers, or bringing data to life with charts, these tools have you covered. In this post, we’ll break down what they do, why they’re useful, and how you can start using them right away. Lets get to it!

# _Pandas: A data analyzation and manipulation library_
[Pandas](https://www.learnenough.com/blog/how-to-import-Pandas-in-python) is one of the most widely used python libraries for handling data. It helps you read, explore, clean, and transform datasets with simple, efficient functions.

### _Reading in Data_
Before working with data, we need to load it. Pandas makes this easy with functions like:
- pd.read_csv('file.csv') to read a CSV file. pd.
- read_excel('file.xlsx') to load an Excel file.
- pd.read_sql(query, connection) to import data from a SQL database.

### _Data Exploration_
To understand what’s in our dataset, we can use:
- df.head() to see the first few rows.
- df.info() to get a summary of column types and missing values.
- df.describe() to generate key statistics like mean and standard deviation.

### _Data Cleaning and Manipulation_
Data often needs cleaning before analysis:
- We can remove missing values using df.dropna() or replace them with a specific value using df.fillna(value). 
- Renaming columns with df.rename(columns={'old_name': 'new_name'}) improves readability.
- f.groupby('column') helps in summarizing data by categories.

### _Data Transformation_
Pandas also helps reshape and modify data efficiently. We can create new columns by applying calculations, such as:
- df['new_col'] = df['existing_col'] * 100. 
- For restructuring data df.pivot_table(values='col', index='row', columns='col2') is useful. 
- If we need to modify values, df['new_col'] = df['existing_col'].
- apply(lambda x: x * 2) applies a function to each row, in this case doubling the values.

Pandas makes working with data fast and intuitive. let’s look at how NumPy helps with numerical operations.


# _NumPy: Numerical Computation_
[NumPy](https://numpy.org/doc/2.2/user/absolute_beginners.html) is a must know library that helps perform fast mathematical operations on large datasets. Using arrays it optimized the speed to do such computation. 

### _Creating Arrays_
To start using NumPy, we first need to create arrays. Here's how you can do that:
- From a list: np.array([1, 2, 3, 4, 5])
- Zeros: np.zeros(5) – Creates an array of five zeros.
- Range: np.arange(1, 10, 2) – Generates an array from 1 to 9 with a step of 2.
These arrays will be the foundation of your numerical operations in NumPy.

### _Performing Math with NumPy_
NumPy makes mathematical operations simple and fast. You can perform calculations directly on arrays without needing loops.
- Multiply: arr * 2
- Sum: np.sum(arr)
- Mean: np.mean(arr)
- Standard Deviation: np.std(arr)
These functions let you quickly compute key statistics without the hassle of manual calculations.

### _Indexing and Slicing Arrays_
Accessing and manipulating array values is easy with NumPy:
- Single element: arr[0]
- Slicing: arr[1:3] – Retrieves elements from index 1 to 2.
- Conditional selection: arr[arr > 2] – Returns elements greater than 2.

### _Reshaping and Combining Arrays_
You can reshape or combine arrays with ease:
- Reshape: arr.reshape(2, 3) – Converts a 1D array into a 2x3 matrix.
- Combine: np.concatenate([arr1, arr2]) – Merges arrays into one.

With NumPy handling the number crunching, it's time to look into data visualization with Matplotlib, a library for creating charts and graphs.


# _Matplotlib: Visualizing useful data_
[Matplotlib](https://matplotlib.org/) is the go to library for any type of data visualization. The libraries allows you to make everything from basic line charts to complex scatter plots, histograms, and more. 
We will look over step by step how to create a simple plot and basic functions that help with that. 

### _Creating Your First Plot_
To get started, first import Matplotlib:
import matplotlib.pyplot as plt
Then, create a simple line plot:
```python 
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.show()
```

This generates a basic line chart, ideal for showing relationships between two variables.
<img src="C:/Users/User/OneDrive/Documents/Winter 2025/Stat 386/My-Blog/assets/images/simple_plot_1.jpeg" alt="Basic Line Chart" width="300">


### _Customizing Your Plot_
Once you’ve created a basic plot, you can easily customize it:
```python
# Add a title and labels: 
plt.title("Basic Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# Change line style and color:
plt.plot(x, y, linestyle='--', color='r')

# Add gridlines:
plt.grid(True)
plt.show()
```
<img src="C:\Users\User\OneDrive\Documents\Winter 2025\Stat 386\My-Blog\assets\images\basic_plot.png" alt="Full Basic Plot" width="300">


### _Creating Other Types of Plots_
Matplotlib supports a variety of plot types, including:
```python
# Scatter plot:
plt.scatter(x, y)
plt.show()

# Bar chart:
categories = ['A', 'B', 'C']
values = [3, 7, 5]
plt.bar(categories, values)
plt.show()

# Histogram:
data = [1, 2, 2, 3, 3, 3, 4, 5, 6]
plt.hist(data)
plt.show()
```
Below is an example of other things that you can create using Matplotlib as well as Numpy to make something look nice. 
<img src="/assets/images/Cool_example.jpeg" alt="Cool Example of Possible Plots" width="300">


# _Wrap Up_
Python’s [Pandas](https://www.learnenough.com/blog/how-to-import-Pandas-in-python), [NumPy](https://numpy.org/doc/2.2/user/absolute_beginners.html), and [Matplotlib](https://matplotlib.org/) are essential tools for any data scientist, helping you analyze, manipulate, and visualize data with ease. Mastering these libraries will set a strong foundation for more advanced data science techniques.

Put your skills you just learned to the test! Try loading a dataset, exploring it with [Pandas](https://www.learnenough.com/blog/how-to-import-Pandas-in-python), performing calculations with [NumPy](https://numpy.org/doc/2.2/user/absolute_beginners.html), and visualizing trends with Matplotlib[Matplotlib](https://matplotlib.org/) using the links on each of these topics. If you have questions or insights, share them in the comments—I’d love to hear your thoughts!