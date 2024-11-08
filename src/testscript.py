from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import gc

# Initialize Spark session
spark = SparkSession.builder \
    .appName("StackOverflowSurveyData") \
    .config("spark.jars", "./work/jdbc-connectors/postgresql-42.7.4.jar") \
    .config("spark.driver.extraClassPath", "./work/jdbc-connectors/postgresql-42.7.4.jar") \
    .config("spark.executor.extraClassPath", "./work/jdbc-connectors/postgresql-42.7.4.jar") \
    .getOrCreate()

# JDBC configurations
jdbc_url = "jdbc:postgresql://postgres:5432/StackOverflowSurveyData"
db_properties = {
    "user": "myuser",
    "password": "myuser",
    "driver": "org.postgresql.Driver"
}

# Define CSV file path
csv_file_path = "./work/data/stack-overflow-developer-survey-2023/survey_results_public.csv"

# Load data from CSV
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

# Helper function to load DataFrame to PostgreSQL and clear memory
def load_to_postgres(dataframe, table_name):
    dataframe.write.jdbc(url=jdbc_url, table=table_name, mode="append", properties=db_properties)
    del dataframe
    gc.collect()

# Load UserProfile table
user_profile_df = df.select(
    col("ResponseId").cast("int"),
    col("Age").cast("string"),
    col("Employment").cast("string"),
    col("RemoteWork").cast("string"),
    col("EdLevel").cast("string"),
    col("Country").cast("string"),
    col("CompTotal").cast("decimal(15, 2)"),
    col("ConvertedCompYearly").cast("decimal(15, 2)")
)
load_to_postgres(user_profile_df, "UserProfile")

# Load ProfessionalTech table
professional_tech_df = df.select(
    col("ResponseId").cast("int"),
    col("DevType").cast("string"),
    col("OrgSize").cast("string"),
    col("PurchaseInfluence").cast("string"),
    col("TechList").cast("string"),
    col("BuyNewTool").cast("string")
)
load_to_postgres(professional_tech_df, "ProfessionalTech")

# Load TechPreferences table
tech_preferences_df = df.select(
    col("ResponseId").cast("int"),
    col("LanguageHaveWorkedWith").cast("string"),
    col("LanguageWantToWorkWith").cast("string"),
    col("DatabaseHaveWorkedWith").cast("string"),
    col("DatabaseWantToWorkWith").cast("string"),
    col("PlatformHaveWorkedWith").cast("string"),
    col("PlatformWantToWorkWith").cast("string"),
    col("WebframeHaveWorkedWith").cast("string"),
    col("WebframeWantToWorkWith").cast("string"),
    col("MiscTechHaveWorkedWith").cast("string"),
    col("MiscTechWantToWorkWith").cast("string"),
    col("ToolsTechHaveWorkedWith").cast("string"),
    col("ToolsTechWantToWorkWith").cast("string")
)
load_to_postgres(tech_preferences_df, "TechPreferences")

# Load TechStackUsage table
tech_stack_usage_df = df.select(
    col("ResponseId").cast("int"),
    col("OpSysPersonal use").alias("OpSysPersonalUse").cast("string"),
    col("OpSysProfessional use").alias("OpSysProfessionalUse").cast("string"),
    col("OfficeStackAsyncHaveWorkedWith").cast("string"),
    col("OfficeStackAsyncWantToWorkWith").cast("string"),
    col("OfficeStackSyncHaveWorkedWith").cast("string"),
    col("OfficeStackSyncWantToWorkWith").cast("string")
)
load_to_postgres(tech_stack_usage_df, "TechStackUsage")

# Load AIInteraction table
ai_interaction_df = df.select(
    col("ResponseId").cast("int"),
    col("SOAI").cast("string"),
    col("AISelect").cast("string"),
    col("AISent").cast("string"),
    col("AIAcc").cast("string"),
    col("AIBen").cast("string"),
    col("AIToolInterested in Using").alias("AIToolInterested").cast("string"),
    col("AIToolCurrently Using").alias("AIToolUsing").cast("string")
)
load_to_postgres(ai_interaction_df, "AIInteraction")

# Load SurveyInteraction table
survey_interaction_df = df.select(
    col("ResponseId").cast("int"),
    col("SOVisitFreq").cast("string"),
    col("SOAccount").cast("string"),
    col("SOPartFreq").cast("string"),
    col("SOComm").cast("string")
)
load_to_postgres(survey_interaction_df, "SurveyInteraction")

# Stop the Spark session
spark.stop()
