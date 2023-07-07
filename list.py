list=[1,5,6,8,4,2,5,5,5,5,8]
print(len(list))
print(list)
i=0
while i<=len(list):
    if 5 in list:
        list.remove(5)
    i+=1

print(list)
