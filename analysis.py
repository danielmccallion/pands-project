# Daniel Mc Callion
# Read the Fisher's Iris data set
# Write a summary of each variable to a single text file
# Create histogram of each variable
# Output scatter plot of each pair of variables
# Outputs a pairplot to allow easily viewing each pair of variable at once

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Function to create a histogram of each variable
def create_histograms_old(df):
    for data_variable in data_variables:
        plt.hist(df[data_variable])
        plt.savefig(f"{data_variable}.png")
        plt.clf()


# Function to create a histogram of each variable
def create_histograms(df):
    for data_variable in data_variables:

        # Colours for each class of Iris with transparancy at half so each can be seen on one graph
        colours_for_hist = ((1, 0, 0, 0.5), (0, 1, 0, 0.5), (0, 0, 1, 0.5))
        # To keep track of which colour to use
        colour_counter = 0        

        # Plot each dataframe for each type of Iris Flower
        for class_df in iris_dataframes_dict:

            # Get dataframe for each type of Iris Flower
            df_to_plot = iris_dataframes_dict[class_df][data_variable]

            # Plot a histogram of data applying a semi-transparent colour and labeling the data
            # the same name as the Iris class it belongs to
            plt.hist(df_to_plot, fc=colours_for_hist[colour_counter], label=class_df)

            # Increase the counter to change the next colour
            colour_counter += 1
        
        # Create a legend to the top right outside the graph, with a shadow and title the
        # legend "Class"
        plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", shadow=True, title="Class")

        # Get the title and labels for the Histogram from the dictionary tied to the
        # variable name
        plot_title = data_variables_labels[data_variable]["title"]
        plot_label = data_variables_labels[data_variable]["label"]

        # Add a title to the Histogram and increase the font size to 18
        plt.suptitle(plot_title, fontsize=18)
        # Add a label to the x-axis and increase the font size to 12
        plt.xlabel(plot_label, fontsize=12)
        # Save the Histogram as a png file with the legend correctly drawn and minimal extra
        # white around sides
        plt.savefig(f"{plot_title}.png", bbox_inches="tight")
        # Clear the canvas
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


# Seperate each dataframe by a value and save each new dataframe to a dict
def seperate_dataframes_by_value(df, value="class"):
    # Iterate each unique value in a dataframes column
    for dataset_class in df[value].unique():
        class_df=df[df[value]==dataset_class]
        iris_dataframes_dict[dataset_class] = class_df
             

# Dictionary to hold each seperate class in their own dataframe  
iris_dataframes_dict = {}

# Name of each variable in the dataset
data_variables = ("sepal_length", "sepal_width", "petal_length", "petal_width")

# Dictionary to give each variable a useable title and label for the graphs
data_variables_labels = {
    "sepal_length": {
        "label": "Sepal length in cm",
        "title": "Sepal Length"
        },
    "sepal_width": {
        "label": "Sepal width in cm",
        "title": "Sepal Width"
        },
    "petal_length": {
        "label": "Petal length in cm",
        "title": "Petal Length"
        },
    "petal_width": {
        "label": "Petal width in cm",
        "title": "Petal Width"
        }
}

# File to output variable summaries to
summary_file = "variable_summary.txt"

# Csv file that contains the Iris dataset
iris_csv_file = "iris.csv"

# Read data from csv to pandas dataframe
iris_df = open_csv_to_dataframe(iris_csv_file)

# If iris datafile found and contains data perform analysis
if not iris_df.empty:
    
    # Save a datframe for each class of Iris to a dictionary
    seperate_dataframes_by_value(iris_df)

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
