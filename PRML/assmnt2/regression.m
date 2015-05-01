function regression()

	X=load('data_2.csv');
    X=X(randperm(size(X,1)),:);
    [m, n]=size(X);
    Y=X(:,n);
    X(:,n)=[];
    KT=zeros(m,m);
    gama=.2;
    C=.3;
    epsilon=exp(-5);
    tol=exp(-3);
    alfa=zeros(m,1);
    alfaStar=zeros(m,1);
    b=.9;
    ERR=Y-epsilon*ones(m,1);

    %computing K for training points
    for i=1:m,
       for j=1:m,
            KT(i,j)=exp(-gama*power(norm(X(i,:)-X(j,:)),2));
            %KT(i,j)=power(X(i,:)*X(j,:)',3); 
        end
    end
    flag=0;
    figure;
    cnt=0;

    while cnt<500,
        for i=1:m,
            y=Y(i);
            if ERR(i)>0,         
                alfa(i)=alfa(i)+(1/KT(i,i))*(y-sum((alfa-alfaStar).* KT(i,:)')-epsilon);
                if alfa(i)<0,
                    alfa(i)=0;
                elseif alfa(i)>C,
                    alfa(i)=C;
                end
            else
                alfaStar(i)=alfaStar(i)+(1/KT(i,i))*(-y+sum((alfa-alfaStar).* KT(i,:)')-epsilon);
                if alfaStar(i)<0,
                    alfaStar(i)=0;
                elseif alfaStar(i)>C,
                    alfaStar(i)=C;
                end
            end             
            value=sum((alfa-alfaStar).* KT(i,:)')+b;                  
            ERR(i)=y-value-epsilon;
            E=abs(y-value);
            %E=ERR(i);
            %r=E*y;
            if(abs(E-epsilon)<tol),
               flag=flag+1;
            end
        end

        cnt=cnt+1;
        if flag==m,
            break;
        else
            flag=0;
        end

    end
    cnt
    value=zeros(m,1);
    MSE=0;
    for i=1:m,
        value(i)=sum((alfa-alfaStar).* KT(i,:)')+b;
        MSE=MSE+(Y(i)-value(i))^2;
    end
    MSE=sqrt(MSE)/m
    ERR=ERR+epsilon;
    mean(ERR)

    for i=1:m,
        if alfa(i)==0,
            plot3(X(i,1),X(i,2),Y(i),'ro');
            %plot3(xval(i),yval(i),zval(i),'ro')
        else
            plot3(X(i,1),X(i,2),Y(i),'*');
        end        
        hold on
    end
    legend('data points','support vectors');
    d = 0.1;
    [X1, X2] = meshgrid(min(X(:,1)):d:max(X(:,1)),min(X(:,2)):d:max(X(:,2)));
    sv=find(alfa>0);

    vals=zeros(size(X1));
    for i=1:size(X1,2),
        this_X=[X1(:, i), X2(:, i)];
        for k=1:size(this_X,1),
            kgrid=zeros(m,1);
            %size(X(j,:))
            %size(this_X(k,:)')
            for j=1:m,
                kgrid(j)=exp(-gama*power(norm(X(j,:)-this_X(k,:)),2));
                %kgrid(j)=power(X(j,:)*this_X(k,:)',3);
            end
            vals(k,i)=sum((alfa-alfaStar).*kgrid)+b;
        end        
    end

    contour(X1,X2,vals,50);
    %contour(X1, X2, vals, [0 0], 'Color', 'b');
    %figure;
    %surf(X1,X2,vals);
    length(sv)
end

