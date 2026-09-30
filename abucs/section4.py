mark= int(input("Enter a mark (or -1 to finish): "))
count=0
highest=0
lowest=0
total=0

while mark != -1:
    
    if mark>100 and mark<0 :
        print("INVALID")

    if highest<mark:
            highest=mark

            if lowest>mark:
                 lowest=mark

    count= count+1
    total= total+mark
    int(input("Enter a mark (or -1 to finish): "))

if mark== -1 
 print("marks entered: ", count)
print("Average:",total//count)
print("Highest:", highest)
print("lowest:", lowest)