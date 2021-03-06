% Implementation of modified Newton-Raphson method
% NOTE: this function will only work for functions of single variable

function raphson()

	syms x;
	f=7*(x^2)-x^3;  		% define your function here
	xold=10;
	maxiter=10;
	epsilon=1e-5;
	k=0;
	alpha1=0.1;

	df=diff(f);
	df2=diff(f,2);
	grad1=subs(df,xold);
	grad2=subs(df2,xold);
	f_x=subs(f,xold);
	xnew=xold-alpha1*(grad1/grad2);
	figure(1);
	plot(xold,f_x,'o');
	xlabel('x value');
	ylabel('f(x)');
	title('convergence');

	hold on;

	%for i=1:20,
	while((abs(xnew-xold)>epsilon)),
		xold=xnew;
		grad1=subs(df,xold);
		grad2=subs(df2,xold);
		f_x=subs(f,xold);
		xnew=xold-alpha1*(grad1/grad2);
		plot(xold,f_x,'o');
		k=k+1;
		if(k>=maxiter),
			break;
		end;	
	end;
	
	f_x=subs(f,xnew);
	plot(xnew,f_x,'ro');
	hold off;
	fprintf('optimal value:%0.3f\n',double(xnew));
	fprintf('min value attained for optimal x:%0.3f\n',double(f_x));
	fprintf('alpha value :%0.2f\n',alpha1);

end

