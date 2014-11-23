%Conjugate gradient algorithm


function  conjGrad(A,b,c)

	%syms x;syms y;syms z;
	%vec=[x y z];
	clc;
	xold=[2,4]';
	epsilon=1e-5;
	maxiter=10;
	k=1;

	grad=A*xold-b;
	%% if g0==0 stop
	if(norm(grad)==0),
		disp('solution is');
		disp(xold);
		quit;
	end;
		
	dold=-grad;
	alpha1=-(grad'*dold)/(dold'*A*dold);
	xnew=xold+alpha1*dold;
	f_x=0.5*(xold'*A*xold)-xold'*b+c;
	figure(1);
	plot(norm(xold),f_x,'ro');
	xlabel('x value');
	ylabel('f(x)');
	title('convergence');

	hold on;

	while((norm(xold-xnew)>epsilon) && (k<maxiter)),	
		xold=xnew;
		grad=A*xold-b;

		if(norm(grad)==0),
			disp('solution is');
			disp(xold);
			quit;
		end;

		beta1=(grad'*A*dold)/(dold'*A*dold);
		alpha1=-(grad'*dold)/(dold'*A*dold);
		dold=-grad+beta1*dold;
		xnew=xold+alpha1*dold;
		f_x=0.5*(xold'*A*xold)-xold'*b+c;
		plot(norm(xold),f_x,'o');
		k=k+1;
	end;	

	hold off;
	%disp(k);
	xold=xnew;
	f_x=0.5*(xold'*A*xold)-xold'*b+c;
	fprintf('optimal value:\n');
	disp(xnew);
	fprintf('\nmin value attained for optimal x is :%0.3f\n',f_x);
	fprintf('alplha value:%f\n',alpha1);
	fprintf('beta value:%f\n',beta1);
end

