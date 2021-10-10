# First take list as a input from user

print("Enter the number of elements in list")
num=int(input())

list=[]

for i in range(1,num+1):
    if i==1:
        place="st"
    elif i==2:
        place="nd"
    elif i==3:
        place="rd"
    else:
        place="th"
    
    print("Enter the ", i,place, " element of list")
    ele=int(input())
    list.append(ele)

my_list=list
print("your list is",my_list)

print("Enter the number to be search in the list")
value = int(input())

def linear_search(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return i
    
    return -1

result = linear_search(my_list,num,value)

if result == -1:
    print("Element is not found")
else:
    print("Element is present at index ",result)

    