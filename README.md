# ACM Research Coding Challenge (Fall 2020)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.

## Daniel Segundo - ACM Research Coding Challenge - Question #1

At first glance the question seems to be asking to find the number of clusters, which to me says
to find the total number of points. Looking at the .csv file, there are 151 rows, 150 of which correspond
to a unique point. Therefore, my solution is to import the .csv file and count the number of rows with data.

## To solve:
1. Import the pandas library (as pd)
2. use pd.read_csv() to read the .csv file
3. use len() to find the number of rows
4. print the number of rows
  
## Sources used:
https://www.datacamp.com/community/tutorials/pandas-read-csv
https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python
