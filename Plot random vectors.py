"""
Created on Tue Jun 25 18:15:42 2024
"""

## uVkBPnJFU3vvvKjg
import numpy as np
import matplotlib.pyplot as plt

###### Adding random vector to its transpose #####

shape =2

a= np.random.randint(0, 9, shape)

a_transpose = np.transpose(a)

a + a_transpose

########## Scatter Plot of unit vectors ############

n=10

x_list=np.zeros(shape=(n, 1))
y_list =np.zeros(shape=(n, 1))

for i in range(0,n):
    x= np.random.randint(-10, 10, shape)
    x= x/np.linalg.norm(x)
    
    print(x)
    
    x_list[i] = x[0]
    y_list[i] = x[1]

plt.figure()
plt.scatter(x_list,y_list, color='b', edgecolor='b', facecolor='none', label='Normalized vector x', s=10)

# plt.quiver(0, 0, x[0], x[1], angles='xy', scale_units='xy', scale=1, color='b', label='Normalized vector x')

plt.xlim(-5, 5) #plot size
plt.ylim(-5, 5)

plt.xlabel('X-axis') #axis label
plt.ylabel('Y-axis')
plt.legend()
# plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()


###### Sctter Plot of random vectors #######

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

########## Least squares #########
import cvxpy as cp

# Generate data
m = 2
n = 15
np.random.seed(1)
A = np.random.randn(m, n)
b = np.random.randn(m)

# Define and solve the CVXPY problem
x = cp.Variable(n)
cost = cp.sum_squares(A @ x - b) ## residual sum squared  - differrence between y and y predicted
prob = cp.Problem(cp.Minimize(cost))
prob.solve()

# Print result
print("\nThe optimal value is", prob.value)
print("The optimal x is")
print(x.value)

print("The norm of the residual is ", cp.norm(A @ x - b, p=2).value)


########## Least squares apply #########

import pandas as pd
import statsmodels.api as sm

#DataFrame making
data = {
    'Income': [1000, 1500, 2000, 2500, 3000],
    'Spending': [400, 600, 800, 1000, 1200]
}
df = pd.DataFrame(data)

# Add a constant term i.e. intercept to the independent variable X
X = sm.add_constant(df['Income'])  
y = df['Spending']  

# Fit the least squares regression model
model = sm.OLS(y, X).fit()

print(model.summary())

print("Estimated coefficients:")
print(f"Intercept: {model.params['const']}")
print(f"Income: {model.params['Income']}")










