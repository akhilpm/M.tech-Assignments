function visualize()
    X=csvread('data_1.csv');
    X=X(randperm(size(X,1)),:);
    [m, n]=size(X);
    Y=X(:,n);
    X(:,n)=[];
    K=zeros(m,m);
    %sig=std2(X);
    %gama=2*sig^2;
    gama=.8;
    
    one=ones(m,1);
    value=zeros(m,1);
    alfa=zeros(m,1);
    confMatrix=zeros(m,1);

    for i=1:m,
        if Y(i)==1,
            plot(X(i,1),X(i,2),'ro')
        %plot3(xval(i),yval(i),zval(i),'ro')
        else
            plot(X(i,1),X(i,2),'*')    
        %plot3(xval(i),yval(i),zval(i),'*')
        end
        hold on
    end

% compute k with gaussian kernel
%    for i=1:m,
%       for j=1:m,
%            K(i,j)=exp(-gama*power(norm(X(i)-X(j)),2));
%        end
%    end 
    
% compute k with LINEAR and POLYNOMIAL kernel    
    for i=1:m,
        for j=1:m,
            %K(i,j)=X(i,:)*X(j,:)';
            K(i,j)=power(X(i,:)*X(j,:)',7);
        end
    end
    
    alfa=inv((Y*Y').*K)*one;

    count=0;
    for i=1:m,
        value(i)=sum(Y.*alfa.* K(i,:)');
        %fprintf('%d:%d:%d\n',i,sign(value(i)),Y(i));
        predictedClass=sign(value(i));
        actualClass=Y(i);
        if(predictedClass==1 && actualClass==1)
            confMatrix(i)=1;
        elseif(predictedClass==1 && actualClass== -1)
            confMatrix(i)=2;   
        elseif(predictedClass== -1 && actualClass==1)
            confMatrix(i)=3;
        elseif(predictedClass== -1 && actualClass== -1)
            confMatrix(i)=4;
        end
    end  
    %%%%% ESTIMATING PERFORMANCE PARAMETERS  %%%%%%
    sumTP=length(find(confMatrix==1));
    sumFP=length(find(confMatrix==2));
    sumFN=length(find(confMatrix==3));
    sumTN=length(find(confMatrix==4));

    accuracy=(sumTP+sumTN)/(sumTP+sumFP+sumFN+sumTN);
    precision=sumTP/(sumTP+sumFP);
    recall=sumTP/(sumTP+sumFN);
    fMeasure=2*precision*recall/(precision+recall);
    alfa
    fprintf('no of misclassifications :%d\n',sumFP+sumFN);
    fprintf('accuracy :%.3f\n',accuracy);
    fprintf('precision :%.3f\n',precision);
    fprintf('recall/sensitivity :%.3f\n',recall);
    fprintf('F-Measure :%.3f\n',fMeasure);
end

