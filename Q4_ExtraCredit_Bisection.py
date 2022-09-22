import math

def f(x):
    return x**2+x-10

tol = 0.000001
def bisection(x1, x2, tol, f, flag):

    if f(x1) * f(x2) > 0.0:
        print("invalid brackets")

    iter = 0; error = 100

    while error >= tol:
        x3 = (x1 + x2) / 2
        iter += 1

        if f(x3) == 0:
            break
        elif f(x1) * f(x3) < 0:
            x2 = x3
            x4 = x1
        else:
            x1 = x3
            x4 = x2

        if flag == 1:
            error = abs(x4 - x3)
        elif flag == 2:
            error = abs((x4 - x3) / x3)
        elif flag == 3:
            error = abs(f(x3))

    print('Root is : %f' % x3)
    print('Iteration: %f' % iter )
    print('Error: ', error)

# Brackets
x1 = -4; x2 = 0
y1 = 1; y2 = 4

"""print('Approximate Error iteration prediction: ')
pred_1 = float(math.log2(abs(x1 - x2) / tol))
print('1st brackets iteration prediction: %f' % pred_1)
pred_2 = float(math.log2(abs(y1 - y2) / tol))
print('2nd brackets iteration prediction: %f' % pred_2)"""

print('\nAbsolute Approximate Error: ')
bisection(x1, x2, tol, f, 1)
bisection(y1, y2, tol, f, 1)
print('\n')

print('Absolute Relative Approximate Error: ')
bisection(x1, x2, tol, f, 2)
bisection(y1, y2, tol, f, 2)
print('\n')

print('True Absolute Error:')
bisection(x1, x2, tol, f, 3)
bisection(y1, y2, tol, f, 3)
print('\n')