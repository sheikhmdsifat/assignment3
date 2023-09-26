try:
     hours=float(input("write your work hours "))
     rate=float(input("write here the rate "))
     if hours > 40:
        salary = 40 * rate + ((hours - 40) * 1.5 * rate)
     else:
         salary = rate * hours
        
     print("Salary is:",salary)
except:
         print("wrong input")

