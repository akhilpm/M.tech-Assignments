%Realization of Logic OR with perceptron and Delta Rule for Learning
%To realize AND gate change the variable out accrodingly

function logicOR()

	in=[1 1; 1 -1; -1 1; -1 -1]; % bipolar input
	%in=[1 1; 1 0; 0 1; 0 0]; % binary input
	out=[1; 1; 1; 0];
	iterations=50;
	weight=rand(3,1);
	alpha1=0.3;
	bias=-1;

	for i=1:iterations,
		pred=zeros(4,1);
		for j=1:length(in),
			y=weight(1,1)*bias+weight(2,1)*in(j,1)+weight(3,1)*in(j,2);
			%pred(j)=sign(y);   % use with bipolar input
			pred(j)=1/(1+exp(-y));  % use with binary input
			err=out(j)-pred(j);
			weight(1,1)=weight(1,1)+alpha1*err*bias;
			weight(2,1)=weight(2,1)+alpha1*err*in(j,1);
			weight(3,1)=weight(3,1)+alpha1*err*in(j,2);
		end
		%disp(pred);
	end

	disp(pred);		

end

