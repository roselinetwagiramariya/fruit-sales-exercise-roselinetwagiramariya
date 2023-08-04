# Fruit Sales

Code Louisville Python programming exercise.

## Overview

In this exercise we will create a Pandas Dataframe with fruit sales information
and write the data to a CSV file. This exercise is based on the Lesson 1 
exercise in the Kaggle Learn Pandas course. 

Write a Python program that creates a Pandas Dataframe that matches the table 
below:

| | Apples | Bananas |
| ----- | ----- | ----- |
| 2017 Sales | 35 | 21 |
| 2018 Sales | 41 | 34 |

Write the data to a file called `fruit.csv` in the project directory.

Make sure to add the `fruit.csv` file to the repo before committing and pushing
back to GitHub.

## Instructions

1. Click on the link in the assignment in Google Classroom.
1. Accept the exercise from GitHub. GitHub will automatically create a new repo 
for you with an open Pull Request for your changes.
1. Clone the new repo to your machine.
1. Create a virtual environment, activate it, and install the required packages. (see instructions below)
1. Add your code to the specified file.
1. Add/Commit/Push your code back to GitHub.GitHub will run the automated tests 
when you push.
1. Review the Pull Request on your repo to see the status of the tests.
1. “Turn in” the assignment in Google Classroom.


### Virtual Environment Step-by-Step Instructions

1. After you have cloned the repo to your machine, 
navigate to the project folder in GitBash/Terminal.
1. Create a virtual environment in the project folder. `python3 -m venv venv` [^1]
1. Activate the virtual environment. `source venv/bin/activate`
1. Install the required packages. `pip install -r requirements.txt`
1. When you are done working on your repo, deactivate the virtual environment. `deactivate`

[^1]: GitBash on Windows uses “python” instead of “python3”


## Optional: Automated Code Testing

This repo contains a small testing program that is automatically run by GitHub 
to validate your code. This testing program is contained in the tests.py file. 
You don't have to do anything with this file to complete the exercise, but 
you can follow these steps if you would like to run the tests on your machine.

1. Open GitBash in Windows or the Terminal in Mac and navigate to the project 
folder.
1. Run the tests. We won't be covering testing with python in this course. Use 
the following command to run the tests: `pytest tests.py`. You can read more 
about it [here](https://realpython.com/python-testing/).
1. Review the output from running the test. This will let you know whether your 
code produces the expected results.
