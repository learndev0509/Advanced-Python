print("Start Code")

try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))

    c=a/b
    print("Division : ",c)

    l=[1,2,3,4]
    index=int(input("Enter Index Number : "))
    print(l[index])

except ZeroDivisionError as e:
    print("Exception Caught : ",e)

except ValueError as e:
    print("Exception Caught : ",e)

except IndexError as e:
    print("Exception Caught : ",e)

except Exception as e:
    print("Exception Caught : ",e)



finally:
    print("Finally Block")
    
print("End Code")
