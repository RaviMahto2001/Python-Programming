def main():
    ln=[10,2,13,4023,23,452]
    ls=['Hello','Ravi','I','was','he']
    print("List taken for example")
    print(ln)
    check=1
    for element in ln:
        if type(element)!=int:
            check=0
            break
    if check==1:
        #counting no of odd values
        nood=0
        for el in ln:
            if el%2==0:
                nood += 1
        print(f"No of odd values in list {ln} is {nood} ")

        #display in reverse form
        print("Display list in reverse order :-")
        print(ln[::-1])
        #find a element
        element=int(input("Enter a element to find in list : "))
        if element in ln:
            print("element found")
        else:
            print("element not found")
        #remove a element
        element=int(input("Enter a element to remove from the list : "))
        if element in ln:
            ln.remove(element)
            print("updated list :-")
            print(ln)
        else:
            print("There is no such element in the list")
        #sort in des order
        print("list in descending order :-")
        ln.sort()
        ln.reverse()
        print(ln)
    else:
        print("not a numeric list")

    print("\nList taken for example")
    print(ls)
    check=1

    for element in ls:
        if type(element)!= type(''):
            check=0
            break
            
    if check==1:
        #max of elements in list
        print(f"Max of  {ls} is ",max(ls))
        #display in reverse form
        print("Display List in reverse order :-")
        print(ls[::-1])
        #find a element
        element=input("Enter a element to find in list : ")
        if element in ls:
            print("element found")
        else:
            print("element not found")
        #remove a element
        element=input("Enter a element to remove from the list : ")
        if element in ls:
            ls.remove(element)
        else:
            print("There is no such element in the list")
        #sort in des order
        print("list in descending order :-")
        ls.sort()
        ls.reverse()
        print(ls)
    else:
        print("not a list of string")


    print("\n\n")
    l1=[10,20,30,40,50]
    l2=[12,10,30,23,45,34]

    print("We have two list as :- ")
    print(l1)
    print(l2)
    lc=[]
    for el in l1 :
        if el in l2 :
            lc.append(el)
    print("Common Elements")
    print(lc)
    
if __name__=='__main__':
    main()
