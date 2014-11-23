%====INPUT==========
% v=initial vector
% A=given input matrix
% m should be less than n,(length(v))

%===OUTPUT=========
% (m+1) orthonormal vectors
% an Upper Hessenberg matrix of size (m+1)*m

function arnoldi(A,v,m)

	v1=v/norm(v);
	n=length(v);
	%disp('v1');
	%disp(v1);
	vprev=v1;
	H=zeros(m+1,m);
	V=zeros(n,m+1);
	V(:,1)=v1;

	for k=1:m,

		vcap=A*vprev;

		for j=1:k,
			H(j,k)=V(:,j)'*vcap;
			vcap=vcap-H(j,k)*V(:,j);
		end;
		
		H(k+1,k)=norm(vcap);
		if H(k+1,k)==0,
			disp('cannot proceed');
			return;
		end;
		
		V(:,k+1)=vcap/H(k+1,k);	

	end;	

	disp('orthonormal vectors');
	disp(V);
	disp('Hessenberg matrix');
	disp(H);


end

