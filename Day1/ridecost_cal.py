#Code to calculate daily travelling cost

distance=float(input("Enter total distance travelled in a day" )) 
avg=float(input("Enter the mileage of car:" ))
cost=float(input("Enter the cost of diesel per litre:" ))
totFuel=(distance)/(avg)
totCost=totFuel*(cost)
print("The total cost to travel to office daily:" ,totCost)
