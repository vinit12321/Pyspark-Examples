import sys

from pyspark import SparkConf
from collections import namedtuple

from pyspark.sql import SparkSession


from lib.logger import Log4j

if __name__ == "__main__":
    conf = SparkConf() \
        .setMaster("local[3]") \
        .setAppName("HelloRDD")

    # sc = SparkContext(conf=conf)
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    sc = spark.sparkContext