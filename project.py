import pandas as pd #Pandas is a python library used when working with dataset
import numpy as np #NumPy is a python library used to perform some operations with numbers.

# Read the csv file
df = pd.read_csv("road_accident_dataset.csv")

#Task-2 (Data Collection & Preprocessing)
# Checking if there is any missing values in dataset
print("Before handling missing values")

# Counts missing values per column
print(df.isnull().sum())  

print(df.info())  # Provides an overview of non-null counts

# Applying imputation methods
df["Number of Vehicles Involved"].fillna(df["Number of Vehicles Involved"].mean(), inplace=True)  # Mean
df["Driver Alcohol Level"].fillna(df["Driver Alcohol Level"].median(), inplace=True)  # Median
df["Driver Fatigue"].fillna(df["Driver Fatigue"].mode()[0], inplace=True)  # Mode
df["Pedestrians Involved"].fillna(df["Pedestrians Involved"].median(), inplace=True)

# Rounding the values to the desired decimal places
df["Number of Vehicles Involved"] = df["Number of Vehicles Involved"].round(0)  # Rounding to 0 decimals
df["Driver Alcohol Level"] = df["Driver Alcohol Level"]  
df["Pedestrians Involved"] = df["Pedestrians Involved"].round(0)  # Rounding to 0 decimals

# Check again if there is any missing value left after imputation
print("After handling missing values")

# Ensure no missing values remain
print(df.isnull().sum())  

# Save cleaned dataset
# Saves without index
df.to_csv("cleaned_road_accident_dataset.csv", index=False)  
#df.head()

#Task-3 (Data Summarization & Descriptive Analysis)
# Compute central tendency (Mean, Median, Mode)

# Select numerical columns
num_columns = df.select_dtypes(include=[np.number])

# Compute Mean
mean = num_columns.mean()

# Compute Median
median = num_columns.median()

# Compute Mode (returns multiple values, so we take the first)
mode = num_columns.mode().iloc[0]

# Display results
print("Mean Values:\n", mean)
print("\nMedian Values:\n", median)
print("\nMode Values:\n", mode)

# Measures of Variation ( Range, Variance, Standard Deviation)

# Compute Range (Max - Min)
# Range is difference between maximum and minimum values in dataset
range = num_columns.max() - num_columns.min()

# Compute Variance
variance = num_columns.var()

# Compute Standard Deviation
standard_deviation = num_columns.std()

# Display results
print("\nRange:\n", range)
print("\nVariance:\n", variance)
print("\nStandard Deviation:\n", standard_deviation)

# Cross-tabulation
# Cross tabulation is a method used to analyze the relationship between two or more categorical variables

# Perform cross-tabulation: Example (Accident Severity vs. Weather Conditions)
cross_tab = pd.crosstab(df["Accident Severity"], df["Weather Conditions"])

# Display the cross-tabulation table
print("Cross-tabulation results")
print(cross_tab)

# Save the cross-tabulation to a CSV file
cross_tab.to_csv("road_accident_crosstab.csv")

# Frequency distribution is a representation that displays how often any specific values occur in dataset
# Select categorical columns ( Can also be calculated based on numerical values)
categorical_cols = df.select_dtypes(include=['object'])

# Compute and display frequency distribution for each categorical column
for col in categorical_cols.columns:
    print(f"\nFrequency Distribution for {col}:\n")
    print(df[col].value_counts())

# # Choose the column you want to analyze for outliers
# column_name = 'Speed Limit'  # Replace with your actual column name

# # Calculate Q1 and Q3
# Q1 = df[column_name].quantile(0.25)
# Q3 = df[column_name].quantile(0.75)
# IQR = Q3 - Q1

# # Calculate bounds
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR

# # Filter outliers
# outliers = df[(df[column_name] < lower_bound) | (df[column_name] > upper_bound)]

# print("Outliers in column:", column_name)
# print(outliers)
