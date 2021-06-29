print('calculating area');
print('AREA OF TRIANGLE');
A=int(input('enter the value of base:'));
B=int(input('enter the value of height:'));
Tarea=(A*B)/2;
print('area of triangle is',Tarea);
print('AREA OF RECTANGLE');
L=int(input('enter the length'));
b=int(input('enter the breath'));
Rarea=L*b;
print('area of rectangle',Rarea);
print('AREA OF SQUARE ');
S=int(input('enter the side of square '));
Sarea=S*S;
print('area of square',Sarea);     
print('AREA OF CIRCLE');
R=int(input('enter the radius of circle'));
 
Carea=3.14*R*R;
print('area of circle',Carea);

print('AREA OF CYLINDER');
C=int(input('enter the radius of cylinder'));
H=int(input('enter the height  of cylinder'));
CYarea=2*3.14*C*H+2*3.14*C*C;
print('area of cylinder',CYarea);
