import math

# Newton-Raphson method

def f(x):
    return (math.cos(x) - x)
#   return ((6432.0 * (x**8) - 12012.0 * (x**6) + 6930.0 * (x**4) - 1260.0 * (x**2) + 35.0) / 128.0)
#   return (x**3 - 169.0)

def f_p(x):
    return (-1.0*math.sin(x) - 1)
#   return ((8.0*6435.0 * (x**7) - 6.0*12012.0 * (x**5) + 4.0 * 6930.0 * (x**3) - 2.0 * 1260.0 * x) / 128.0)
#   return (3.0 * (x**2))

# Newton-Raphson
def newtonRahpsonMethod(xOld, tolerance):
    xNew = xOld - (f(xOld) / f_p(xOld))
    error = math.fabs((xNew - xOld) / xNew)
    numberOfIterations = 1
    while error > tolerance:
        xOld = xNew
        xNew = xOld - (f(xOld) / f_p(xOld))
        error = math.fabs((xNew - xOld) / xNew)
        print('number of iteration = {:.8f}, x0 = {:.8f}'.format(numberOfIterations,xOld))
        numberOfIterations += 1

    print('Root found at {:.8f}'.format(xNew))
    print("After the {} iterations.".format(numberOfIterations))

def main():
    xOld = float(input('Enter x0: '))
    tolerance = float(input('Enter tolerance: '))
    newtonRahpsonMethod(xOld, tolerance)

if __name__ == '__main__':
    main()