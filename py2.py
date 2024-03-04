li = []
flag = 1
while(flag):
    ele = int(input("Enter an element"))
    j = len(li)-1
    while(j>=0):
        if(ele>li[j]):
            break
        j=j-1
    if(len(li)==0 or j==len(li)-1):
        li.append(ele)
    else:
        li.insert(j+1, ele)
    print(li)
    flag = int(input("Do you want to insert more element(0/1)"))
