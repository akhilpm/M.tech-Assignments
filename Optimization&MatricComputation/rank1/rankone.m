%rank one algorithm
% i/p xold = initial value for X

function  rankone(A,b,c,xold)

	%syms x;syms y;syms z;
	%vec=[x y z];
	clc;
	%xold=[2,4]';
	%epsilon=1e-5;

	n=size(A,1);
	Hold=eye(n);

	grad=A*xold-b;
	%% if g0==0 stop
	if(norm(grad)==0),
		disp('solution is');
		disp(xold);
		return;
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

	for ii=2:n,	
		xold=xnew;
		gradnew=A*xold-b;

		if(norm(gradnew)==0),
			disp('solution is');
			disp(xold);
			break;
		end;

		gradDiff=gradnew-grad;
		xDiff=alpha1*dold;
		tempDiff=xDiff-Hold*gradDiff;

		Hnew=Hold+(tempDiff*tempDiff')/(gradDiff'*tempDiff);
		dold=-(Hnew*gradnew);
		alpha1=-(gradnew'*dold)/(dold'*A*dold);
		xnew=xold+alpha1*dold;
		grad=gradnew;
		Hold=Hnew;
		f_x=0.5*(xold'*A*xold)-xold'*b+c;
		plot(norm(xold),f_x,'o');
	end;	

	hold off;
	%disp(k);
	xold=xnew;
	f_x=0.5*(xold'*A*xold)-xold'*b+c;
	fprintf('optimal value:\n');
	disp(xnew);
	fprintf('\nmin value attained for optimal x is :%0.3f\n',f_x);
	fprintf('alplha value:%f\n',alpha1);
end

