from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField, IntegerType, StringType, DecimalType
)
import os
os.environ["HADOOP_HOME"] = "C:/hadoop/hadoop-3.3.6"
os.environ["PATH"] += os.pathsep + "C:/hadoop/hadoop-3.3.6/bin"

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Chunked Data Load to SQL Server") \
    .config("spark.jars", "C:/Users/TEJ/Desktop/Projects/serverless etl automation/jdbc-connectors/mssql-jdbc-12.8.1.jre11.jar")\
    .getOrCreate()

# Define schema for the data
schema = StructType([
    StructField("ResponseId", IntegerType(), False),
    StructField("Q120", StringType(), True),
    StructField("MainBranch", StringType(), True),
    StructField("Age", StringType(), True),
    StructField("Employment", StringType(), True),
    StructField("RemoteWork", StringType(), True),
    StructField("CodingActivities", StringType(), True),
    StructField("EdLevel", StringType(), True),
    StructField("LearnCode", StringType(), True),
    StructField("LearnCodeOnline", StringType(), True),
    StructField("LearnCodeCoursesCert", StringType(), True),
    StructField("YearsCode", StringType(), True),
    StructField("YearsCodePro", StringType(), True),
    StructField("DevType", StringType(), True),
    StructField("OrgSize", StringType(), True),
    StructField("PurchaseInfluence", StringType(), True),
    StructField("TechList", StringType(), True),
    StructField("BuyNewTool", StringType(), True),
    StructField("Country", StringType(), True),
    StructField("Currency", StringType(), True),
    StructField("CompTotal", DecimalType(15, 2), True),
    StructField("LanguageHaveWorkedWith", StringType(), True),
    StructField("LanguageWantToWorkWith", StringType(), True),
    StructField("DatabaseHaveWorkedWith", StringType(), True),
    StructField("DatabaseWantToWorkWith", StringType(), True),
    StructField("PlatformHaveWorkedWith", StringType(), True),
    StructField("PlatformWantToWorkWith", StringType(), True),
    StructField("WebframeHaveWorkedWith", StringType(), True),
    StructField("WebframeWantToWorkWith", StringType(), True),
    StructField("MiscTechHaveWorkedWith", StringType(), True),
    StructField("MiscTechWantToWorkWith", StringType(), True),
    StructField("ToolsTechHaveWorkedWith", StringType(), True),
    StructField("ToolsTechWantToWorkWith", StringType(), True),
    StructField("OpSysPersonalUse", StringType(), True),
    StructField("OpSysProfessionalUse", StringType(), True),
    StructField("OfficeStackAsyncHaveWorkedWith", StringType(), True),
    StructField("OfficeStackAsyncWantToWorkWith", StringType(), True),
    StructField("OfficeStackSyncHaveWorkedWith", StringType(), True),
    StructField("OfficeStackSyncWantToWorkWith", StringType(), True),
    StructField("SOAI", StringType(), True),
    StructField("AISelect", StringType(), True),
    StructField("AISent", StringType(), True),
    StructField("AIAcc", StringType(), True),
    StructField("AIBen", StringType(), True),
    StructField("AIToolInterested", StringType(), True),
    StructField("AIToolUsing", StringType(), True),
    StructField("SOVisitFreq", StringType(), True),
    StructField("SOAccount", StringType(), True),
    StructField("SOPartFreq", StringType(), True),
    StructField("SOComm", StringType(), True),
])

# Load CSV data
csv_path = "C:/Users/TEJ/Desktop/Projects/serverless etl automation/stack-overflow-developer-survey-2023/survey_results_public.csv"
df = spark.read.csv(csv_path, header=True, schema=schema)

# Connection properties for SQL Server using Windows Authentication
jdbc_url = "jdbc:sqlserver://LAPTOP-KI8F8A9A\\SQLEXPRESS;databaseName=StackOverflowSurvey;integratedSecurity=true;"
connection_properties = {
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

# Define chunk size
chunk_size = 1000
total_rows = df.count()

# Loop through the DataFrame in chunks
for start in range(0, total_rows, chunk_size):
    chunk_df = df.limit(chunk_size)  # Simulate chunking logic
    chunk_df.write.jdbc(url=jdbc_url, table="YourTableName", mode="append", properties=connection_properties)

print("Data load complete.")
