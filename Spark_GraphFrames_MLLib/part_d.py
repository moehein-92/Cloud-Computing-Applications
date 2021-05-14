from pyspark.ml.classification import RandomForestClassifier
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.types import StringType, FloatType, StructType, StructField
from pyspark.sql.functions import *
import pyspark.sql.functions as F

sc = SparkContext()
sqlContext = SQLContext(sc)

def predict(df_train, df_test):
    # Train random forest classifier

    vecAssembler = VectorAssembler(inputCols=["f1","f2","f3","f4","f5","f6","f7","f8"], outputCol="features")
    new_train_df = vecAssembler.transform(df_train)
    #new_train_df.show()

    algo = RandomForestClassifier(featuresCol='features', labelCol='label', seed=10, maxDepth=5, numTrees=10)
    model = algo.fit(new_train_df)

    new_test_df = vecAssembler.transform(df_test)
    #new_test_df.show()

    predictions = model.transform(new_test_df)
    #predictions.show()

    predictions = [int(row['prediction']) for row in predictions.collect()]
    return predictions

def parse_line(line):
    line = line.split(',')
    s = [float(x) for x in line]
    return s


def main():

    # TRAIN DATA
    raw_training_data = sc.textFile("dataset/training.data")
    rdd_train = raw_training_data.map(parse_line)
        
    train_schema = StructType([
                    StructField('f1', FloatType(), True),
                    StructField('f2', FloatType(), True),
                    StructField('f3', FloatType(), True),
                    StructField('f4', FloatType(), True),
                    StructField('f5', FloatType(), True),
                    StructField('f6', FloatType(), True),
                    StructField('f7', FloatType(), True),
                    StructField('f8', FloatType(), True),
                    StructField('label', FloatType(), True)])

    df_train = sqlContext.createDataFrame(rdd_train, train_schema)
    #df_train.show()

    
    # TEST DATA
    raw_test_data = sc.textFile("dataset/test-features.data")
    rdd_test = raw_test_data.map(parse_line)
    
    test_schema = StructType([
                    StructField('f1', FloatType(), True),
                    StructField('f2', FloatType(), True),
                    StructField('f3', FloatType(), True),
                    StructField('f4', FloatType(), True),
                    StructField('f5', FloatType(), True),
                    StructField('f6', FloatType(), True),
                    StructField('f7', FloatType(), True),
                    StructField('f8', FloatType(), True)])

    df_test = sqlContext.createDataFrame(rdd_test, test_schema)
    #df_test.show()

    # MACHINE LEARNING
    predictions = predict(df_train, df_test)

    for pred in predictions:
        print(int(pred))


if __name__ == "__main__":
    main()
