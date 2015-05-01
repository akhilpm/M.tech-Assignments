function val = examineExample(i2)

	global X Y m B K ERR alfa C;
	tol=exp(-4);
	alpha2=alfa(i2);
	y2=Y(i2);
	i1=0;
	val=0;
	E2=ERR(i2);
	r2=E2*y2;

	%check the Violation of KKT condition
	if( (r2<-tol && alpha2<C) || (r2>tol && alpha2>0) ),

		no_of_nonZero_alpha=length(find(alfa~=0));
		no_of_nonC_alpha=length(find(alfa~=C));
		%choose alfa with the help of second heuristic
		if(no_of_nonZero_alpha>1 && no_of_nonC_alpha>1),
			maxerr=0;
			for i=1:m,
				if(alfa(i)~=0 && alfa(i)~=C)
					if(abs(ERR(i)-E2)>maxerr)
						maxerr=abs(ERR(i)-E2);
						i1=i;
					end
				end		
			end
			if (takeStep(i1,i2)==1),
				val=1;
				return;
			end	
		end

		pos=randperm(m);
		%loop over non-zero and non-C alpha starting at random point
		for j=1:m,
			if(alfa(pos(j))~=0 && alfa(pos(j))~=C),
				i1=pos(j);
				if (takeStep(i1,i2)==1),
					val=1;
					return;
				end
			end
		end		

		pos=randperm(m);
		%loop over all possible i1 starting at random point
		for j=1:m,
			i1=pos(j);
			if (takeStep(i1,i2)==1),
				val=1;
				return;
			end
		end	
	end	

end

