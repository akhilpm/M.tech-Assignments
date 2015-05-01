xval=[1 1 -1 -1];
yval=[1 -1 -1 1];
%xval=[1 1 1 1];
%yval=[1 1 1 1];
%zval=[sqrt(2) -sqrt(2) sqrt(2) -sqrt(2)];

out=[-1 1 -1 1];

for i=1:4,
    if out(i)==1,
        plot(xval(i),yval(i),'ro')
        %plot3(xval(i),yval(i),zval(i),'ro')
    else
        plot(xval(i),yval(i),'*')    
        %plot3(xval(i),yval(i),zval(i),'*')
    end
    hold on
end
 xlim([-2 2])
 ylim([-2 2])
 %zlim([-2 2])
 xlabel('x')
 ylabel('y')
 %zlabel('z')
 title('input space')
 %title('Feature space')
 legend('+ve Y','-ve Y')
 