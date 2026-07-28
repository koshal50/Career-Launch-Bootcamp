
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data (X = study hours, y = exam scores)
X = np.array([[1], [2], [3], [4], [5]])   # independent variable
y = np.array([1, 3, 2, 3, 5])             # dependent variable

# Create Linear Regression model
model = LinearRegression()

# Train (fit) the model
model.fit(X, y)

# Predict values
y_pred = model.predict(X)

# Print slope (coefficient) and intercept
print("Slope (Coefficient):", model.coef_)
print("Intercept:", model.intercept_)

# Plot the results
plt.scatter(X, y, color="red", label="Actual Data")
plt.plot(X, y_pred, color="blue", label="Regression Line")
plt.xlabel("X - Study Hours")
plt.ylabel("y - Exam Score")
plt.legend()
plt.show()






# OUTPUT 

# Slope (Coefficient): [0.8]
# Intercept: 0.39999999999999947
