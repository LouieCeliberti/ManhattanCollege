import math

def func(x):
    return ((2*math.sin(x)-math.exp(x))/4)-1

tol = 0.000001
def Secant(x0, x1, tol, error_type):

    if abs(func(x0)) > abs(func(x1)):
        xbuf = x0
        x0 = x1
        x1 = xbuf
 
    iter = 0; error = 100

    while error >= tol:
        x2 = x1-func(x1)*((x0-x1)/(func(x0)-func(x1)))
        iter += 1

        if func(x2) == 0:
            print('The root is: ', x2)
            print('Iterations: ', iter)
            break
        else:
            x0 = x1
            x1 = x2

        if error_type == 1:
            error = abs(x0 - x1)
        elif error_type == 2:
            error = abs((x0 - x1) / x1)
        elif error_type == 3:
            error = abs(func(x1))

    print('Root is : %f' % x2)
    print('Iteration: %f' % iter )
    print('Error: ', error)

#Itervals for question 2
x0 = -7; x1 = -5
y1 = -5; y2 = -3

print('\nAbsolute Approximate Error: ')
Secant(x0, x1, tol, 1)
Secant(y1, y2, tol, 1)
print('\n')

print('Absolute Relative Approximate Error: ')
Secant(x0, x1, tol, 2)
Secant(y1, y2, tol, 2)
print('\n')

print('True Absolute Error:')
Secant(x0, x1, tol, 3)
Secant(y1, y2, tol, 3)
print('\n')