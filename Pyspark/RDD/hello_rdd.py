import findspark
findspark.init()
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
conf = SparkConf() \
        .setMaster("local[3]") \
        .setAppName("HelloRDD")

    # sc = SparkContext(conf=conf)
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext
print("COnnected")
print(type(sc))