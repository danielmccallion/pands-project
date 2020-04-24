# Daniel Mc Callion
# Read the Fisher's Iris data set
# Write a summary of each variable to a single text file
# Create histogram of each variable

import pandas as pd
import matplotlib.pyplot as plt


# Function to create a histogram of each variable
def create_histograms(df):
    for data_variable in data_variables:
        plt.hist(df[data_variable])
        plt.savefig(f"{data_variable}.png")
        plt.clf()


# Function to write a summary of each variable to a single text file
def write_summary(file_to_write, df):
    with open(file_to_write, "wt") as f:
        # Write summary of data frame to file
        f.write(str(df.describe()))
        

# Name of each variable in the dataset
data_variables = ("sepal_length", "sepal_width", "petal_length", "petal_width")

# File to output variable summaries to
summary_file = "variable_summary.txt"

# Read data from csv to pandas dataframe
iris_df = pd.read_csv("iris.csv")

# Create summary file on each variable
write_summary(summary_file, iris_df)

# Create histogram for each variable
create_histograms(iris_df)
