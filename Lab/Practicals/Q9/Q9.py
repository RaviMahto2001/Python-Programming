def StdHighPercent(stud):
    maxstudkey = ""
    maxmarks = 0
    for key in stud :
        totalmarks = sum(stud[key])
        if maxmarks < totalmarks :
            maxmarks = totalmarks
            maxstudkey = key
    
    return maxstudkey
    
def main():
    Students = {} # Empty Dictionary
    n = int(input("Enter the No of Students : "))
    
    subjects = ("Math","Science","Computer","English")

    for i in range(1,n+1):
        print("Enter the Detials of Student ",i," :-")
        name = input("Enter the Name of Student : ")
        lst = [0,0,0,0] # to store marks for one student 
        print("Enter the Marks in Subject respectively :-")
        for j in range(4):
            lst[j] = int(input(str(subjects[j] + " : ")))
        Students[name] = lst
            
    std = StdHighPercent(Students)
    print("Student with Highest Percentage : ",std)
            

if __name__=='__main__':
    main()
