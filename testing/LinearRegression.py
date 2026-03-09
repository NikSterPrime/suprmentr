import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Provide Data
# The input 'x' must be a 2D array (n_samples, n_features)
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# 2. Create and Fit the model
# The .fit() method calculates the optimal intercept and slope
model = LinearRegression().fit(x, y)

# 3. Get Results
r_sq = model.score(x, y)
print(f"Coefficient of determination (R-squared): {r_sq:.2f}")
print(f"Intercept (b0): {model.intercept_}")
print(f"Slope/Coefficient (b1): {model.coef_}")

# 4. Predict Response
y_pred = model.predict(x)
print(f"Predicted response for original x values:\\n{y_pred}")

# Predict for new data
x_new = np.array([10, 30, 60]).reshape((-1, 1))
y_new = model.predict(x_new)
print(f"Predicted response for new x values:\\n{y_new}")

# Optional: Plotting the results
plt.scatter(x, y, color='blue', label='Actual data points')
plt.plot(x, y_pred, color='red', linewidth=2, label='Regression line')
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.title('Linear Regression with scikit-learn')
plt.legend()
plt.show()

