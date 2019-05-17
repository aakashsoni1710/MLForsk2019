#to calculate wieghted score of student

as1 = int(input("Enter The score in Assignment1:"))

as2 = int(input("Enter The score in Assignment2:"))

as3 = int(input("Enter The score in Assignment3:"))

e1 = int(input("Enter The score in Exam1:"))

e2 = int(input("Enter The score in Exam2:"))

ws = ( as1 + as2 + as3 ) *0.1 + (e1 + e2 ) * 0.35

print("Weighted Score is:",ws)
