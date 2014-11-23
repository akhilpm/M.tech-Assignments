function  GaussPP(A)


    n = size(A,1);  %getting n
    L=eye(n);


%elimination process starts
    for i = 1:n-1,
        permMatrix=eye(n);
        p = i;
        %comparison to select the pivot
        for j = i+1:n,
            if abs(A(j,i)) > abs(A(i,i)), % swapping the rows
                temp = A(i,:);
                A(i,:) = A(j,:);
                A(j,:) = temp;
                idx=j;        
            end
        end

        temp=permMatrix(idx,:);
        permMatrix(idx,:)=permMatrix(i,:);
        permMatrix(i,:)=temp;
        disp(permMatrix);
    
        for j = i+1:n,
            m = A(j,i)/A(i,i);
            L(j,i)=m;
            for k = i+1:n, 
                A(j,k) = A(j,k) - m*A(i,k);
            end
        end
    end

%checking for nonzero of last entry
    if A(n,n) == 0,
        disp('No unique solution');
        return;
    end

    for i=1:n,
        for j=1:n,
            if(i>j),
                A(i,j)=0;
            end;
        end;
    end;    

    disp('L matrix');
    disp(L);
    disp('U matrix');
    disp(A);

end