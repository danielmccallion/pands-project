# Daniel Mc Callion
# Read the Fisher's Iris data set
# Write a summary of each variable to a single text file
# Create histogram of each variable
# Output scatter plot of each pair of variables

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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
        

# Function to output a scatter plot for each set of variables
def scatter_plot_pair(df):
    for data_variable in data_variables:
        for data_variable2 in data_variables:
            if data_variable2 == data_variable:
                continue
            plt.clf()
            plt.plot(df[data_variable], df[data_variable2], "b.")
            scatter_plot_title = f"{data_variable} vs {data_variable2}"
            plt.title(scatter_plot_title)
            plt.savefig(f"{scatter_plot_title}.png")


# Function to output a scatter plot for each set of variables using the seaborn library
def scatter_plot_pair_seaborn(df):
    for data_variable in data_variables:
        for data_variable2 in data_variables:
            if data_variable2 == data_variable:
                continue
            plot = sns.scatterplot(x=data_variable, y=data_variable2, hue="class", style="class",
            data=df)
            scatter_plot_title = f"{data_variable} vs {data_variable2}"
            plot.set_title(scatter_plot_title)
            plot.get_figure().savefig(f"{scatter_plot_title}.png")
            plot.get_figure().clf() 


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

# Output scatter plot each set of variables
scatter_plot_pair_seaborn(iris_df)
#scatter_plot_pair(iris_df)
