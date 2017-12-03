import time
print(time.gmtime())
start_time = time.clock()
# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt


# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv("iris.data", names=names)

#print(dataset)

# rows x columns(attributes)
print(dataset.shape)
print("=========================================================================")

# view data 
print(dataset.head(2))
print("=========================================================================")

# data description min max standard deviation mean
print(dataset.describe())
print("=========================================================================")

# class distributions count
print(dataset.groupby("class").size())
print("=========================================================================")

# data visualization with univariate plot

# box and whisker plots

# dataset.plot(kind = "box",
# 			subplots = "True",
# 			layout = (2,2),
# 			sharex = "False",
# 			sharey = "False")
# plt.show()

# generate the histograms for given data
# dataset.hist()
# plt.show()

# data visualization with multivariate plot 
# scatter plot matrix 
scatter_matrix(dataset)
plt.show()


end_time = time.clock()

print("Execution time :", end_time-start_time)


