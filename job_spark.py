from pyspark import SparkFiles
from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseEnem2020Spark")
    .getOrCreate()
)

## Ler os dados do ENEM 2020
# enem = dataframe spark 

enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .options(encoding='ISO-8859-1')
    .load("s3://<caminho-lake>+<arquivo csv>")
)

## Grava dados em Parquet
(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("NU_ANO")
    .save("s3://<caminho-lake-repositorio-parquet>")
)