import numpy as np
import matplotlib.pyplot as plt

tolerance = 0.0001
D = 0.00001
h = 0.1
deltaT = h ** 2 / (2 * D)
T1 = 39
T2 = 178

def equation(t):
    nmax = 10000
    u = np.zeros(11)
    x = np.linspace(0, 1, 11)
    for n in range(1, nmax + 1):
        if n % 2 == 0:
            u = u + 1/n * np.exp(- n**2 * np.pi**2 * D * t) * np.sin(n * np.pi * x)
        else:
            u = u - 1/n * np.exp(- n**2 * np.pi**2 * D * t) * np.sin(n * np.pi * x)

    u = u * 2 * (T2 - T1) / np.pi
    u += (T2 - T1) * x + T1

    return u

def plot3d(X, Y, numericalData, analyticalData):
    ax = plt.axes(projection='3d')
    ax.scatter(X, Y, numericalData)
    ax.scatter(X, Y, analyticalData)
    plt.show()

def plotRelativeError(analyticalData, numericalData):
    relativeError = []
    for j in range(T1):
        relativeErrorSum = 0
        for i in range(11):
            relativeErrorSum += abs((analyticalData[j, i] - numericalData[j][i]) / analyticalData[j][i])
        relativeErrorSum /= 11
        relativeError.append(np.log10(relativeErrorSum))

    plt.plot(list(j * deltaT for j in range(j + 1)), relativeError)
    plt.show()

def saveDataToFile(numericalData, analyticalData):
    np.savetxt('numericalData', numericalData, fmt='%10.5f', delimiter='\t')
    np.savetxt('analyticalData', analyticalData, fmt='%10.5f', delimiter='\t')

def numericalMethod():
    numericalData = [[T1 for i in range(10)] + [T2]]
    j = 0
    error = 1
    while (error > tolerance):
        temp = [T1]
        for i in range(1, 10):
            temp.append((numericalData[j][i + 1] + numericalData[j][i - 1]) / 2)

        temp.append(T2)
        numericalData.append(temp)
        j += 1
        error = 0
        for i in range(11):
            error += abs((numericalData[j][i] - numericalData[j - 1][i]) / numericalData[j][i])
        error /= 11

    return numericalData, j

def analyticalMethod(j):
    X, Y = np.meshgrid(list(x * h for x in range(11)), list(t * deltaT for t in range(j + 1)))
    analyticalData = np.zeros((11, j + 1))
    for i in range(j + 1):
        analyticalData[:, i] = equation(i * deltaT)
    analyticalData = np.transpose(analyticalData)

    return X, Y, analyticalData


def main():
    numericalData, j = numericalMethod()
    X, Y, analyticalData = analyticalMethod(j)
    plot3d(X, Y, numericalData, analyticalData)
    plotRelativeError(analyticalData, numericalData)
    saveDataToFile(numericalData, analyticalData)

if __name__ == '__main__':
    main()
