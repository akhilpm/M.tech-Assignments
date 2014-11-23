%###### LU DECOMPOSITION  ###########
% this will work only for square matrices


function luFactorise(A)
   

    [m n]=size(A);
    if(m~=n),
        error('This is not a square matrix');
    end;
        
    L=eye(n);
    
    for i=1:n,
        if(A(i,i)==0),
            fprintf('Not possible to factorize\nleading principal submatic is singular\n');
            break;
        end;
        
        for j=i+1:n,
            divider=A(i,i)/A(j,i);
            L(j,i)=divider;
            %idx=idx+1;
            A(j,:)=A(i,:)-A(j,:)*divider;
        end;
                
    end;    
            
    disp('L matrix')
    disp(L);
    
    disp('U matrix')
    disp(A);
    
end    