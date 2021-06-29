 
principal = float(input('Enter amount: '));
time = float(input('Enter time: '));
rate = float(input('Enter rate: '));

 
simple_interest = (principal*time*rate)/100;
compound_interest = principal * ( (1+rate/100)**time - 1);
 
print('Simple interest is: ' ,simple_interest);
print('Compound interest is: '  ,compound_interest );
