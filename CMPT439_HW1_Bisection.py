import math

def func(x):
    return ((2*math.sin(x)-math.exp(x))/4)-1

tol = 0.000001
def bisection(x1, x2, tol, error_type):

    if func(x1) * func(x2) > 0.0:
        print("invalid brackets")

    iter = 0; error = 100

    while error >= tol:
        x3 = (x1 + x2) / 2
        iter += 1

        if func(x3) == 0:
            break
        elif func(x1) * func(x3) < 0:
            x2 = x3
            x4 = x1
        else:
            x1 = x3
            x4 = x2

        if error_type == 1:
            error = abs(x4 - x3)
        elif error_type == 2:
            error = abs((x4 - x3) / x3)
        elif error_type == 3:
            error = abs(func(x3))

    print('Root is : %f' % x3)
    print('Iteration: %f' % iter )
    print('Error: ', error)

#Itervals for question 2
x1 = -7; x2 = -5
y1 = -5; y2 = -3

print('Approximate Error iteration prediction: ')
pred_1 = float(math.log2(abs(x1 - x2) / tol))
print('1st brackets iteration prediction: %f' % pred_1)
pred_2 = float(math.log2(abs(y1 - y2) / tol))
print('2nd brackets iteration prediction: %f' % pred_2)

print('\nAbsolute Approximate Error: ')
bisection(x1, x2, tol, 1)
bisection(y1, y2, tol, 1)
print('\n')

print('Absolute Relative Approximate Error: ')
bisection(x1, x2, tol, 2)
bisection(y1, y2, tol, 2)
print('\n')

print('True Absolute Error:')
bisection(x1, x2, tol, 3)
bisection(y1, y2, tol, 3)
print('\n')