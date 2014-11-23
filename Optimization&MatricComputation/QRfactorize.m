% QR factorization using Gram-schmidt orthogonalization
function  QRfactorize(A)

	[m,n]=size(A);
	e=zeros(m,n);
	R=zeros(m,n);
	u1=A(:,1);
	e(:,1)=u1/norm(u1);

	% Computing Q matrix
	for i=2:n,
		temp=zeros(n,1);
		a_now=A(:,i);

		for j=i-1:-1:1,
			temp=temp+(a_now'*e(:,j))*e(:,j);
		end;	

		a_now=a_now-temp;
		e(:,i)=a_now/norm(a_now);

	end;	

	%computing R matrix
	for i=1:m,
		for j=i:n,
			R(i,j)=A(:,j)'*e(:,i);
		end;
	end;

	disp('Q matrix');
	disp(e);
	disp('R matrix');	
	disp(R);
	disp('product');
	disp(e*R);	

end

