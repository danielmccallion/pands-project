# Daniel Mc Callion
# Create histogram of each variable

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

plt.hist(df["sepal_length"])
plt.savefig("sepal_length.png")

plt.clf()
plt.hist(df["sepal_width"])
plt.savefig("sepal_width.png")

plt.clf()
plt.hist(df["petal_length"])
plt.savefig("petal_length.png")

plt.clf()
plt.hist(df["petal_width"])
plt.savefig("petal_width.png")
