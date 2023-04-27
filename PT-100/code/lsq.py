import numpy as np
import matplotlib.pyplot as plt

# Training the Model - Model Training
Train_data = np.loadtxt('PT-100/code/training_data.txt')
n1, m1 = Train_data.shape
T = Train_data[:,0]
X = np.vstack((np.ones((1,n1)),T))
Y = Train_data[:,[1]]

# Least Squares Method - Model Training
n = np.linalg.lstsq(X.T, Y, rcond=None)[0]
print(n)

plt.plot(T, X.T @n, label= 'Fitted line')
plt.scatter(T, Y, label='Original data', color = 'red')
plt.grid()
plt.ylabel("Voltage (in Volts)")
plt.xlabel("Temperature (in $^{\circ}$C)")
plt.legend()
plt.savefig('train.png')
plt.close()

# Testing the Model - Model Evaluation
Test_data = np.loadtxt('PT-100/code/validation_data.txt')
n2, m2 = Test_data.shape
T_test = Test_data[:,0]
X_test = np.vstack((np.ones((1,n2)),T_test))
Y_test = Test_data[:,[1]]

plt.plot(T_test, X_test.T @n, label= 'Fitted line')
plt.scatter(T_test, Y_test, label='Original data', color = 'red')
plt.ylabel("Voltage (in Volts)")
plt.xlabel("Temperature (in $^{\circ}$C)")
plt.legend()
plt.grid()
plt.savefig("test.png")