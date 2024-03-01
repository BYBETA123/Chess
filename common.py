def Bubble_Sort_Ascending(MyList):
    MaxIndex = len(MyList)-1
    MaxIndex = MaxIndex -1
    n = len(MyList)-1
    for i in range(MaxIndex):
        for j in range(n):
            if MyList[j] > MyList[j+1]:
                temp = MyList[j]
                MyList[j] = MyList[j+1]
                MyList[j+1] = temp
        n = n-1
    print(MyList)

def Bubble_Sort_Descending(MyList):
    MaxIndex = len(MyList)-1
    MaxIndex = MaxIndex -1
    n = len(MyList)-1
    for k in range(2):
        for i in range(MaxIndex):
            for j in range(n):
                if MyList[j]<MyList[j+1]:
                    temp = MyList[j+1]
                    MyList[j+1]=MyList[j]
                    MyList[j]=temp
            n = n-1
    print(MyList)

def InsertionSort(mylist):
    n = len(mylist)

    for i in range(1,n):
        value = mylist[i]
        hole = i
        while hole>0 and mylist[hole-1]>value:
            mylist[hole] = mylist[hole-1]
            hole = hole -1
        mylist[hole] = value

def InsertionSort_Reverse(mylist):
    n=len(mylist)
    for i in range(1,n):
        value=mylist[i]
        hole=i
        while hole>0 and value>mylist[hole-1]:
            mylist[hole] = mylist[hole-1]
            hole=hole-1
        mylist[hole]=value

def Alpha_Counter(word):
    Alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Counter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    word_list=[]
    for char in word:
        word_list.append(char)
    print(word_list)
    print(word_list[0])

    for i in range(len(word_list)):
        for j in range(len(Alphabet)):
            if word_list[i]==Alphabet[j]:
                Counter[j]+=1

    for i in range(26):
        if Counter[i]>0:
            print(f"{Alphabet[i]}:{Counter[i]}")

def BinarySort(mylist, searchitem):
    first=0
    last = len(mylist)-1
    found=False
    searchfailed=False
    while not found and not searchfailed:
        middle = (first + last)//2
        if mylist[middle]==searchitem:
            found = True
        else:
            if first >= last:
                searchfailed = True
            else:
                if mylist[middle]>searchitem:
                    last=middle-1
                else:
                    first=middle+1
    if found==True:
        print(f"found at position: {middle}")
    else:
        print("Item not present in array/list")