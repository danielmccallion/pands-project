# Daniel Mc Callion
# Read the Fisher's Iris data set
# Write a summary of each variable to a single text file
# Create histogram of each variable
# Output scatter plot of each pair of variables
# Outputs a paiplot to allow easily viewing each pair of variable at once

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
def write_summary_old(file_to_write, df):
    with open(file_to_write, "wt") as f:
        # Write summary of data frame to file
        f.write(str(df.describe()))


# Function to write a summary of each variable to a single text file
def write_summary(file_to_write, df):
    with open(file_to_write, "wt") as f:
        # Write summary of data frame to file
        # Describing the data set, its size, shape and columns
        f.write("Summary of the Dataset\n\n")
        f.write(f"Size of the dataset: {df.size}\n\n")
        f.write(f"Shape of the dataset: {df.shape}\n\n")
        f.write(f"Columns of the dataset:\n{df.columns.values}\n\n")
        f.write(f"Samples per class of flower:\n{df['class'].value_counts()}\n\n")

        f.write("Statistics for the dataset:\n")
        f.write(str(df.describe()))

        # Get statistics for each class in the dataframe
        for dataset_class in df["class"].unique():
            class_df=df[df["class"]==dataset_class]
            f.write(f"\n\nStatistics for {dataset_class} class:\n")
            f.write(str(class_df.describe()))  


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


# Use seaborn to create a pair plot to plot each pair of variable and the univariate distribution on the diagonal axis
# all at once and very easily
def pair_plot_seaborn(df):
    plot = sns.pairplot(df, hue="class")
    plot.savefig(f"pairplot.png")


# Read data from csv to pandas dataframe
def open_csv_to_dataframe(file_to_open):        
    try:
        df = pd.read_csv(file_to_open)
        return df
    # If unable to open csv file, display message to state file not found
    except FileNotFoundError:
        print(f"File {file_to_open} does not exist.")


# Name of each variable in the dataset
data_variables = ("sepal_length", "sepal_width", "petal_length", "petal_width")

# File to output variable summaries to
summary_file = "variable_summary.txt"

# Csv file that contains the Iris dataset
iris_csv_file = "iris.csv"

# Read data from csv to pandas dataframe
iris_df = open_csv_to_dataframe(iris_csv_file)

# If iris datafile found and contains data perform analysis
if not iris_df.empty:
    # Create summary file on each variable
    write_summary(summary_file, iris_df)

    # Create histogram for each variable
    create_histograms(iris_df)

    # Output scatter plot each set of variables
    scatter_plot_pair_seaborn(iris_df)

    # Output pairplot to easliy view each pair of variables
    pair_plot_seaborn(iris_df)

# If unable to find iris datafile display message to state analysis not being performed
else:
    print("Unable to perform analysis without data.")
    
print("Script Complete!")
