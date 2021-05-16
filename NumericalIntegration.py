import math

def f(x):
    return math.sin(x)


def fp(x):
    return math.cos(x)


def fppp(x):
    return -1.0 * math.cos(x)


def TrapezoidMethod():
    N = 4
    while N <= 1024:
        h = math.pi / (1.0 * N)
        x = 0.0
        I = 0.0
        for i in range(N):
            if (i == 0) or (i == N):
                I = I + f(x) / 2.0
            else:
                I = I + f(x)
            x = x + h
        I = I * h
        print('Integral ( Trapezoid, N= {}) = {:.13f}'.format(N, I))
        N *= 2


def SimpsonMethod():
    N = 4
    while N <= 1024:
        h = math.pi / (1.0 * N)
        x = 0.0
        I = 0.0
        for i in range(N):
            if (i == 0) or (i == N):
                I = I + f(x)
            elif i % 2 == 0:
                I = I + 2.0 * f(x)
            else:
                I = I + 4.0 * f(x)
            x = x + h
        I = I * h / 3.0
        print('Integral ( Simpson, N= {}) = {:.13f}'.format(N, I))
        N *= 2


def BooleMethod():
    N = 4
    while N <= 1024:
        h = math.pi / (1.0 * N)
        x = 0.0
        I = 0.0
        for i in range(N):
            if (i == 0) or (i == N):
                I = I + 7.0 * f(x)
            elif i % 2 != 0:
                I = I + 32.0 * f(x)
            elif i % 4 == 0:
                I = I + 14.0 * f(x)
            else:
                I = I + 12.0 * f(x)
            x = x + h
        I = I * (2.0 * h / 45.0)
        print('Integral (Boole, N = {}) = {:.13f}'.format(N, I))
        N *= 2


def EulerMaclaurinMethod():
    N = 4
    xN = math.pi
    x0 = 0.0
    while N <= 1024:
        h = math.pi / (1.0 * N)
        x = 0.0
        I = 0.0
        for i in range(N):
            if (i == 0) or (i == N):
                I = I + f(x) / 2.0
            else:
                I = I + f(x)
            x = x + h
        I = I * h
        I = I + (h * h / 12.0) * (fp(x0) - fp(xN)) - (h * h * h * h / 720.0) * (fppp(x0) - fppp(xN))
        print('Integral (EulerMaclaurin, N = {}) = {:.13f}'.format(N, I))
        N *= 2

def main():
    print('--------- Menu ---------')
    print('Menu: (1) Trapezoid rule')
    print('Menu: (2) Simpson rule')
    print('Menu: (3) Boole rule')
    print('Menu: (4) EulerMaclaurin rule')
    print('Menu: (5) Exit')
    choice = int(input('Your choice: '))
    while choice != 5:
        if choice == 1:
            TrapezoidMethod()
        elif choice == 2:
            SimpsonMethod()
        elif choice == 3:
            BooleMethod()
        elif choice == 4:
            EulerMaclaurinMethod()
        else:
            print('Wrong choice')
        choice = int(input('Your choice'))


if __name__ == '__main__':
    main()
