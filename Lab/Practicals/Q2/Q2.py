def SalesmanData(week):
    totalSales=sum(week)
    remarks=''
    commission=0.0

    # remarks calculation
    if totalSales>=80000:
        remarks="Excellent"
    elif totalSales>=60000 and totalSales<80000:
        remarks="Good"
    elif totalSales>=40000 and totalSales<60000:
        remarks="Average"
    else:
        remarks="Work Hard"

    # commission calculation
    if totalSales<50000:
        commission=0.0
    else:
        commission=0.05*totalSales

    print("Total Sales : ",totalSales)
    print("Commission : ",commission)
    print("Remarks : ",remarks)

    

def main():
    noOfSalesman=int(input("Enter the no of Salesman : "))
    week=[]
    for i in range(noOfSalesman):
        print(f"Enter weekly sales of Salesman {i+1} :- ")
        sales=eval(input("Week 1 : "))
        week.append(sales)
        sales=eval(input("Week 2 : "))
        week.append(sales)
        sales=eval(input("Week 3 : "))
        week.append(sales)
        sales=eval(input("Week 4 : "))
        week.append(sales)
        print("--- Details of Salesman ---")
        print(f"Salesman {i+1} :-")
        SalesmanData(week)
        
    print()

if __name__=='__main__':
    main()
