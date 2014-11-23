%program to find Condition no of a matrix

function condNo(A)

	invA=inv(A);
	disp('condition no with 1-norm');
	temp1=norm(A,1);
	temp2=norm(invA,1);
	fprintf('K1(A) = %f\n',temp1*temp2);


	disp('condition no with 2-norm');
	temp1=norm(A,2);
	temp2=norm(invA,2);
	fprintf('K2(A) = %f\n',temp1*temp2);


	disp('condition no with inf-norm');
	temp1=norm(A,inf);
	temp2=norm(invA,inf);
	fprintf('Kinf(A) = %f\n',temp1*temp2);


end

