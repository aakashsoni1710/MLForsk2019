#FizzBuzz
num=0
while (num < 100):
    num=num+1
    if(num%3==0 and num%5==0):
        print("FuzzBizz")
        continue
    elif(num%3==0):
        print("Fuzz")
        continue
    elif(num%5==0):
        print("Bizz")
        continue
    print(num)
    
        
    