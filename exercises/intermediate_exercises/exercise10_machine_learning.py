# Problem: Simple Machine Learning Model
# Question: Implement a basic linear regression model using scikit-learn.








from sklearn.linear_model import LinearRegression
import numpy as np

def linear_regression_example(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model.coef_, model.intercept_

# Example usage
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 3, 4, 5])
print(linear_regression_example(X, y))  # Output: (array([1.]), 1.0)
