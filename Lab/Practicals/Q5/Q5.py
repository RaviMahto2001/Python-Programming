import sys
sys.path.append("F:\studyfiles\Python\Lab\Practicals\Q3")
import Q3

def SumOfSeries(x,n):
    res=0.0
    prev=0.0
    print(f"series upto {n} terms :-")
    for i in range(0,2*n,2):
        if i%4==0:
            res = res + x**i/Q3.factorial(i)
            print(res-prev,end=' ')
            prev=res
        else:
            res = res - x**i/Q3.factorial(i)
            print(res-prev,end=' ')
            prev=res
    print()
    return res

def main():
    x=eval(input("Enter the value of x : "))
    n=int(input("Enter the no of terms : "))
    result=SumOfSeries(x,n)
    print(f"Sum of Series upto {n} terms : {result}")

if __name__=='__main__':
    main()
