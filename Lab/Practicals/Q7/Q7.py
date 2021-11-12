def replace_vowels(str):
    res=""
    for i in range(len(str)):
        if str[i] in 'aeiou' or str[i] in 'AEIOU':
            res += '#'
        else:
            res += str[i]
    return res

def no_of_words(str):
    return len(str.split())

def ispalindrome(s):
    l=len(s)
    for i in range(l):
        if s[i]!=s[l-i-1]:
            return False
    return True

def main():
    choice=1
    while choice!=6:
        print(" 1. Find the length of string\n",
        "2. Return maximum of three string\n",
        "3. Accept a string and replace all vowels with #\n",
        "4. Find no of words in the given string\n",
        "5. Check whether the string is palindrome or not\n",
        "6. Exit\n")
        choice=int(input("Enter your choice : "))

        if choice==1:
            s1=input("Enter a string : ")
            print("Length of string :",len(s1))
        elif choice==2:
            s1=input("Enter 1st string : ")
            s2=input("Enter 2nd string : ")
            s3=input("Enter 3rd string : ")
            print("Maximum : ",max(s1,s2,s3))
        elif choice==3:
            s1=input("Enter a string : ")
            s1=replace_vowels(s1)
            print("Updated string : ",s1)
        elif choice==4:
            s1=input("Enter a string : ")
            print("No of words in the string : ",no_of_words(s1))
        elif choice==5:
            s1=input("Enter a string : ")
            print("Palindrome : ",ispalindrome(s1))
        elif choice==6:
            exit(0)
        else:
            print("wrong!! choice try again...")
            
        n=int(input("\nDo you want to continue (1/0) : "))
        if n==0:
            exit(0)
            
if __name__=='__main__':
    main()
