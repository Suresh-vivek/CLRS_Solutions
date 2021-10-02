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

# InsertionSort

  # Arrange list in Ascending order
for j in range(1, num):
    key=my_list[j]

    # Insert my_list[j] into the sorted sequence my_list[1.....j-1]
    i=j-1
    while i>=0 and my_list[i]>key:
        my_list[i+1]=my_list[i]
        i=i-1
    my_list[i+1]=key

print("List in Ascending order",my_list)


  # Arrange list in Descending order
for j in range(1, num):
    key=my_list[j]

    # Insert my_list[j] into the sorted sequence my_list[1.....j-1]
    i=j-1
    while i>=0 and my_list[i]<key:
        my_list[i+1]=my_list[i]
        i=i-1
    my_list[i+1]=key


print("List in Descending order",my_list)

