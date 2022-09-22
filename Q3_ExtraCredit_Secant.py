import math

def f(x):
    return math.exp(math.cos(2*x)+math.sin(3*x))-3*math.cos(x)-2*math.sin(x)

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

        print('%0.6f \t %0.6f \t  %0.6f \t %d' % (x1, x2, x3, iter))

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

    """print('Root is : %f' % x3)
    print('Iteration: %f' % iter )
    print('Error: ', error)"""

# Brackets
w1 = -1; w2 = 0.2
x1 = 0.3; x2 = 1
y1 = 0.5; y2 = 1
z1 = 1.5; z2 = 3

print('\nAbsolute Approximate Error: ')
Secant(w1, w2, tol, f, 1)
Secant(x1, x2, tol, f, 1)
Secant(y1, z2, tol, f, 1)
Secant(z1, z2, tol, f, 1)
print('\n')

print('\nAbsolute Relative Approximate Error: ')
Secant(w1, w2, tol, f, 2)
Secant(x1, x2, tol, f, 2)
Secant(y1, z2, tol, f, 2)
Secant(z1, z2, tol, f, 2)
print('\n')

print('True Absolute Error:')
Secant(w1, w2, tol, f, 3)
Secant(x1, x2, tol, f, 3)
Secant(y1, z2, tol, f, 3)
Secant(z1, z2, tol, f, 3)
print('\n')