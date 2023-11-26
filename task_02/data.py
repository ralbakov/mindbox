from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = (
    SparkSession.builder
         .master("local[*]")
         .appName("PySpark_Tutorial")
         .getOrCreate()
)

prod_data = [
    (1, "Тунец"),
    (2, "Колбаса"),
    (3, "Рис"),
    (4, "Хлеб"),
    (5, "Соль"),
    (6, "Молоко"),
    (7, "Сыр"),
    (8, "Уксус"),
    (9, "Мед"),
    (10, "Лук"),
]

prod_schema = StructType([
    StructField("prod_id", IntegerType()),
    StructField("prod_name", StringType()),
])

category_data = [
    (1, "Рыба"),
    (2, "Мясо"),
    (3, "Полуфабрикаты"),
    (4, "Бакалея"),
    (5, "Крупы"),
    (6, "Выпечка"),
    (8, "Молочка"),
    (11, "Овощи"),
]

category_schema = StructType([
    StructField("category_id", IntegerType()),
    StructField("category_name", StringType()),
])

prod_category_data = [
    (1, 1),
    (2, 2),
    (2, 3),
    (3, 4),
    (3, 5),
    (4, 4),
    (4, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
    (9, 10),
    (10, 11),
]

prod_category_schema = StructType([
    StructField("prod_id", IntegerType()),
    StructField("category_id", IntegerType()),
])


product = spark.createDataFrame(data=prod_data, schema=prod_schema)
category = spark.createDataFrame(data=category_data, schema=category_schema)
product_category = spark.createDataFrame(data=prod_category_data, schema=prod_category_schema)

df_result = product.join(product_category, on=["prod_id"], how="left") \
    .join(category, on=["category_id"], how="left") \
    .select("prod_name", "category_name")

df_result.show()
print(type(df_result))