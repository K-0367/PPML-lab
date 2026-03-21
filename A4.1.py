#wap to print the second largest and second smallest element in a list of 10 integers without sorting it
arr=[]
x=int(input("ente the no of elements:"))
for i in range(x):
    m=int(input('enter the elements:'))
    arr.append(m)
    for i in range(len(arr)-1):
        for k in range(len(arr)-j-1):
            if arr[k]>arr[k=1]:
print("the second array is: ")
print(arr)
second_arr=arr[-2]
second_smallest=arr[-2]
print("second larregest element is;",second_arr)
print("second smallest element is:", second_smallest)