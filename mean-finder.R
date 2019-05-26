setwd("~/Desktop/Programming/PythonProjects/apt-data-crawler")
Boston = read.csv("data.csv", header=T)
Boston$X = NULL

Boston$Price = as.numeric(Boston$Price)
output = aggregate(Boston$Price, list(Boston$Neighborhood), mean)
