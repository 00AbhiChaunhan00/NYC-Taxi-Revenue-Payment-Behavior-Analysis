import pandas as pd

df = pd.read_parquet("yellow_tripdata_2025-01.parquet")
# print(df.columns)

df = df[[
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
    "passenger_count",
    "trip_distance",
    "payment_type",
    "fare_amount",
    "total_amount"
]]

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# print(df.head())


# check the null value
print(df.isnull().sum())


# to check duplicate value
print("Duplicate rows:", df.duplicated().sum())


# verifying the payment_type
print(df["payment_type"].value_counts())


# checking the fare_amount
print(df["fare_amount"].describe())
print("Zero Fare:", (df["fare_amount"] == 0).sum())
print("Negative Fare:", (df["fare_amount"] < 0).sum())


# checking the trip_distance
print(df["trip_distance"].describe())
print("Zero Distance:", (df["trip_distance"] == 0).sum())
print("Negative Distance:", (df["trip_distance"] < 0).sum())


# checking the date columns
invalid_time = (
    df["tpep_dropoff_datetime"] <=
    df["tpep_pickup_datetime"]
).sum()

print("Invalid Trip Times:", invalid_time)


# =========================
# BASIC DATA CLEANING
# =========================

# Keep original dataframe safe
df_clean = df.copy()

print("Rows Before Cleaning:", len(df_clean))


# 1. Keep only Card and Cash payments
# 1 = Credit Card
# 2 = Cash
df_clean = df_clean[
    df_clean["payment_type"].isin([1, 2])
]


# 2. Remove zero and negative fares
df_clean = df_clean[
    df_clean["fare_amount"] > 0
]


# 3. Remove zero-distance trips
df_clean = df_clean[
    df_clean["trip_distance"] > 0
]


# 4. Remove invalid trip times
df_clean = df_clean[
    df_clean["tpep_dropoff_datetime"] >
    df_clean["tpep_pickup_datetime"]
]


# Reset index
df_clean = df_clean.reset_index(drop=True)


# =========================
# CHECK CLEANED DATA
# =========================

print("Rows After Cleaning:", len(df_clean))
print("Rows Removed:", len(df) - len(df_clean))

print("\nPayment Types:")
print(df_clean["payment_type"].value_counts())

print("\nFare Summary:")
print(df_clean["fare_amount"].describe())

print("\nDistance Summary:")
print(df_clean["trip_distance"].describe())

print("\nMissing Values:")
print(df_clean.isnull().sum())


# =========================
# OUTLIER DETECTION
# =========================

Q1 = df_clean["fare_amount"].quantile(0.25)
Q3 = df_clean["fare_amount"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print(
    "Fare Outliers:",
    (
        (df_clean["fare_amount"] < lower_bound) |
        (df_clean["fare_amount"] > upper_bound)
    ).sum()
)


# =========================
# CALCULATED COLUMN
# =========================

# Calculate trip duration in minutes
df_clean["duration_minutes"] = (
    df_clean["tpep_dropoff_datetime"] -
    df_clean["tpep_pickup_datetime"]
).dt.total_seconds() / 60


# =========================
# REPLACE PAYMENT TYPE
# =========================

df_clean["payment_type"] = df_clean["payment_type"].replace({
    1: "Credit Card",
    2: "Cash"
})


# =========================
# FINAL CHECK
# =========================

print("\nFinal Payment Types:")
print(df_clean["payment_type"].value_counts())

print("\nDuration Summary:")
print(df_clean["duration_minutes"].describe())

print("\nFinal Dataset Shape:")
print(df_clean.shape)

print("\nFinal Columns:")
print(df_clean.columns)


# =========================
# STORE CLEANED FILE
# =========================

df_clean.to_parquet(
    "yellow_taxi_cleaned.parquet",
    index=False
)

print("\nCleaned dataset saved!")