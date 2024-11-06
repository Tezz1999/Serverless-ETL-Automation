from pyspark.sql import SparkSession
import os

# Set Hadoop Home (required on Windows for PySpark)
os.environ["HADOOP_HOME"] = "C:/hadoop/hadoop-3.3.6"
os.environ["PATH"] += os.pathsep + "C:/hadoop/hadoop-3.3.6/bin"

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Test SQL Server Connection") \
    .config("spark.jars", "C:/Users/TEJ/Desktop/Projects/serverless etl automation/jdbc-connectors/mssql-jdbc-12.8.1.jre11.jar") \
    .getOrCreate()

# Connection properties for SQL Server
jdbc_url = "jdbc:sqlserver://LAPTOP-KI8F8A9A\\SQLEXPRESS;databaseName=StackOverflowSurvey;integratedSecurity=true;"
connection_properties = {
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

# Sample DataFrame to test the connection
data = [("John Doe", 29), ("Jane Smith", 34)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Write DataFrame to SQL Server
try:
    df.write.jdbc(url=jdbc_url, table="TestTable", mode="overwrite", properties=connection_properties)
    print("Successfully connected to the database and inserted data into TestTable.")
except Exception as e:
    print(f"Failed to connect to the database: {e}")
