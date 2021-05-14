
1 Overview

You have been provided an airlines dataset consisting of 5 CSV files and you need to analyze this data and obtain meaningful insights from it. In order to do so, you would first have to perform a simplified version of ETL (Extract, Transform, Load) on these CSV files using AWS Glue. You will then select a subset of this data based on some constraints through AWS Athena using a SQL query. This filtered dataset will then be used inside Tableau for visualization and  gaining further insight into it. 

2 Requirements

You will need an AWS account (AWS Athena and Glue are available on educate accounts) and install Tableau software on your local machine. You will need to learn SQL to perform filtering on top of Athena and get familiar with Tableau. Please use region -> us-east-1 for your deployment.

3 Procedure

3.1 AWS Glue Setup

You can download the dataset (flights-dataset.zip) ~ 50MB from below. Once you download this dataset, you will have to upload the csv files to your AWS account S3 storage in order for Glue to access it. 

In order to run your ETL job on this S3 dataset, you need to first configure AWS Glue so that it has the metadata required to read from S3 and create/monitor your jobs. You will then use a crawler to populate the Glue Data catalog with the metadata for the datastore (S3 Bucket where the flights csv files are stored). Create a Database within the data catalog and run the crawler. It will create a table under that database. You should manually verify the relevant properties and the schema in order to ensure that the correct ones have been extracted by the crawler. The database and the table that you created through AWS Glue are also going to reflect in Athena. 

https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html  

3.2  Query and Filtering through AWS Athena

W​hat is AWS Athena: https://docs.aws.amazon.com/athena/latest/ug/what-is.html  

SQL Reference for Athena: https://docs.aws.amazon.com/athena/latest/ug/ddl-sql-reference.html

You should be able to view the table created through the Glue inside AWS Athena reflecting the total entries of 479230 (with header trimmed). You need to now come up with a SQL query for the following:

Select all possible trips from SFO to JFK with 1 stop-over airport in between such that: 
60 minutes <= stop-over time <= 180 minutes. Here, the stop-over time is the difference between the arrival time of the first flight and the departure time of the second flight. Note that we are using arrival time and departure time (not scheduled arrival time or scheduled departure time). Also, note that some of the formats of timings in the dataset are in integer format as HHMM (i.e., 1730 means 5.30 PM), and some are in minutes. If a flight is scheduled at 23:50 (shown as 2350) and delayed for 20 minutes, the departure time will be 00:10 (shown as 10), then the DAY column value does not reflect the actual departure date.
 Both the flights on a given trip should belong to the same airline.
Neither of the two flights was canceled. The first flight cannot be diverted. It is OK if the second flight is diverted, as people can still get on it. 
You need to output the following columns for each trip: Day, Airline, Origin Airport, Stop-over Airport, Destination Airport, Origin Departure Delay, Stop-over Arrival Delay, Stop-over Departure Delay,  Destination Arrival Delay. Note that there should be one row for each trip in the output. Please save the count of entries you obtain from your query as you would need to submit this parameter to the autograder.

Save the output results from this query in a CSV file that will be used by Tableau for the tasks below. 

3.3 Tableau Setup

As a student, you're eligible for a free Tableau Desktop license through Tableau for Students. In order to download and install Tableau, you need to first fill out this form, providing your .illinois.edu email address. 

Next, you will receive an email on your email account with download links along with the product key. You will be using the product key during installation.

Note that Tableau Desktop can only be installed on MacOS (version >=10.13) or Windows. You may have to use virtual machines if you are using other OSes. 

If you would like more info on how to use Tableau, please check out the Tableau Tutorial. You can also refer to the first 30 minutes of this video.

3.4 Tableau Visualization

Using the output CSV from 3.2, you need to create two visualizations.

In the Tableau window, click on the File menu and then New. Next, you need to connect to the CSV file. Once connected, you create two worksheets one for each of the tasks below, and save the results as mentioned. 

Create a bar chart to show the count of flights between SFO and different stop-over airports. Now you need to save the data corresponding to this visualization as follows: Right-click on the visualization, then click "View Data", ensure that "Summary Data" is selected at the bottom, and finally click on "Export All" to save the data into a file named “mp9-viz1.tsv” or “mp9-viz1.csv” depending on whether your file is tab or comma-separated.
Create a scatter plot with Stop-over Departure Delay at the intermediate airport as x-axis and Destination Arrival Delay at JFK as Y-axis. Now create two filters: one for Stop-over Departure Delay, and another for Destination Arrival Delay. Set the range of Departure Delay filter from 200 to 260 and Arrival Delay filter from 110 to 220. Similar to the above task, you can now save the data corresponding to this visualization as follows: Right-click on the visualization, then click "View Data", ensure that "Summary Data" is selected at the bottom, and finally click on "Export All" to save the data into a file named “mp9-viz2.tsv” or “mp9-viz2.csv” depending on whether your file is tab or comma-separated.
4. Submission

You need to download test.py attached below in order to submit your work. You need to modify the required parameters within test.py which takes in your email address, Coursera secret token, and the number of filtered entries from 3.2 along with the two file paths corresponding to the csv files from 3.4. Please also double-check the viz1StopOverColumn and viz2ArrivalDelayColumn. 

The  delimiter used in the output file from tableau can be ','  instead of '\t'. However, test.py uses '\t' as the delimiter by default. If your output is comma-separated,  please update the delimiter inside test.py at line 28 as follows:

Change:

reader =  csv.reader((line.replace('\0','') for line in csvfile), delimiter='\t')  

 to 

reader = csv.reader((line.replace('\0','') for line in csvfile), delimiter=',') 

Execute test.py which will update your grade or provide you with an error message. 

The test.py should output a payload similar to the following

{"student": {"submitterEmail": "*@illinois.edu", "secret": ""}, "numFilteredEntries": 0, "viz1": {"SLC": 5, ...}, "viz2": {"206": 226,... }}
