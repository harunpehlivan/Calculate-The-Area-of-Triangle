a  = float (input('Enter first side:'))
b = float (input('Enter second side:'))
c = float (input('Enter Third side:'))
s = (a + b + c) / 2
#calculate the area 
area = (s*(s - a)*(s - a)*(s - c)) ** 0.5
print('The area of triangle is %0.2f ' %aera)