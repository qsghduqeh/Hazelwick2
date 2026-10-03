mark = int(input("Enter a mark (or -1 to finish): "))

count=0
highest=0
lowest= 100
total=0

while mark != -1:
    
    if mark > 100 or mark < 0 :
        print("INVALID")
    else:
        count= count+1
        total= total+mark
        
        if highest<mark:
            highest=mark

    if lowest>mark:
            lowest=mark

    mark = int(input("Enter a mark (or -1 to finish): "))

if mark == -1:
     print("Average:",total//count)
     print("Highest:", highest)
     print("Lowest:", lowest)
