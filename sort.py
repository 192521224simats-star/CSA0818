#You  are given an arry arr contain integer element arrange them in increasing order and find the middle value

arr=[90,-90,80,66,78,10]
s=sorted(arr)
print('THE SORTED LIST:',s)
mid=(len(s)-1)//2
print('THE MIDDLE ELEMENT:',s[mid])
