function golden()

    a=-2;                            % start of interval
    b=2;                            % end of interval
    epsilon=1e-5;                   % accuracy value
    maxiter= 50;                  
    tau=double((sqrt(5)-1)/2);      % golden ratio, around 0.618
    k=0;                            % iteration counter


    x1=a+(1-tau)*(b-a);             % computing initial values
    x2=a+tau*(b-a);

    f_x1=f(x1);                     
    f_x2=f(x2);

    figure(1);
    plot(x1,f_x1,'o');            
    hold on;
    plot(x2,f_x2,'o');
    xlabel('x value');
    ylabel('f(x)');
    title('convergence');

    while ((abs(b-a)>epsilon) && (k<maxiter))
        k=k+1;
        if(f_x1<f_x2)
            b=x2;
            x2=x1;
            x1=a+(1-tau)*(b-a);
        
            f_x1=f(x1);
            f_x2=f(x2);
        
            plot(x1,f_x1,'o');
        else
            a=x1;
            x1=x2;
            x2=a+tau*(b-a);
        
            f_x1=f(x1);
            f_x2=f(x2);
        
            plot(x2,f_x2,'o')
        end;
    
    end;


% chooses minimum point
    if(f_x1<f_x2)
        fprintf('x_min=%f\n', x1);
        fprintf('f(x_min)=%f \n', f_x1);
        plot(x1,f_x1,'ro');
    else
        fprintf('x_min=%f\n', x2);
        fprintf('f(x_min)=%f \n', f_x2);
        plot(x2,f_x2,'ro');
    end;

end