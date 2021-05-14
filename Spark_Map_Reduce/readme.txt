1 Overview
Welcome to the Spark MapReduce programming assignment. You have to implement the solution of this machine problem in Python. It is highly recommended that you practice the Tutorial: Docker installation (under week 4) and Tutorial: Introduction to Apache Sparkbefore beginning this assignment.

2 General Requirements
Please note that our grader runs on a docker container and is NOT connected to the internet. Therefore, no additional libraries are allowed for this assignment ( (you can only use the default libraries of python)). Also, you will NOT be allowed to create any file or folder outside the current folder (that is, you can only create files and folders in the folder that your solutions are in).

3 Sorting
When you are to select top N items in a list, sorting is implicitly needed. Use the following steps to sort:

1. Sort the list ASCENDING based on Firstly count then Secondly on the key. If the key is string, sort lexicographically.

2. Select the bottom N items in the sorted list as Top items.

There is an implementation of this logic in the the third example of the Hadoop MapReduce Tutorial.

For example, to select top 5 items in the list {"A": 100, "B": 99, "C":98, "D": 97, "E": 96, "F": 96, "G":90}, first sort the items ASCENDING:

"G":90

"E": 96

"F": 96

"D": 97

"C":98

"B": 99

"A": 100

Then, the bottom 5 items are A, B, C, D, F.

Another example, to select 5 top items in the list {"43": 100, "12": 99, "44":98, "12": 97, "1": 96, "100": 96, "99":90}

"99":90

"1": 96

"100": 96

"12": 97

"44":98

"12": 99

"43": 100

Then, the bottom 5 items are 43, 12, 44, 12, 100.

Python submission
1 Requirements
This assignment will be graded based on Python 3

2 Procedures
Step 1: Run the provided Docker image (please follow "Tutorial: Docker installation" in week 4)


Step 2: Download the project files


# git clone https://github.com/UIUC-CS498-Cloud/MP5_SparkMapReduce_Template.git
step 3: Change the current folder to


# cd # git clone MP5_SparkMapReduce_Template/
step 4: Finish the exercises by editing the provided templates files. All you need to do is complete the parts marked with TODO. Please note that you are NOT allowed to import any additional libraries.

Each exercise has one or more code template. All you must do is edit these files.
The code will be run on the provided Docker image.
For partial credit: Only submit the files related to the exercise in a zip format (MP2.zip). Example: For part A, only submit TopTitlesSpark.py files to receive a partial credit.
More information about these exercises is provided in the next section.

step 5: After you are done with the assignments, put all your 5 python files (TopTitlesSpark.py, TopTitlesStatisticsSpark.py, OrphanPagesSpark.py, TopPolularLinksSpark.py, PopularityLeagueSpark.py) into a .zip file named as "MP2Spark.zip". Submit your "MP2Spark.zip".

Exercise A: Top Titles
In this exercise, you are going to implement a counter for words in Wikipedia titles and an application to find the top words used in these titles. To make the implementation easier, we have provided a boilerplate for this exercise in the following files: TitleCountSpark.py 

All you need to do is make the necessary changes to parts that are marked with TODO.

Your application takes a huge list of Wikipedia titles (one in each line) as an input and first tokenizes them using provided delimiters, after that make the tokens lowercased, then removes common words from the provided stopwords. Next, your application selects top 10 words, and finally, saves the count for them in the output. Use the method in section 3 Sorting to select top words.

You should first tokenize Wikipedia titles, make the tokens lowercased, remove common words, and save the count for the words in the output.

You can test your output with:


# spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ partA
If you want to check your output, run:


# cat partA
Here is the output of an application that selects top 5 words in alphabetical order (after they are selected based on count):


The order of lines matters. Please sort the output (key value) in alphabetic order. Also, make sure the key and value pair in final output are tab separated.

Exercise B: Top Title Statistics
In this exercise, you are going to implement an application to find some statistics about the top words used in Wikipedia titles. To make the implementation easier, we have provided a boilerplate for this exercise in the following files: TopTitleStatisticsSpark.py

All you need to do is make the necessary changes to parts that are marked with TODO.

Your output from Exercise A will be used here. The application saves the following statistics about the top words in the output: “Mean” count, “Sum” of all counts, “Minimum” and “Maximum” of counts, and “Variance” of the counts. All values should be floored to be an integer. For the sake of simplicity, simply use Integer in all calculations.

The following is the sample command we will use to run the application:


# spark-submit TopTitleStatisticsSpark.py partA partB
If you want to check your output, run:


# cat partB
Here is the output of an application that selects top 5 words:


Make sure the stats and the corresponding results are tab separated.

Exercise C: Orphan Pages
In this exercise, you are going to implement an application to find orphan pages in Wikipedia. To make the implementation easier, we have provided a boilerplate for this exercise in the following files: OrphanPagesSpark.py

All you need to do is make the necessary changes to parts that are marked with TODO.

Your application takes a huge list of Wikipedia links (not Wikipedia titles anymore) as an input. All pages are represented by their ID numbers. Each line starts with a page ID, which is followed by a list of all the pages that the ID has a link to. The following is a sample line in the input:


In this sample, page 2 has links to page 3, 747213, and so on. Note that links are not necessarily two-way. The application should save the IDs of orphan pages in the output. Orphan pages are pages to which no other pages link.

The following is the sample command we will use to run the application:


# spark-submit OrphanPagesSpark.py dataset/links/ partC
If you want to check your output, run:


# cat partC
If you want to check a part of your output, run:


# head partC
Here is a part of the output of this application:


The order of lines matters. Please sort your output (key value) in alphabetic order.

Exercise D: Top Popular Links
In this exercise, you are going to implement an application to find the most popular pages in Wikipedia. To make the implementation easier, we have provided a boilerplate for this exercise in the following files: TopPopularLinksSpark.py

All you need to do is make the necessary changes to parts that are marked with TODO.

Your application takes a huge list of Wikipedia links as an input. All pages are represented by their ID numbers. Each line starts with a page ID, which is followed by a list of all the pages that the ID has a link to. The following is a sample line in the input:


In this sample, page 2 has links to page 3, 747213, and so on. Note that links are not necessarily two-way. The application should save the IDs of top 10 popular pages as well as the number of links to them in the output. A page is popular if more pages are linked to it. Use the method in section 3 Sorting to select top links.

The following is the sample command we will use to run the application:

# spark-submit TopPopularLinksSpark.py dataset/links/ partD
If you want to check your output, run:


# cat partD
Here is the output of an application that selects top 5 popular links:


The order of lines matters. Please sort your output (key value) in alphabetic order. Also, make sure the key and value pair in final output are tab separated.

Exercise E: Popularity League
In this exercise, you are going to implement an application to find the most popular pages in Wikipedia. To make the implementation easier, we have provided a boilerplate for this exercise in the following file: PopularityLeagueSpark.py

All you need to do is make the necessary changes to parts that are marked with TODO.

Your application takes a huge list of Wikipedia links as an input. All pages are represented by their ID numbers. Each line starts with a page ID, which is followed by a list of all the pages that the ID has a link to. The following is a sample line in the input:


In this sample, page 2 has links to page 3, 747213, and so on. Note that links are not necessarily two-way.

The popularity of a page is determined by the number of pages in the whole Wikipedia graph that link to that specific page. (Same number as Exercise D)

The application also takes a list of page IDs as an input (also called a league list). The goal of the application is to calculate the rank of pages in the league using their popularity.

The rank of the page is the number of pages in the league with less popularity than the original page.

The following is the sample command we will use to run the application:

# spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt partE
If you want to check your output, run:

# cat partE
Here is the output with League={5300058,3294332,3078798,1804986,2370447,81615,3,1}):


Here is the output with League={88822,774931,4861926,1650573,66877,5115901,75323,4189215}):


The order matters. Please sort your output (key value) in alphabetic order. Also, make sure the key and value pair in final output are tab separated. 

Note that we will use a different League file in our test.
