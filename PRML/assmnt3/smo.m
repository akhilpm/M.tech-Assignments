%data_1 : C=2 degree = 5 best for polynomial kernel : 1 misclassification

function smo()
    global X Y m B K ERR alfa C;
    %X=csvread('data_1.csv');
    X=load('iono.txt');
    [m, n]=size(X);
    Y=X(:,n);
    X(:,n)=[];
    %X=featureScale(X);
    K=zeros(m,m);
    value=zeros(m,1);
    confMatrix=zeros(m,1);
    cost=zeros(m,1);
    gama=.7;  %g=0.5 C=8 best for gaussian 
    C=8;
    counter=0;
    %lambda=.8;
    
    %compute k with gaussian kernel
    for i=1:m,
       for j=1:m,
            K(i,j)=exp(-gama*power(norm(X(i)-X(j)),2));
            %K(i,j)=power(X(i,:)*X(j,:)',1);
        end
    end

    alfa=zeros(m,1);
    numChanged=0;
    examineAll=1;
    ERR=-Y;
    B=0;
    while(numChanged>0 || examineAll),

    	numChanged=0;
    	if(examineAll)
    		for i=1:m,
    			numChanged=numChanged+examineExample(i);
    		end
        else
    		for i=1:m,
    			if (alfa(i)~=0 && alfa(i)~=C),
    				numChanged=numChanged+examineExample(i);
    			end
    		end
        end 
    	%numChanged
    	if(examineAll==1),
    		examineAll=0;   
        elseif (numChanged==0),
    		examineAll=1;
    	end	

        counter=counter+1;
        cost(counter)=sum(alfa)-0.5*alfa'*K*alfa;
    	%pause;									
    end
    cost(counter:m)=[];
    length(cost);
    counter=counter-1;
    plot(1:counter,cost);
    hold on;

    disp(alfa');
    for i=1:m,
        value(i)=sum(Y.*alfa.* K(i,:)')-B;
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
    no_of_svectors=length(find(alfa~=0));
    fprintf('no of misclassifications :%d\n',sumFP+sumFN);
    fprintf('accuracy :%.3f\n',accuracy);
    fprintf('precision :%.3f\n',precision);
    fprintf('recall/sensitivity :%.3f\n',recall);
    fprintf('F-Measure :%.3f\n',fMeasure);
    fprintf('No of support vectors:%d\n',no_of_svectors);
    fprintf('Bias:%f\n',B);

end

