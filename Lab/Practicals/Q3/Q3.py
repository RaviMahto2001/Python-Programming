def factorial(n):
    res=1
    for i in range(1,n+1):
        res *= i
    return res

def fibonacci(n):
    if n<=1:
        return n
    else:
        a=0
        b=1
        for i in range(2,n):
            a,b=b,a+b
        return b

def Function(n):
    list=[]
    term=fibonacci(n)
    list.append(term)
    list.append(factorial(term))
    return list
    
def main():
    list=[]
    n=int(input("Enter value of n : "))
    list=Function(n)
    print(n,"th term of fibonacci : ",list[0])
    print("factorial of nth term : ",list[1])

if __name__=='__main__':
    main()
    
