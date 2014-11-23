function   matrixNorms(A)


	n=size(A,1);
	colsum=zeros(size(A,1));
	rowsum=zeros(size(A,1));
	oneNorm=0;
	infNorm=0;

	for ii=1:n,
		colsum(ii)=sum(A(:,ii));
	end;
	oneNorm=max(colsum);	

	for ii=1:n,
		rowsum(ii)=sum(A(ii,:));
	end;
	infNorm=max(rowsum);

	fobNorm=sqrt(sum(sum(A.*A)));	


	A=A'*A;
	euclidnorm=sqrt(max(eig(A)));


	fprintf('one Norm :%f\n',oneNorm);
	fprintf('inf Norm :%f\n',infNorm);
	fprintf('Fobenius Norm :%f\n',fobNorm);
	fprintf('Eucledian Norm :%f\n',euclidnorm);
end

