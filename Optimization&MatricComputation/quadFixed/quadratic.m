%Steepest descent for quadratic
%with fixed alplha


function  quadratic(A,b,c)

	%syms x;syms y;syms z;
	%vec=[x y z];
	clc;
	xold=[.1;.1];
	epsilon=1e-5;
	maxiter=100;
	k=1;
	alpha1=0.003;

	grad=A*xold-b;
	xnew=xold-alpha1*grad;
	f_x=0.5*(xold'*A*xold)-xold'*b+c;
	figure(1);
	plot(xold(1),f_x,'o');
	xlabel('x value');
	ylabel('f(x)');
	title('convergence');

	hold on;

	while((norm(xold-xnew)>epsilon) && (k<maxiter)),	
		xold=xnew;
		grad=A*xold-b;
		%alpha1=(grad'*grad)/(grad'*A*grad);
		xnew=xold-alpha1*grad;
		f_x=0.5*(xold'*A*xold)-xold'*b+c;
		plot(xold(1),f_x,'o');
		k=k+1;
	end;	

	hold off;

	xold=xnew;
	f_x=0.5*(xold'*A*xold)-xold'*b+c;
	fprintf('optimal value:');
	xnew
	fprintf('\nmin value attained for optimal x:%0.3f\n',f_x);
	fprintf('alplha value:%f\n',alpha1);
	
end

