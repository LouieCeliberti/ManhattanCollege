import math

def f(x):
    return 2*math.sin(x)-(math.exp(x)/4)-1

tol = 0.000001
def FalsePosition(x1, x2, tol, f, flag):

    if f(x1)*f(x2)>0:
        print('Invalid Brackets')
 
    iter = 0; error = 100

    while error >= tol:
        x = x2
        x3 = x2-f(x2)*((x1-x2)/(f(x1)-f(x2)))
        iter += 1

        if f(x3) == 0:
            print('The root is: ', x3)
            print('Iterations: ', iter)
            break
        elif f(x1)*f(x3)<0:
            x2 = x3
        else:
            x1 = x3

        if flag == 1:
            error = abs(x - x3)
        elif flag == 2:
            error = abs((x - x3) / x3)
        elif flag == 3:
            error = abs(f(x3))

    print('Root is : %f' % x3)
    print('Iteration: %f' % iter )
    print('Error: ', error)

#Itervals for question 2
x1 = -7; x2 = -5
y1 = -5; y2 = -3

print('\nAbsolute Approximate Error: ')
FalsePosition(x1, x2, tol, f, 1)
FalsePosition(y1, y2, tol, f, 1)
print('\n')

print('Absolute Relative Approximate Error: ')
FalsePosition(x1, x2, tol, f, 2)
FalsePosition(y1, y2, tol, f, 2)
print('\n')

print('True Absolute Error:')
FalsePosition(x1, x2, tol, f, 3)
FalsePosition(y1, y2, tol, f, 3)
print('\n')
