def main():
    t1 = (1,2,5,7,9,2,4,6,8,10)
    
# a) Print another tuple whose values are even numbers in the given tuple.

    l1 = []
    
    for i in t1:
        if i%2==0:
            if i not in l1:
                l1.append(i)

    ans1 = tuple(l1)

    print("Given Tuple : ",t1)
    print("Tuple with Even values of given tuple :-")
    print(ans1)

# b) Concatenate a tuple t2 = (11,13,15) with t1

    t2 = (11,13,14)
    list1 = list(t1)

    # concatenating t2 in t1 with help of list1
    for i in t2 :
        list1.append(i)

    t1 = tuple(list1)

    print("After Concatenating t2=(11,13,15) in t1=(1,2,5,7,9,2,4,6,8,10) : ")
    print(t1)

# c) Return Max and Min value from this tuple

    print("t1 : ",t1)
    print("Max of t1 : ",max(t1))
    print("Min of t1 : ",min(t1))
    
if __name__=='__main__':
    main()
