import numpy as np
import matplotlib.pyplot as plt

n = 200
h = 0.1
k = 0.01
L = 20.0

def initialCondition0():
    u = []
    i = 0
    while i <= n:
        u.append(0)
        i = i + 1
    
    return u

def initialConditionExp():
    u = []
    i = 0
    while i <= n:
        u.append(0)
        i = i + 1
    u[0] = np.exp(0.01) 
    return u

def resultsEulerMethod(u):
    v = []
    i = 0

    while i <= n:
        v.append(0)
        i = i + 1
        
    j = 0
    while j <= 1000:
        j = j + 1
        v[0] = np.sin(k*j)
        v[n] = 0
        i = 1
        while i <= n - 1:
            v[i] = u[i] - k/(2*h)*(u[i+1]-u[i-1])
            i = i + 1
        x = 0
        while x <= n:
            u[x] = v[x]
            x = x + 1
    
    return u

def resultsModificatedEulerMethod(u):
    v = []
    i = 0
    while i <= n:
        v.append(0)
        i = i + 1

    j = 0
    while j <= 1000:
        v[0] = np.sin(k*(j-1.0/2.0))
        v[n] = 0
        i = 1
        while i <= n - 1:
            v[i] = u[i] - k/(4*h)*(u[i+1]-u[i-1])
            i = i + 1
        u[0] = np.sin(k*j)
        u[200] = 0
        x = 1

        while x <= n - 1:
            u[x] = u[x] - k/(2*h)*(v[x+1]-v[x-1])
            x = x + 1
        j = j + 1
    return u

def plot(results, resultsExponent):  # wyswietlanie wykresow
    # x = np.linspace(0, 202, n, endpoint=True)
    plt.subplot(1,2,2)
    plt.plot(resultsExponent, color='g', lw = 1, ls='-.')
    plt.title('War. pocz. Exp')
    plt.legend(["Funkcja"])
    plt.grid()
    plt.subplot(1,2,1)
    plt.tight_layout()
    plt.plot(results, color='g', lw=1, ls='-.')
    plt.grid()
    plt.title('War. pocz. 0')
    plt.legend(["Funkcja"])
    plt.show()

def eulerMethod():
    initCond0 = initialCondition0()
    initCondExp = initialConditionExp()
    print('Metoda Eulera')
    
    resEuler = resultsEulerMethod(initCond0)
    resEulerExp = resultsEulerMethod(initCondExp)
    
    plot(resEuler, resEulerExp)

def modEuluerMethod():
    initCond0 = initialCondition0()
    initCondExp = initialConditionExp()

    print('Zmodyfikowana Metoda Eulera')
    resModEuler = resultsModificatedEulerMethod(initCond0)
    resModEulerExp = resultsModificatedEulerMethod(initCondExp)
    plot(resModEuler, resModEulerExp)
    
def main():
    print("k = ", k)
    eulerMethod()
    modEuluerMethod()
    
if __name__ == "__main__":
    main()
