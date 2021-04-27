import math

def f(x):
    return math.cos(x) - x


def falsePositionMethod(tolerance):
    print('False position: ')
    xL = float(input('Enter xL: '))
    xR = float(input('Enter xR: '))

    xOld = xL  # Used to calculate first Error
    xNew = (xL * f(xR) - xR * f(xL)) / (f(xR) - f(xL))
    Error = math.fabs((xNew - xOld) / xNew)

    numberOfIterations = 0

    while Error > tolerance:
        xNew = (xL * f(xR) - xR * f(xL)) / (f(xR) - f(xL))
        print('i = {} xNew = {:.8f} xL = {} xR = {}'.format(numberOfIterations, xNew, xL, xR))
        if ((f(xL) * f(xNew)) < 0.0):
            xR = xNew
        else:
            xL = xNew
        Error = math.fabs((xNew - xOld) / xNew)
        xOld = xNew
        numberOfIterations += 1

    print('Root found at: {:.8f}'.format(xNew))
    print('Iterations: {}'.format(numberOfIterations))

def secantMethod(tolerance):
    print('Secant: ')
    xOlder = float(input("Enter x_i-1: "))
    xOld = float(input("Enter xi: "))

    numberOfIterations = 0
    xNew = (xOlder*f(xOld) - xOld*f(xOlder))/(f(xOld)-f(xOlder))
    Error = math.fabs((xNew-xOld)/xNew)

    while Error > tolerance:
        xNew = (xOlder * f(xOld) - xOld * f(xOlder)) / (f(xOld) - f(xOlder))
        Error = math.fabs((xNew - xOld) / xNew)
        print('i = {} xNew = {:.8f}'.format(numberOfIterations, xNew))
        xOlder = xOld
        xOld = xNew
        numberOfIterations += 1

    print('Root found at: {:.8f}'.format(xNew))
    print('Iterations: {}'.format(numberOfIterations))


def main():
    tolerance = 0.00000001
    falsePositionMethod(tolerance)
    secantMethod(tolerance)

if __name__ == '__main__':
    main()