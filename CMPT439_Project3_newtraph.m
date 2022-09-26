function [root,iter] = newtraph(x0,f,tol,flag)

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
