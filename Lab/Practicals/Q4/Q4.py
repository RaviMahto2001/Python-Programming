def ReturnDigits(num):
    s = set()
    while num > 0:
        s.add( num % 10 )
        num = num // 10
        
    return s
    
def main():
    num = int(input("Enter the Number : "))

    s1 = set()
 
    s1 = ReturnDigits(num)

    print("Digits : ", s1)

if __name__=='__main__':
    main()
    
