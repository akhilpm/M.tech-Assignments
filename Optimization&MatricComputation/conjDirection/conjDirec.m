%Conjugate direction method


function  conjDirec(A,b,c,xold)

	%syms x;syms y;syms z;
	%vec=[x y z];
	clc;
	%xold=[2,4]';
	%epsilon=1e-5;

	[m,n]=size(A);
	if(n~=rank(A)),
		disp('matrix is not full rank,so no basis');
		return;
	end;
	d=orth(A);

	grad=A*xold-b;
	%% if g0==0 stop
	if(norm(grad)==0),
		disp('solution is');
		disp(xold);
		quit;
	end;
		
	dold=-grad;
	alpha1=-(grad'*d(:,1))/(d(:,1)'*A*d(:,1));
	xnew=xold+alpha1*d(:,1);
	f_x=0.5*(xold'*A*xold)-xold'*b+c;
	figure(1);
	plot(norm(xold),f_x,'ro');
	xlabel('x value');
	ylabel('f(x)');
	title('convergence');

	hold on;

	for ii=2:n,	
		xold=xnew;
		grad=A*xold-b;

		if(norm(grad)==0),
			disp('solution is');
			disp(xold);
			break;
		end;

		alpha1=-(grad'*d(:,ii))/(d(:,ii)'*A*d(:,ii));
		xnew=xold+alpha1*dold;
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

