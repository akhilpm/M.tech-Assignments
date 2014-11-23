% Implementation of Steepest Descent method
% NOTE: this function will only work for functions of single variable


function gradient()

	syms x;
	f=x^2;  		% define your function here
	xold=5;
	maxiter=50;
	alpha1=0.1;
	epsilon=1e-5;
	k=0;

	df=diff(f);
	grad=subs(df,'x', xold);
	f_x=subs(f,xold);
	xnew=xold-alpha1*grad;
	figure(1);
	plot(xold,f_x,'o');
	xlabel('x value');
	ylabel('f(x)');
	title('convergence');

	hold on;

	while((abs(xnew-xold)>epsilon) && (k<maxiter)),
		xold=xnew;
		grad=subs(df,xold);
		f_x=subs(f,xold);
		xnew=xold-alpha1*grad;
		plot(xold,f_x,'o');
		k=k+1;
	end;
	
	hold off;
	f_x=subs(f,xnew);
	xnew=subs(xnew,xnew);
	fprintf('optimal value:%0.3f\n',double(xnew));
	fprintf('min value attained for optimal x:%0.3f\n',double(f_x));


end

