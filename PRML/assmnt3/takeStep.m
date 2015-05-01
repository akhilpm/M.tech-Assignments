function val = takeStep(i1,i2)

	global X Y m B K ERR alfa C;
	Eps=exp(-4);
	val=0;
	if (i1==i2),
		return;
	end
	%disp('1st ret 0');
	alpha1=alfa(i1);
	alpha2=alfa(i2);
	y1=Y(i1);
	y2=Y(i2);
	E1=ERR(i1);
	E2=ERR(i2);
	s=y1*y2;

	% calculate L and H limits
	if y1==y2,
		L=max(0,alpha1+alpha2-C);
		H=min(C,alpha1+alpha2);
	else,
		L=max(0,alpha2-alpha1);	
		H=min(C,C-alpha1+alpha2);
	end
	
	if(L==H),
		return;
	end
	%disp('2nd ret 0');
	eta=2*K(i1,i2)-K(i1,i1)-K(i2,i2);
	if(eta<0),
   		a2=alpha2-y2*(E1-E2)/eta;
	  	if (a2<L),
	       a2=L;
  	   	elseif (a2>H),
       		a2=H;
   		end
   	else,	

   		f1=y1*(E1+B)-alpha1*K(i1,i1)-s*alpha2*K(i1,i2);
	   	f2=y2*(E2+B)-s*alpha1*K(i1,i2)-alpha2*K(i2,i2);
   		L1=alpha1+s*(alpha2-L);
   		H1=alpha1+s*(alpha2-H);
   		Lobj=L1*f1+L*f2+0.5*L1^2*K(i1,i1)+0.5*L^2*K(i2,i2)+s*L*L1*K(i1,i2);
   		Hobj=H1*f1+H*f2+0.5*H1^2*K(i1,i1)+0.5*H^2*K(i2,i2)+s*H*H1*K(i1,i2);

	   	%set a2
   		if (Lobj>Hobj+Eps),
       		a2=L;
   		elseif(Lobj<Hobj-Eps)
       		a2=H;
	   	else
    	   a2=alpha2;
   		end
   		%a2,i2
   		%pause;
   	end
   	%a2
   	if(abs(a2-alpha2)<Eps*(a2+alpha2+Eps)),
   		%disp('a2<alpha2');
   		val=0;
   		return;
   	end	
   	a1=alpha1+s*(alpha2-a2);
   	%disp('last ret 0');
   	%update threshold to reflect change in lagrange
	b1=ERR(i1)+y1*(a1-alpha1)*K(i1,i1)+y2*(a2-alpha2)*K(i1,i2)+B;
	b2=ERR(i2)+y1*(a1-alpha1)*K(i1,i2)+y2*(a2-alpha2)*K(i2,i2)+B;
	bold=B;
	if (b1==b2),
    	B=b1;
	else,
    % one of these alphas is at an edge
  		if a1~=H||a1~=L,
        	B=b1;
	    elseif a2~=H||a2~=L,
    	    B=b2;
	    else,
    	    B=(b1+b2)/2;
	    end
	end

	%update error cache
	for i=1:m,
		if(alfa(i)~=0 && alfa(i)~=C)
			if (i==i1 || i==i2)
				ERR(i)=0;
			else
				ERR(i)=ERR(i)+y1*(a1-alpha1)*K(1,i)+y2*(a2-alpha2)*K(2,i)+bold-B;
			end
		end			
	end	
	%update Alpha values
	alfa(i1)=a1;
	alfa(i2)=a2;
	val=1;
	return;
	
end

