def GaussianElimantion(a,b,c,r):
    Beta = []
    Rho = []
    x = []
    Beta.append(b[0])
    Rho.append(r[0])

    for i in range(1, 5):
        Beta.append(b[i] - (a[i] / Beta[i - 1]) * c[i - 1])
        Rho.append(r[i] - (a[i] / Beta[i - 1]) * Rho[i - 1])

    # initialize x
    for i in range(5):
        x.append(0)

    x[4] = Rho[4] / Beta[4]
    for i in range(1, 5):
        x[4 - i] = (Rho[4 - i] - c[4 - i] * x[4 - i + 1]) / Beta[4 - i]

    # write solution
    for i in range(5):
        print('x{} = {}'.format(i + 1, x[i]))

    # check solution
    r1 = b[0] * x[0] + c[0] * x[1]
    r2 = a[1] * x[0] + b[1] * x[1] + c[1] * x[2]
    r3 = a[2] * x[1] + b[2] * x[2] + c[2] * x[3]
    r4 = a[3] * x[2] + b[3] * x[3] + c[3] * x[4]
    r5 = a[4] * x[3] + b[4] * x[4]
    return r1,r2,r3,r4,r5
    
def main():
    a = [0.0, -1.0, -1.0, -1.0, -1.0]
    b = [2.0, 2.0, 2.0, 2.0, 2.0]
    c = [-1.0, -1.0, -1.0, -1.0, 0.0]
    r = [0.0, 1.0, 2.0, 3.0, 4.0]

    r1, r2, r3, r4, r5 = GaussianElimantion(a,b,c,r)
    print('Check solution ( values of r ): ')
    print('r1 = {}'.format(r1))
    print('r2 = {}'.format(r2))
    print('r3 = {}'.format(r3))
    print('r4 = {}'.format(r4))
    print('r5 = {}'.format(r5))

if __name__ == '__main__':
    main()