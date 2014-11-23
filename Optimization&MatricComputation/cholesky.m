function  cholesky(A)

	n=size(A,1);
	R=zeros(n,n);

	for i=1:n,
		rsum=0;
		for k=1:i-1,
			rsum=rsum+(R(k,i)*R(k,i));
		end;

		if((A(i,i)-rsum)==0),
			disp('matrix is not positive definite');
			break;
		end;
		
		R(i,i)=sqrt(A(i,i)-rsum);

		for j=i+1:n,
			rjsum=0;
			for k=1:i-1,
				rjsum=rjsum+R(k,i)*R(k,j);
			end;
			
			R(i,j)=(A(i,j)-rjsum)/R(i,i);
		end;
	end;
	
	R					


end

