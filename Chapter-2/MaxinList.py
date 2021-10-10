# in this code we will try to find Largest number in a list without  sorting
 
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


# Here we consider first element of a list as largest and compare it with other elements linearly.
#if we get a element higher than max we replace it with max and this process continues until loop ends.

max=my_list[0]

if num>1:
    for i in range(0,num):
        if my_list[i]>max:
            max=my_list[i]

else:
    max=my_list[0]

print("Largest number in the list is - ", max)