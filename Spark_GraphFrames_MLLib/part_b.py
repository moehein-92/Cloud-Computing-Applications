from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.clustering import KMeans
from pyspark.ml.linalg import Vectors
import pyspark.sql.functions as F
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.types import StringType, FloatType, StructType, StructField

############################################
#### PLEASE USE THE GIVEN PARAMETERS     ###
#### FOR TRAINING YOUR KMEANS CLUSTERING ###
#### MODEL                               ###
############################################

NUM_CLUSTERS = 4
SEED = 0
MAX_ITERATIONS = 100
INITIALIZATION_MODE = "random"

sc = SparkContext()
sqlContext = SQLContext(sc)


def get_clusters(df, num_clusters, max_iterations, initialization_mode,
                 seed):

    kmeans = KMeans(k=num_clusters, seed=seed, maxIter=max_iterations, initMode=INITIALIZATION_MODE)
    model = kmeans.fit(df.select('features'))
    transformed = model.transform(df)

    return transformed


def parse_line(line):
    s = line.split(',')
    name = s[0]
    features = s[1:]
    features = [float(x) for x in features]
    return (name,) + tuple(features)

if __name__ == "__main__":
    f = sc.textFile("dataset/cars.data")
    rdd = f.map(parse_line)

    schema = StructType([StructField('name', StringType(), True),
                    StructField('f1', FloatType(), True),
                    StructField('f2', FloatType(), True),
                    StructField('f3', FloatType(), True),
                    StructField('f4', FloatType(), True),
                    StructField('f5', FloatType(), True),
                    StructField('f6', FloatType(), True),
                    StructField('f7', FloatType(), True),
                    StructField('f8', FloatType(), True),
                    StructField('f9', FloatType(), True),
                    StructField('f10', FloatType(), True),
                    StructField('f11', FloatType(), True)])

    df = sqlContext.createDataFrame(rdd, schema)

    vecAssembler = VectorAssembler(inputCols=["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11"], outputCol="features")
    new_df = vecAssembler.transform(df)
    #new_df.show()

    clusters = get_clusters(new_df, NUM_CLUSTERS, MAX_ITERATIONS,
                            INITIALIZATION_MODE, SEED)

    for cluster in clusters:
        print(','.join(cluster))
