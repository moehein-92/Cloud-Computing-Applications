from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType

sc = SparkContext()
sqlContext = SQLContext(sc)

def splitter(line):
    word, count1, count2, count3 = line.split('\t')
    return (word, count1, count2, count3)

f = sc.textFile("gbooks")
f = f.map(splitter)


schema = StructType([StructField('word', StringType(), True),
                     StructField('count1', IntegerType(), True),
                     StructField('count2', IntegerType(), True),
                     StructField('count3', IntegerType(), True),])

df = sqlContext.createDataFrame(f, schema)
df.printSchema()


