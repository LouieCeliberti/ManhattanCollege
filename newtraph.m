function [root,iter] = newtraph(x0,f,tol,flag)
% newtraph: Newton − Raphson root location zeroes
% [root,ea,iter] = newtraph(func,dfunc,xr,es,maxit,p1,p2,...):
% uses Newton − Raphson method to find the root of func
% input:
% func = name of function
% dfunc = name of derivative of function
% xr = initial guess
% es = desired relative error (default = 0.0001%)
% maxit = maximum allowable iterations (default = 50)
% p1,p2,... = additional parameters used by function
% output:
% root = real root
% ea = approximate relative error (%)
% iter = number of iterations
% if nargin<3,error('at least 3 input arguments required'),end
% if nargin<4||isempty(tol),tol=0.00001;end
% if nargin<5||isempty(maxit),maxit = 50;end


iter = 0; tol = 0.00001; error = 100;

if f(x0) == 0
    print('x0 is the root'+ x0);
    print('Iteration: ' + iter)
else
    iter = iter + 1;
end
if df(x0) == 0
    print('invalid bracket');
end


while error >= tol
 %x0 = x1;
 x1 = x0-f(x0)/finverse(f(x0));
 iter = iter + 1;

 if flag == 1
     error = abs(x1-x0) * 100;
 elseif flag == 2
     error = abs((x1-x0)/x1) * 100;
 elseif flag == 3
     error = abs(x1) * 100; 
 end


    print('Root is: '+ x1);
    print('Iteration: '+ iter);
    print('Error: '+ error);

end

newtraph(-6,2*sin(x)-(exp(x)-1/4),tol,1);
newtraph(-6,2*sin(x)-(exp(x)-1/4),tol,2);
newtraph(-6,2*sin(x)-(exp(x)-1/4),tol,3);