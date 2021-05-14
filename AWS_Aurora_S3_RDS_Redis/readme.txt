1  Overview
In this MP, we are going to explore AWS RDS, ElastiCache as well as S3, and how using ElastiCache can boost RDS performance. Specifically, you will build a storage service to support read and write queries on data stored in a relational database. The read and write APIs are built using Lambda functions. Your goal is to demonstrate the performance benefits of using caching to improve performance of database queries.

2 Requirements
You need a valid AWS account and will be working on Lambda, API Gateway, RDS, ElastiCache and S3. Note that AWS Educate account doesn't have access to Redis Service, so you will need to use your personal account. It will be easier to configure if all services are running on your personal account. Also, you need to be familiar with one of the following programming languages for implementing lambda: Python / Javascript / Java / Go. While we will make every attempt to help out irrespective of your chosen language, we can best assist with python 3. Please try to implement your Lambda in us-east-1.

3 Populate database and set up Redis cluster
3.1 Amazon S3 setup
First, we setup S3 bucket and load the content for populating the database.

Step 1: Set up an Amazon S3 bucket and upload mp11input.csv into the bucket, reference the tutorial:
 https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html


3.2 Setup and populate Amazon Aurora 
Step 2: Create an IAM policy and IAM role for Amazon Aurora to access Amazon S3
Next, create an IAM policy and IAM role for Amazon Aurora database, use the following tutorials for reference.

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.S3CreatePolicy.html  

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.CreateRole.htm

Step 3: Setup Amazon Aurora database
Create an Amazon Aurora database. Reference the 2 tutorials listed below, and use the following settings: Make sure publicly accessible is selected. Make sure to create a custom DB cluster parameter group and assign the IAM role you created to parameters that allow Aurora to access S3. Attach the IAM role created in step 2 to the database just created. 

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.Aurora.html

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.AddRoleToDBCluster.html

Step 4: Populate database using data in Amazon S3
Next, load data from mp11input.csv which is stored in S3 bucket created in step 1 into database. Reference the tutorial:

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.LoadFromS3.htm

To access aurora, you can use mysql from an EC2 instance like in this tutorial. 

https://aws.amazon.com/getting-started/hands-on/boosting-mysql-database-performance-with-amazon-elasticache-for-redis/

An example command would be mysql -h rds_writer_endpoint -P 3306 -u admin -p

Before loading the csv into Aurora, you should create a database and a table. The table should have the following fields: id, hero, power, name, xp, color. Don't change these filed names as the autograder is hardcoded with these names. 

For basic mysql operations, this tutorial should help.

https://dev.mysql.com/doc/mysql-getting-started/en/

3.3 Create a Redis Cluster
For creating a redis cluster, you can refer to the following tutorial:

https://aws.amazon.com/getting-started/hands-on/boosting-mysql-database-performance-with-amazon-elasticache-for-redis/module-one/

Unfortunately, AWS Educate cannot create Redis. You need to use a personal account to do that. To save money, you can try to scale down the instance for both RDS and ElastiCache. 

4 Create Lambda function 

You can refer to MP2 for creating Lambda function. Unlike some of the previous MPs, third party libraries can be imported in this MP. If you choose to use Python for this MP, you will need to refer to the following tutorial for importing two modules pymysql and redis:

https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

If you choose to use other languages, please refer to the AWS' official documentation to figure out how to import third-party libraries in https://docs.aws.amazon.com/lambda/latest/dg/welcome.html.

You can refer to this template when writing your lambda function.

mp6_template.py
The following example might also help you.

https://github.com/aws-samples/amazon-elasticache-samples/blob/master/database-caching/example.py

4.2 Read/Write API
There are different strategies of using cache. You can refer to this document for more details https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/Strategies.html. In this MP, we ask you to enable lazy loading and write through strategies. 

Specifically, the autograder will send read requests with the following format:

12345
{
  "USE_CACHE": "True",
  "REQUEST": "read",
  "SQLS": [1,2,3]
}
We would like you to return the corresponding rows with the ids that's in SQLS list (you need to create a list and append the corresponding rows to the list, which you need to return at the end of the api call). If USE_CACHE is true, check if Redis contains the id. If not, store the row returned by RDS in Redis, and then return the result. Note that choice of key and value in Redis is totally up to you. The autograder will only ask you for the corresponding rows of the ids. Make sure your response is in json format. 

Our lazy loading test will check if your implementation takes advantage of Redis and boosts the perfomance of querying data. You can test that on your own before submitting.

The write requests examples are as follows,

1234567891011121314151617181920
{
  "USE_CACHE": "True",
  "REQUEST": "write",
  "SQLS": [
    {
      "hero": "yes",
      "name": "fireman",
      "power": "fire",
      "color": "red",
      "xp": "10"

For write request, you will have to insert the new characters in Aurora. If USE_CACHE is true, we would like you to use write-through strategy. Our autograder will check whether your write-through implementation improves the read performance. Make sure your insert the data according to the order of "SQLS"

You can refer to https://aws.amazon.com/getting-started/hands-on/boosting-mysql-database-performance-with-amazon-elasticache-for-redis/module-four/ to get started with the implementation. Refer to

https://pymysql.readthedocs.io/en/latest/
https://redis-py.readthedocs.io/en/latest/
for documentation of pymysql and redis.

At the end of your lambda handler function, the return statement should be as follow

1234
return {
    "statusCode": 200,
    "body": result
}
For read API call, the result should be rows of data in the format of list of dictionaries and in json format. An example is shown below. For write API call, the result should be "write success".

123456789101112131415
return {
    "statusCode": 200,
    "body": [
        {
            "id": 1,
            "hero": "yes",
            "power": "fly",
            "name": "batman",
            "xp": 100,
            "color": "black"

If you are getting "unable to jsonify response or no 'body' key in json" error response, you can try to replicate the problem using the following code. Copy these codes in a new file, replace api with your API POST method url, then run it. 

12345678910
payload = {
        "USE_CACHE": "True",
        "REQUEST": "read",
        "SQLS": [1,2,3]
    }
api = "your dbApi"
r = requests.post(api, data=json.dumps(payload))
res = ""
res = r.json()['body']

5 API setup
Set up an API endpoint for your Lambda function. 
