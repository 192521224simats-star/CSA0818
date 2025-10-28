# Area of the circle
a=int(input('Enter the radius:'))
pi=3.14
area=3.14*a**2
print('The area of the circle:', area)

#Swap number
a=int(input('Enter the First Number a:'))
b=int(input('Enter the Second Number b:'))
a,b=b,a
print('The swaped number is a,b:' ,a,b)

# squareroot of the number
a=int(input('Enter the number:'))
sr=a**(1/2)
print('The square root of the number is:',sr)

#Cuberoot of the number
a=int(input('Enter the number:'))
cr=a**(1/3)
print('The cuberoot of the number:',cr)

#celsuis to fahrenheit
cel=float(input('Enter the celsuis value:'))
f=(cel*5/9)+32
print('The Fahrenheit is:',f)

#Fahrenheit to celsuis
f=float(input('Enter tbe fahrenheit value:'))
cel=(f-32)*95
print('The celsuis is :',cel)

# Arthimetic Operator

print('ARTHIMETIC OPERATOR')

a=10
b=2
print('Sum of the number is:', a+b) # Add
print('Subraction of the number is :', a-b)
print('Multiplication of the number is :', a*b) # Multiplication
print('Division of the number is :', a/b) #Normal division result: with float
print('floor Division of the number is :', a//b) #Result : without float
print('Modulas Division of the number is :', a%b) # Result : remanider
print('Exponentional of the number is:',a**b) #Power

#Assignment operator

print('ASSIGNMENT OPERATOR')

a+=2
b+=2
print('addition equal to:',a,' , ',b)
a/=b
b/=a
print('Division equals to:', a,' , ',b)
a-=4
b-=4
print('subration equal to::',a,' , ',b)
a*=b
b*=a
print('multiplication equals to;',a,' , ',b)
a//=b
b//=a
print('Floor Division equals to:',a,' , ',b)
a%=b
b%=a
print('Modulas equals to:',a,' , ',b)
a**=b
b**=a
print('The power equals to :',a,' , ',b)

#Comparsion operator

print('COMPARSION OPERATOR')

print(a==b)
print(a!=b) #Not equal 
print(a>b) #Greater than
print(a<b) #less than
print(a>=b) #Greater than equal to
print(a<=b) #Less than equal to

# Logical operator

print('LOGICAL OPERATOR')

print(a<b and a>b)
print(a<b or a>b)
print(not(a>b))









