# import sys
# from fileinput import filename
#
# from pyspark.sql import *
#
# if __name__ == '__main__':
#     spark = SparkSession \
#         .builder \
#         .appName("SparkWebUIDemo") \
#         .master("local[2]") \
#         .getOrCreate()
#
#     rawDF = spark.read \
#     .option("inferSchema", "true")\
#     .option("header", "true")\
#     .csv("")
