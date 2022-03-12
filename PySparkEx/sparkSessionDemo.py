import sys
import pyspark 
from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.master("local[2]") \
    .appName("Spark Session") \
    .getOrCreate()

    sp3 = SparkSession.newSession
    
    print(sp3.toString())
