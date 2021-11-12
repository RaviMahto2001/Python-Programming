import math
def triangle(side1,side2,side3):   
    perimeter=side1+side2+side3
    s=perimeter/2;
    area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return (area,perimeter)
                  
def main():
    print("--- Enter Details of Triangle ---")
    side1=int(input("Enter Side1 :"))
    side2=int(input("Enter Side2 :"))
    side3=int(input("Enter Side3 :"))

    assert side1+side2>side3 and side2+side3>side1 and side3+side1>side2,"Triangle is not valid."
    tupleforResult=triangle(side1,side2,side3)
    print("Area of triangle : ",tupleforResult[0])
    print("Perimeter of triangle : ",tupleforResult[1])

if __name__=='__main__':
    main()
