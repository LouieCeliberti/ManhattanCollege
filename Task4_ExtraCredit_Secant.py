import math

def f(x):
    return x**2+x-10

tol = 0.000001
def Secant(x1, x2, tol, f, flag):

    if abs(f(x1)) > abs(f(x2)):
        xswap = x1
        x1 = x2
        x2 = xswap
 
    iter = 0; error = 100

    while error >= tol:
        x3 = x2-f(x2)*((x1-x2)/(f(x1)-f(x2)))
        iter += 1

        if f(x1) == 0 and f(x3) == 0:
            print('The root is: ', x3)
            print('Iterations: ', iter)
            break
        else:
            x1 = x2
            x2 = x3
        
        if flag == 1:
            error = abs(x1 - x2)
        elif flag == 2:
            error = abs((x1 - x2) / x2)
        elif flag == 3:
            error = abs(f(x2))

    print('Root is : %f' % x3)
    print('Iteration: %f' % iter )
    print('Error: ', error)

# Brackets
x1 = -4; x2 = -1


print('\nAbsolute Approximate Error: ')
Secant(x1, x2, tol, f, 1)
print('\n')

print('\nAbsolute Relative Approximate Error: ')
Secant(x1, x2, tol, f, 2)
print('\n')

print('True Absolute Error:')
Secant(x1, x2, tol, f, 3)
print('\n')
