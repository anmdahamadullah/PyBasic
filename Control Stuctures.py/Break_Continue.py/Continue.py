


#continue বর্তমান iteration Skip করে, পরবর্তী iteration শুরু করে।..

for number in range(10):
    if(number % 2 != 0): # Only Collect even Value...
        continue 
    print("Even Value=",number)

print("\n")

for number in range(10):
    if (number % 2 == 0): # Only Collect Odd Value...
        continue         
    print("Odd Value=",number)
