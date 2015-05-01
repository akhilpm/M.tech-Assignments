function  gradient()

	X=csvread('data_1.csv');
    X=X(randperm(size(X,1)),:);
    [m, n]=size(X);
    Y=X(:,n);
    X(:,n)=[];
    KT=zeros(m,m);
    gama=.09;
    ERR=-Y;
    C=.7;
    %epsilon=exp(-5);
    tol=exp(-3);
    alfa=zeros(m,1);
    b=-0.0473971456320590;


    %computing K for training points
    for i=1:m,
       for j=1:m,
            KT(i,j)=exp(-gama*power(norm(X(i,:)-X(j,:)),2));
            %KT(i,j)=power(X(i,:)*X(j,:)',13); 
        end
    end
    flag=0;
    figure;
    cnt=0;
    while cnt<30,
    	for i=1:m,
    		y=Y(i);    		
    		alfa(i)=alfa(i)+(1/KT(i,i))*(1-y*(sum(Y.*alfa.* KT(i,:)')));
    		if alfa(i)<0,
    			alfa(i)=0;
    		elseif alfa(i)>C,
    			alfa(i)=C;
    		end	    
    		value=sum(Y.*alfa.* KT(i,:)')+.01;					
    		ERR(i)=value-y;
    		E=ERR(i);
			r=E*y;
    		%if( (r>-tol && alfa(i)<C) || (r<tol && alfa(i)>0) ),
    		%	flag=flag+1;
    		%end
    	end
        sumAlfa=sum(alfa);
        dualObj=sumAlfa-0.5*((alfa.*Y)'*KT*(alfa.*Y));   			
        primalObj=2*dualObj-sumAlfa-dualObj*(sumAlfa-dualObj+1);
        primalObj=-primalObj/(1+dualObj);
        plot(cnt,primalObj,'ro');
        hold on
        plot(cnt,dualObj,'*');
        cnt=cnt+1;
        if flag==m,
            break;
        else
            flag=0;
        end

    end
    legend('primalObj','dualObj');
    %disp(alfa);
    %for i=1:m,
    %    for j=1:train,
    %        K(i,j)=exp(-gama*power(norm(X(i,:)-X(j,:)),2));
            %K(i,j)=power(X(i,:)*X(j,:)',1);    
    %    end    
    %end    
    value=zeros(m,1);
    confMatrix=zeros(m,1);
    %for i=1:m,
    %    value(i)=sum(Y.*alfa.* KT(i,:)')+b;
    %    fprintf('%d:%d:%d\n',i,sign(value(i)),Y(i));
    %end    				

    for i=1:m,
        value(i)=sum(Y.*alfa.* KT(i,:)')+b;
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
    fprintf('no of misclassifications :%d\n',sumFP+sumFN);
    fprintf('accuracy :%.3f\n',accuracy);
    fprintf('precision :%.3f\n',precision);
    fprintf('recall/sensitivity :%.3f\n',recall);
    fprintf('F-Measure :%.3f\n',fMeasure);    

    %%%%% PLOTTING DECISION BOUNDARY %%%%%%
    figure;
    d = 0.1;
    [X1, X2] = meshgrid(min(X(:,1)):d:max(X(:,1)),min(X(:,2)):d:max(X(:,2)));
    sv=find(alfa>0);

    for i=1:m,
        if alfa(i)==0,
            if(Y(i)==1),
                plot(X(i,1),X(i,2),'ro');
            else
                plot(X(i,1),X(i,2),'*'); 
            end       
            %plot3(xval(i),yval(i),zval(i),'ro')
        else
            if(Y(i)==1),
                plot(X(i,1),X(i,2),'ko');
            else
                plot(X(i,1),X(i,2),'k*'); 
            end       
        end        
        hold on
    end
    legend('+ve class','-ve class','Black */0 S. Vectors');
    vals=zeros(size(X1));
    for i = 1:size(X1,2),
        this_X=[X1(:, i), X2(:, i)];
        for k=1:size(this_X,1),
            kgrid=zeros(m,1);
            %size(X(j,:))
            %size(this_X(k,:)')
            for j=1:m,
                kgrid(j)=exp(-gama*power(norm(X(j,:)-this_X(k,:)),2));
                %kgrid(j)=power(X(j,:)*this_X(k,:)',13);
            end
            val=sum(Y.*alfa.*kgrid)+b;
            vals(k,i)=sign(val);
        end        
    end

    %contour(X1,X2,vals,50);
    contour(X1, X2, vals, [0 0], 'Color', 'b');
    %figure;
    %surf(X1,X2,vals);
    length(sv)
end

