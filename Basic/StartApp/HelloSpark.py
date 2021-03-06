import sys
from pyspark.sql import *
from loglib.logger import Log4j
from loglib.utils import *

from Basic.HelloSpark.loglib.utils import get_spark_app_config, load_survey_df, count_by_country

if __name__ == "__main__":
    conf = get_spark_app_config()

    spark = SparkSession \
        .builder \
        .appName("HelloSpark") \
        .master("local[2]") \
        .getOrCreate()

    logger = Log4j(spark)

    if len(sys.argv) != 2:
        logger.error("Usage: HelloSpark <filename>")
        sys.exit(-1)

    logger.info("Starting HelloSpark")

    """
    Actions: Read, write , collect, show, count
    """
    survey_raw_df = load_survey_df(spark, sys.argv[1])
    # survey_raw_df.show()

    filtered_survey_df = survey_raw_df \
        .where("Age < 40") \
        .select("Age", "Gender", "Country", "state")

    # filtered_survey_df.show()

    partitioned_survey_df = survey_raw_df.repartition(2)
    count_df = count_by_country(partitioned_survey_df)
    #count_df.show()
    logger.info(count_df.collect())

    logger.info("Finished HelloSpark")
    input("Press Enter")
    #spark.stop()
