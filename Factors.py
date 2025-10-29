#Factors

x=int(input('Enter the number:'))
y=[]
print('The Factors of',x,'are:')
for i in range(1,x):
    if x%i==0:
        y.append(i)
print(y)
print('Number of factors :', len(y))
n=int(input('Enter N number:'))
if n==len(y):
    print('INVALID')
else:
    print('First',n,'Factors:')
for  k in range(0,n):
    print(y[k],end='')
